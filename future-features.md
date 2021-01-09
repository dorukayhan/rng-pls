# Ideas for stuff to add in the future

## Multithreading

The loop that spams `grind(drop_chance)` calls can be trivially parallelized.

## Grinding for multiple things

A rank 5 [Arcane Energize](https://warframe.fandom.com/wiki/Arcane_Energize) is one of the best things one can have in Warframe, and getting one requires fusing 21 rank 0 Energizes, which are already hard enough to get when there are no [rogue artificial aliens](https://warframe.fandom.com/wiki/Operation:_Orphix_Venom) [hard inting](https://warframe.fandom.com/wiki/Operation:_Scarlet_Spear). One would think finding out the effort required to get a rank 5 Energize is as simple as running `./rng-pls.py "Arcane Energize" 5 "Hydrolyst capture"` and multiplying the result by 21. I don't trust this rule-of-thumb.

## Pity

After 89 Wish pulls without a 5\* character or weapon, Genshin Impact forces the 90th pull to be 5\*. RNG Pls currently can't simulate pity mechanics like this.