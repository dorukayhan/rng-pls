#!/usr/bin/env python3

import random
import math
import statistics

def main():
    import sys
    # Is user stupid or/and in need of help?
    if len(sys.argv) < 4 or sys.argv[1] == "-h":
        help(sys.argv[0])
        sys.exit(0)
    # Read argv
    drop_name = sys.argv[1]
    drop_chance = float(sys.argv[2]) / 100 # Convert % chance to [0, 1] chance
    action = sys.argv[3]
    run_count = int(sys.argv[4]) if len(sys.argv) > 4 else 100000
    # Short-circuit special cases
    if drop_chance <= 0.0: # Impossible drop, avoid infinite loop
        print(f"{drop_name} is unobtainable")
        sys.exit(0)
    if drop_chance >= 1.0: # Guaranteed drop, no need for real calculation
        print(f"Your next {action} will get you {drop_name}. What are you waiting for?")
        sys.exit(0)


    data = []
    print(f"LF {run_count} {drop_name}s, press Ctrl-C to end early")
    try:
        while len(data) < run_count:
            data.append(grind(drop_chance))
            if len(data) % 100 == 0: # Progress indicator
                # The carriage return at the beginning and lack of a newline causes the line to be overwritten on normal OSs like Linux and Windows
                # This doesn't work on OSs that use CR as newline and I won't make it work, switch to a real OS please
                print(f"\r{(100*len(data))/run_count}% complete".ljust(60), end="")
    except KeyboardInterrupt: # Getting impatient? Press Ctrl-C to make the program stop and make do with what it got
        pass
    # CR again to overwrite the progress indicator
    print(f"\rSimulation done, interpreting the results...{len(data)} simulations is a lot and {'may' if len(data) < 5000000 else 'will'} take a while to deal with...", end="")
    print(f"\r{math.ceil(statistics.fmean(data))}±{math.ceil(statistics.pstdev(data))} {action}s to get {drop_name} according to {len(data)} simulations".ljust(124))

def grind(drop_chance):
    attempts = 0
    # random.random() < drop_chance has the same chance of happening as the thing dropping
    while random.random() >= drop_chance:
        attempts += 1
    return attempts

def help(filename):
    print(f"Usage: {filename} [drop_name] [drop_chance] [action] [run_count]")
    print("      drop_name: name of the thing you're looking for (e.g. Condition Overload)")
    print("    drop_chance: % drop chance of the thing without the % sign (e.g. 0.0225)")
    print("         action: what you'll do in-game to get the thing (e.g. Deimos Carnis/Jugulus/Leaping Thrasher/Saxum kill)")
    print("      run_count: number of runs to simulate, defaults to 100000 if not entered")

if __name__ == "__main__":
    main()