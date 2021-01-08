#!/usr/bin/env python3

import random
import math
import statistics

# Name of the mod
mod_name = "Condition Overload"
# Drop chance of the mod from 0 to 1
# 1% would be 0.01
mod_drop_chance = 0.000225
# Number of runs to simulate
# Higher number gives a more accurate guess and takes more time
# 100 000 is a lot
run_count = 100000
# Thing you do to get the mod
action = "Deimos Carnis/Jugulus/Leaping Thrasher/Saxum kill"

def grind():
    attempts = 0
    # random.random() < mod_drop_chance has the same chance of happening as the mod dropping
    while random.random() >= mod_drop_chance:
        attempts += 1
    return attempts
    
data = []
print(f"LF {mod_name}, press Ctrl-C to stop")
try:
    while len(data) < run_count:
        data.append(grind())
        if len(data) % (run_count/1000) == 0:
            print(f"\r{(100*len(data))/run_count}% complete", end="")
except KeyboardInterrupt: # Getting impatient? Press Ctrl-C to make the program stop and make do with what it got
    pass
print()
print(f"{math.ceil(statistics.fmean(data))}±{math.ceil(statistics.pstdev(data))} {action}s to get the mod according to {len(data)} simulations")