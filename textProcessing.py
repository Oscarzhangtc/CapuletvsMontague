'''Mini Project 3: Text Mining
Software Design Spring 2020
Oscar Zhang

This script parses the text of Romeo Juliet from Project Gutenberg, counts how often each character speaks
speaks, and returns the average number of times of the Capulets spoke versus Montague. '''

import string
import pickle

input_file = open('shakespeare.pickle', 'rb')

reloaded = pickle.load(input_file)

text_list= list(reloaded.split())
# this transforms loaded textfile into a list of strings of words

character_dict = {'Chor.' : 'Neither',
             'Samp.' : 'Capulet',
             'Greg.' : 'Capulet',
             'Abr.' : 'Montague',
             'Bal.' : 'Montague',
             'Ben.' : 'Neither',
             'Tyb.' : 'Capulet',
             'Officer.' : 'Neither',
             'Citizens.' : 'Neither',
             'Cap.' : 'Capulet',
             'Wife.' : 'Capulet',   # Wife of Capulet
             'Cap. Wife.' : 'Capulet', #  wife of Capulet is also referred to as 'Cap. Wife' twice
             'Mon.' : 'Montague',
             'M. Wife.' : 'Montague',
             'Pri.' : 'Neither',
             'Prin.' : 'Neither', # prin is seldomly referred to as pri. (2lines)
             'Rom.' : 'Montague',
             'Par.' : 'Capulet',
             'Nurse.' : 'Montague',
             'Jul.' : 'Capulet',
             'Mer.' : 'Neither',
             'Friar.' : 'Neither', # usually used to refer to Friar Larurence, once used to refer to Friar John,
             'Laur.' : 'Neither', # usually same person with Friar.
             'John.' : 'Neither',
             'Peter.' : 'Capulet',
             'Apoth.' : 'Neither',
             '1. Serv.' : 'Capulet',
             '2. Serv.' : 'Capulet',
             '3. Serv.' : 'Capulet',
             '2. Cap.' : 'Capulet',
             }





def handle_abbrev(text_list):
    '''Deals with all 2-word character abbreviations in the script such as
    '1. Serv' and '2. Cap'
    here we combining any string that starts with 'M.', '1.', '2.', '3.' with the string that comes after it
    to have the full name of the characters
    '''
    for i in range(len(text_list)):
        if text_list[i] in ['M.', '1.', '2.', '3.']:
            # if the word IS one of the 4 words
            # 'M.' to account for 'M. Wife'
            # Does not account for 'Cap. Wife' (because 'Cap.' is a different character

            text_list[i] = text_list[i] + str(' ') + text_list[i+1]
    return text_list

def count_character_house(character_dict):
    '''Counts how many capulet and montague characters are in the dictionary.'''
    number_of_montague = 0
    number_of_capulet = 0
    # initialize var
    for value in character_dict.values():
        if value == 'Montague':
            number_of_montague = number_of_montague + 1
        elif value == 'Capulet':
            number_of_capulet  = number_of_capulet  + 1
    answer = 'There are ' + str(number_of_montague) + ' Montagues and ' + str(number_of_capulet) + ' Capulets in Romeo and Juliet.'
    print(answer)

count_character_house(character_dict)

modified_text_list = handle_abbrev(text_list)

def all_character_count_mentions(character_dict, text_file):
    '''Counts number of times each key/character-name in character_dict appears in modified_text_list.
    takes the character_dict and the text_file

    note: 'Cap. Wife.' and 'Wife.' are the same person but is counted as 2 separate characters'''
    mentions = {}
    for name in character_dict.keys():
            times_mentioned = 0
            for word in text_file:
                # brute force solution...goes through every word in text_file and find all matching word
                if word == name:
                    times_mentioned += 1
            mentions[name] = times_mentioned
    #print(mentions)
    return mentions
    # the returned mentions is a dictionary that maps character names to number of times they speak.

all_character_count_mentions(character_dict, modified_text_list)

all_mentions_dict = dict(all_character_count_mentions(character_dict,modified_text_list))



def average_house_speaking(all_mentions_dict, character_dict):
    '''
    Takes the two dictionaries as input arguments:
        1. all_mentions_dict: a dict that maps character names to how many times they speak
        2. character_dict: a the initialized  dict that maps character names to house
    Calculates average number of times montague and capulet characters speak.
    '''
    for key,value in all_mentions_dict.items():
        all_mentions_dict[key] = (character_dict[key],value)
        # re-map each key of all_mentions_dict with a new value that includes the house
        # and set it as the new all_mentions_dict
    print(all_mentions_dict)

    #initialize counts
    mention_count = { 'Montague': (0, 0),
                  'Capulet': (0, 0),
                  'Neither': (0, 0) }
    for name, (house, mentions) in all_mentions_dict.items():
        characters, total_mentions = mention_count[house]
        # initialize characters and total mentions
        mention_count[house] = (characters + 1, total_mentions + mentions)
        # increment character and total mentions
    print(mention_count)
    average = {house: total / characters for house, (characters, total) in mention_count.items()}
    return average
    #Returns average number of times characters of each house speak.
print(average_house_speaking(all_mentions_dict,character_dict))
