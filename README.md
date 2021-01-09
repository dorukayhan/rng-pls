# RNG Pls

[Warframe](https://store.steampowered.com/app/230410/Warframe/) is ~~Farming Simulator 2013 with guns~~ ~~what "video games cause violence" people think every game is~~ ~~a bug showcase~~ ~~Tencent's latest spyware container in the form of~~ a pseudo-MMO grindfest in the form of a PvE third-person "shooter" that I may be playing too much.

As is the case with all grindy games where the 100% "win" condition is obtaining every collectible that goes into some inventory space, some things in the game are rarer than others (e.g. ["you hit more than twice as hard in close quarters"](https://warframe.fandom.com/wiki/Pressure_Point) vs ["you hit _a hell lot_ more than twice as hard in close quarters"](https://warframe.fandom.com/wiki/Condition_Overload)). Luckily for all players' sanity, the devs decided to [disclose exactly how rare everything is](https://warframe.com/droptables), and a bunch of good Samaritans integrated their data to [the game's wiki](https://warframe.fandom.com). This allows players to quickly check how much time they'll need to get particular things.

One day, I felt like taking this "quickly check how much time I'll need to get [a particular thing](https://warframe.fandom.com/wiki/Flame_Gland)" really far with some ad hoc Python. This is that bit of ad hoc Python, generalized to work with any collectible from any grindfest.

## Installation and usage

1. Get Python 3.9
2. `git clone git@github.com:dorukayhan/rng-pls.git`
3. `cd rng-pls`
4. `./rng-pls.py -h` or `py -3 rng-pls.py -h`
5. Follow the instructions