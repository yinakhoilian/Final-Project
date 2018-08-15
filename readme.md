## **Instructions for the game**
Just run the final_game.py file and follow the instructions in the game. Enjoy!

## **Motivation behind this game**
When I first moved to New York three years ago, I struggled to find a nice apt within my budget. I wanted to create a game that illustrates this. It was great to use some of the concepts from class (functions, conditionals, dictionary etc).

## **Challenges and Lessons Learned**
I enjoyed debugging the game and getting it to work! Going to Jess' office hours and Google were particularly helpful. I initially wanted to create a class and objects for the various neighborhoods. Took awhile for it to work, since I was using _init_ instead of __init__. Little did I know that it was two connected underscores before and after! Afterwards, I decided to use a dictionary instead: the keys were the neighborhoods and the values were the "happiness" scores for each neighborhood. Depending on how you answered the preference questions, it will increase (or decrease) the score for a particular neighborhood. For instance, if you enjoy celebrity sightings, Tribeca would score higher compared to the other neighborhoods on this question. From a technical perspective, I'm happy I was able to get the incremental changes to work. If your favorite activity is to "pretend to be a tourist", this will increase the score for Midtown. However if you were also annoyed by your encounter with tourists when they were blocking the street, this will lower the score for Midtown and net out your previous response.
