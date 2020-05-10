'''
Author: Oscar Zhang
Project 3: Text Mining
Software Design

A script that pull the text shakespeare's Romeo & Juliet from ProjectGutenberg online and pickles it'''

import requests
shakespeare_full_text = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt').text
# simplest version of Romeo and julet in Glutenberg also without UTF-encoding
print(shakespeare_full_text)

import pickle

# Save data to a file (will be part of your data fetching script)
f = open('shakespeare.pickle', 'wb')
pickle.dump(shakespeare_full_text, f)
f.close()
