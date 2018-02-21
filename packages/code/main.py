import random
from helpers import *

def lab_chatter(gender, category=None):
    """
    input:
        + gender: str - gender of lab member ('M'/'F')
        + category (optional): str - type of lab member ('post_doc', 'student', 'PI')

    output:
        + str - phrase simulating CDL lab chit chat
    """

    males = ['jeremy', 'andy', 'paxton']
    females = ['lucy', 'gina', 'kirsten', 'emily']

    if category == 'PI':
        name = 'jeremy'

    elif gender == 'M':
        if category == 'post_doc':
            name = 'andy'
        elif category == 'student':
            name = 'paxton'
        else:
            name = random.choice(males)

    else :
        if category == 'post_doc':
            name = 'gina'
        elif category == 'student':
            name = random.choice(['lucy', 'kirsten'])
        else:
            name = random.choice(females)

    # output #
    utterance = first_phrase(name)
    return(utterance)


def add_valence(phrase, mood):
    """
    input:
        + str - mood ('+', '-')
        + NOTE : can use output from lab_chatter

    output:
        + string appended with mood-appropriate phrase
    """

    if mood == '+':
        mood_phrase = phrase + 'it\'s AWESOME!! :D'
    else:
        mood_phrase = phrase + 'it\'s so terrible.'

    return(mood_phrase)
