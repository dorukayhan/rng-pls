#!/usr/bin/env python3
"""
RNG Pls - find out how much effort is needed to make RNGesus smile at you
Copyright (C) 2021 Doruk Ayhan

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import random
import math
import statistics
import argparse
from sys import exit

def main():
    # Read argv
    args = read_argv()
    drop_name = args.drop_name
    drop_chance = args.drop_chance / 100 # Convert % chance to [0, 1] chance
    action = args.action
    run_count = args.run_count
    # Short-circuit special cases
    if drop_chance <= 0.0: # Impossible drop, avoid infinite loop
        print(f"{drop_name} is unobtainable")
        exit(0)
    if drop_chance >= 1.0: # Guaranteed drop, no need for real calculation
        print(f"Your next {action} will get you {drop_name}. What are you waiting for?")
        exit(0)


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

def read_argv():
    parser = argparse.ArgumentParser(description="find out how much effort is needed to make RNGesus smile at you")
    parser.add_argument("drop_chance", type=float, help="percent drop chance of the thing you're looking for without the percent sign (e.g. 0.0225)")
    parser.add_argument("--drop_name", "-d", help="name of the thing you're looking for (e.g. Condition Overload) (default: \"Thing\")", default="Thing")
    parser.add_argument("--action", "-a", help="what you'll do in-game to get the thing (e.g. Deimos Carnis/Jugulus/Leaping Thrasher/Saxum kill) (default: \"attempt\")", default="attempt")
    parser.add_argument("--run_count", "-c", type=int, help="number of runs to simulate (default: 100 000)", default=100000)
    return parser.parse_args()

if __name__ == "__main__":
    main()