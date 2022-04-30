Final project for Colin Haywood in SI507

You will need the following modules enabled to run the program (some may be built-in):

requests

json

requests_cache

BeautifulSoup from bs4

webbrowser

The program imagines that you have a character in the game Elden Ring and want to decide on a weapon for that character. You input 4 statistics: Strength, Dexterity, Intelligence, and Faith, and the program scrapes the Elden Ring wiki, compares input character statistics with weapon requirements listed on the wiki, and recommends a weapon for the user's character.

The data structure was originally going to use trees, but per a meeting with Professor Madamanchi on 2/29/2022, he instructed (and presumably allowed) that I should use filtering rather than trees to solve this problem; therefore the data is organized as a list of lists.
