# What the heck is this?
Thought of this after a frustrating game of monopoly (one of those games I intensely dislike but play nonetheless). I wanted to calculate the exact probability of a player landing on every square of the board and what exactly is the best strategy to win.

<br>

# I want to win as well, how do I run this?
```
python3 monopoly.py [noIterations]
```
Where `noIterations` is the number of player turns you want this script to simulate

<br>

# Does this script simulate everything from the base game?
Yes, it does. Community chest, treasure, jail, (mostly) everything's in here. 

Note: for the sake of simplicity a few things have been excluded, such as the payouts from the treasure and chance cards (in fact, money as a whole has <b>NOT</b> been added, I will add it in due time). Another thing is that ails don't require the player to stay in it for 3 turns (might add this at a later date). 

<br>

# What is the result?
### 1,000,000 Iterations
Sets | Probability
---- | -----------
Browns | 4.4425% 
Light Blues | 6.8938% 
Pinks | 7.6058% 
Oranges | 8.543%
Reds | 8.695%
Yellows | 7.9265%
Greens | 7.8613%
Dark Blues | 5.0376%
Station | 11.1829%
Utilities | 5.4089%
Jail | 5.9911%

<br>

### Afterwords
Feel free to copy, edit, reuse this script however you like. It's not the most efficient nor I suppose the most "realistic", so use this script and its results at your own peril :)
