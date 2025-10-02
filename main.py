#!/usr/bin/env python3
"""
Meditation App — Terminal version
Features:
 - Guided meditations (5/10/15 min)
 - Custom-length timer
 - Box-breathing guided exercise
 - Short body-scan guided meditation
 - Session logging to meditation_log.csv
 - Simple progress display and gentle bells
No external dependencies.
"""

import time
import sys
import os
import csv
from datetime import datetime

LOG_FILE = "meditation_log.csv"

# Utility functions

def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def bell():
    """
    Try to play a gentle bell:
    - On Windows, try winsound.Beep (if available)
    - Otherwise print ASCII bell (may or may not beep)
    """
    try:
        if os.name == "nt":
            import winsound
            winsound.Beep(440, 300)
        else:
            # terminal bell
            sys.stdout.write("\a")
            sys.stdout.flush()
    except Exception:
        # fallback: print a star separator
        print("\n***\n")

def log_session(kind, duration_min, notes=""):
    row = {
        "timestamp": datetime.now().isoformat(sep=" ", timespec="seconds"),
        "type": kind,
        "duration_min": duration_min,
        "notes": notes
    }
    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "type", "duration_min", "notes"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

def print_centered(s, width=60):
    print(s.center(width))

def progress_bar(total_seconds, prefix=""):
    start = time.time()
    while True:
        elapsed = time.time() - start
        if elapsed >= total_seconds:
            break
        percent = elapsed / total_seconds
        bar_len = 30
        filled = int(percent * bar_len)
        bar = "[" + "#" * filled + "-" * (bar_len - filled) + "]"
        mins_left = int((total_seconds - elapsed) // 60)
        secs_left = int((total_seconds - elapsed) % 60)
        sys.stdout.write(f"\r{prefix} {bar} {mins_left:02d}:{secs_left:02d} remaining")
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\r" + " " * 80 + "\r")  # clear line

# Guided scripts

GUIDED_5 = [
    (0, "Sit comfortably, spine straight, hands relaxed."),
    (8, "Close your eyes softly. Bring attention to the breath."),
    (20, "Follow your inhale... and your exhale. No need to control."),
    (60, "If the mind wanders, gently bring it back to the breath."),
    (120, "Feel the body—weight on the seat, ground beneath you."),
    (180, "Notice sounds outside without judging them."),
    (240, "Feel gratitude for this time. When ready, deepen the breath."),
]

GUIDED_10 = [
    (0, "Make yourself comfortable. Relax your shoulders."),
    (10, "Close your eyes. Take three slow breaths, in and out."),
    (30, "Allow your breath to find its own natural rhythm."),
    (90, "Scan the body from head to toe—release any tension."),
    (180, "Focus on the rise and fall of the chest or belly."),
    (300, "If thoughts appear, label them 'thinking' and let them pass."),
    (420, "Extend your out-breath by one second — just softly."),
    (540, "Bring kindness to yourself. Hold this moment of calm."),
    (570, "When ready, wiggle your fingers and toes and open eyes slowly."),
]

GUIDED_15 = [
    (0, "Begin seated or lying down. Let the body soften."),
    (12, "Take a deep inhalation and a slow exhalation."),
    (40, "Scan your body and breathe into any tight spots."),
    (120, "Now focus on breath sensations — cool at the nostrils, warm at the exhale."),
    (300, "If a thought grabs you, observe it, then return to the breath."),
    (480, "Stay with a gentle attention; do not push or force."),
    (660, "Offer a short gratitude for something simple (a breath, a sound)."),
    (840, "Slowly deepen your breath and return awareness to the room."),
    (880, "When ready, open your eyes and take this calm into your next minutes."),
]

# Main features

def guided_session(script, duration_min):
    clear()
    total_seconds = duration_min * 60
    start_time = time.time()
    bell()
    i = 0
    while True:
        elapsed = time.time() - start_time
        if elapsed >= total_seconds:
            break
        # play any script lines whose time has come
        while i < len(script) and elapsed >= script[i][0]:
            print()
            print_centered(script[i][1])
            i += 1
        remaining = max(0, total_seconds - elapsed)
        progress_bar(remaining, prefix="Guided:")
        # small sleep already handled inside progress_bar
    bell()
    print_centered("Session complete — gently come back when ready.")
    log_session(f"Guided {duration_min} min", duration_min)
    input("Press Enter to return to menu...")

def custom_timer(duration_min):
    clear()
    print_centered(f"Custom silent timer — {duration_min} minutes")
    bell()
    progress_bar(duration_min * 60, prefix="Timer:")
    bell()
    print_centered("Time's up. Well done.")
    log_session("Custom timer", duration_min)
    input("Press Enter to return to menu...")

def box_breathing(cycles=4, inhale=4, hold=4, exhale=4):
    """
    Box breathing: inhale-hold-exhale-hold with equal counts.
    cycles: how many full cycles to run.
    """
    clear()
    print_centered("Box Breathing Exercise")
    print()
    print(f"Cycles: {cycles}, Pattern: Inhale {inhale}s — Hold {hold}s — Exhale {exhale}s — Hold {hold}s")
    bell()
    time.sleep(1.2)
    for c in range(1, cycles + 1):
        print(f"\nCycle {c}/{cycles}")
        # Inhale
        for t in range(inhale, 0, -1):
            sys.stdout.write(f"\rInhale  : {t:2d} ")
            sys.stdout.flush()
            time.sleep(1)
        # Hold
        for t in range(hold, 0, -1):
            sys.stdout.write(f"\rHold    : {t:2d} ")
            sys.stdout.flush()
            time.sleep(1)
        # Exhale
        for t in range(exhale, 0, -1):
            sys.stdout.write(f"\rExhale  : {t:2d} ")
            sys.stdout.flush()
            time.sleep(1)
        # Hold after exhale
        for t in range(hold, 0, -1):
            sys.stdout.write(f"\rHold    : {t:2d} ")
            sys.stdout.flush()
            time.sleep(1)
        print()
    bell()
    print("\nBox breathing complete. Notice how you feel.")
    log_session("Box breathing", cycles * (inhale + hold + exhale + hold) / 60)
    input("Press Enter to return to menu...")

def body_scan(duration_min=10):
    """
    A simple body-scan guided meditation that walks down the body.
    The script is timed proportionally to the duration.
    """
    clear()
    parts = [
        "top of the head — notice sensations there",
        "forehead and eyes — soften the muscles",
        "jaw and mouth — let the jaw relax",
        "neck and shoulders — release weight into the chair",
        "arms, hands, and fingers — soft and heavy",
        "chest and belly — breathe into the chest",
        "lower back and hips — let them sink",
        "thighs and knees — feel support",
        "calves and shins — let go",
        "feet and toes — notice contact with the floor"
    ]
    total_seconds = duration_min * 60
    per_part = total_seconds / len(parts)
    bell()
    print_centered(f"Body-scan — {duration_min} minutes")
    time.sleep(1.2)
    for idx, part in enumerate(parts, start=1):
        print()
        print_centered(f"Focus: {part}")
        progress_bar(per_part, prefix=f"Part {idx}/{len(parts)}:")
    bell()
    print_centered("Body scan complete. Slowly reconnect with the room.")
    log_session(f"Body-scan {duration_min} min", duration_min)
    input("Press Enter to return to menu...")

def show_log():
    clear()
    if not os.path.exists(LOG_FILE):
        print("No log found yet. Your sessions will be saved to meditation_log.csv")
        input("Press Enter to return to menu...")
        return
    print_centered("Meditation Log")
    print("-" * 60)
    with open(LOG_FILE, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        if not rows:
            print("No sessions logged yet.")
        else:
            for r in rows[-20:]:  # show last 20 entries
                print(f"{r['timestamp']:20} | {r['type'][:20]:20} | {r['duration_min']:>5} min | {r['notes']}")
    print("-" * 60)
    input("Press Enter to return to menu...")

def main_menu():
    while True:
        clear()
        print("=" * 60)
        print_centered("Calm CLI — Simple Meditation App")
        print("=" * 60)
        print("Choose an option:")
        print(" 1) Guided — 5 minutes")
        print(" 2) Guided — 10 minutes")
        print(" 3) Guided — 15 minutes")
        print(" 4) Custom silent timer")
        print(" 5) Box breathing exercise")
        print(" 6) Body-scan meditation (10 min default)")
        print(" 7) View session log")
        print(" 0) Exit")
        print()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            guided_session(GUIDED_5, 5)
        elif choice == "2":
            guided_session(GUIDED_10, 10)
        elif choice == "3":
            guided_session(GUIDED_15, 15)
        elif choice == "4":
            try:
                mins = float(input("Enter duration in minutes (e.g., 7.5): ").strip())
                if mins <= 0:
                    raise ValueError
                custom_timer(mins)
            except ValueError:
                print("Invalid duration. Press Enter to continue...")
                input()
        elif choice == "5":
            try:
                cycles = int(input("Number of cycles (default 4): ") or "4")
                inhale = int(input("Inhale seconds (default 4): ") or "4")
                hold = int(input("Hold seconds (default 4): ") or "4")
                exhale = int(input("Exhale seconds (default 4): ") or "4")
                box_breathing(cycles=cycles, inhale=inhale, hold=hold, exhale=exhale)
            except ValueError:
                print("Invalid numbers. Returning to menu...")
                time.sleep(1.2)
        elif choice == "6":
            try:
                mins = float(input("Duration minutes (default 10): ") or "10")
                body_scan(int(mins))
            except ValueError:
                print("Invalid input. Returning to menu...")
                time.sleep(1.2)
        elif choice == "7":
            show_log()
        elif choice == "0":
            clear()
            print_centered("May you have a calm and peaceful day — goodbye.")
            break
        else:
            print("Unknown choice. Try again.")
            time.sleep(1.0)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nSession interrupted. Take care.")
