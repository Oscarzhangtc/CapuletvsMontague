Oscar Zhang

# Project Overview
Having been curious about old english literatures, I wanted to analyze the familiar story of
Romeo and Juliet and compare the frequency of speech between the two houses Capulets and
Montague as well as the non-house characters. From a software design aspect, I also wanted
to practice working with text files and build a function program from scratch. To avoid running
the restriction imposed by project gutenberg, I used pickle to save and pre-load the data for
analysis without having to pull the text and query the api every time.

# To run this project
Make sure [python](https://www.python.org/downloads/) is installed on your device. 

Run in terminal:
```bash
python textMining.py
```

# Implementation
To begin, in my textMining.py file, I used Python's pickle module to store a local copy of the text
for it to be loaded, parsed and analyzed in the textProcessing.py file. I chose dictionaries to
represent my processed data as best represent key-value pairs with increments. Intuitively, the
key is the name of the character in the play, and value is the house he/she/they belong to and
the the number of times they speak. The structure of my code is divided into 5 components
each with their individual function. The first is to create a dictionary of characters and their
associated houses. The second component is for parsing the text file/script loaded in to pickle
and handle some special cases. The third is to refer back to the dictionary and output the
number of characters from each house. The fourth is to calculate the number of times each
character speaks. The fifth and last is to use the output from the fourth step to compute the
averages of the speech frequency for each house.
Since text from Gutenberg or texts in general varies significantly depending on the genre and
writer, I made specific parsing targeted solely for the chosen text. For example, when I came
across a few character names that consist of two words rather than one, I needed to hard-code
my function to recognize them. Furthermore, I was able to use the feature of plays that it is
composed mostly of dialogues and the name of the character comes conveniently before they
speak. Running the program on another text, especially one that’s not a play, it would not yield
accurate results.

# Results
```bash
There are 6 Montagues and 13 Capulets in Romeo and Juliet.{'Chor.': ('Neither', 2),
'Samp.': ('Capulet', 20), 'Greg.': ('Capulet', 15), 'Abr.': ('Montague', 5), 'Bal.': ('Montague',
9), 'Ben.': ('Neither', 64), 'Tyb.': ('Capulet', 17), 'Officer.': ('Neither', 2), 'Citizens.':
('Neither', 2), 'Cap.': ('Capulet', 53), 'Wife.': ('Capulet', 20), 'Cap. Wife.': ('Capulet', 0),
'Mon.': ('Montague', 10), 'M. Wife.': ('Montague', 2), 'Pri.': ('Neither', 0), 'Prin.': ('Neither',
0), 'Rom.': ('Montague', 163), 'Par.': ('Capulet', 23), 'Nurse.': ('Montague', 100), 'Jul.':
('Capulet', 117), 'Mer.': ('Neither', 62), 'Friar.': ('Neither', 52), 'Laur.': ('Neither', 4), 'John.':
('Neither', 5), 'Peter.': ('Capulet', 5), 'Apoth.': ('Neither', 4), '1. Serv.': ('Capulet', 3), '2.
Serv.': ('Capulet', 2), '3. Serv.': ('Capulet', 1), '2. Cap.': ('Capulet', 2)}
{'Montague': (6, 289), 'Capulet': (13, 278), 'Neither': (11, 197)}
{'Montague': 48.166666666666664, 'Capulet': 21.384615384615383, 'Neither':
17.90909090909091}
```
![ Data visualized](/images/visualization.png)
In the graph, the characters with highest numbers of speaking times are visualized. the main
driver of dialogues is unsurprisingly the main character Romeo and Juliet. And the most of the
frequently spoken characters are Montagne characters. However, what stood out is the fact the
Capulet(the character) has significant more lines than Montagne(the character), despite being
an irreplaceable role, Montague(the character) only spoke 10 times. Only 5 sets of characters
presented in the graph because there are no more pairable Montagne and Capulet
counterparts, and all other house associated characters play a much smaller role.
