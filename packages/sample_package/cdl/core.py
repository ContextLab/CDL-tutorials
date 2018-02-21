import random
from helpers import *

class chatter:
    def make(gender, category=None):
        """
        input:
            + gender: str - gender of lab member ('m'/'f')
            + category (optional): str - type of lab member ('post_doc', 'student', 'PI')

        output:
            + str - phrase simulating CDL lab chit chat
        """

        males = ['jeremy', 'andy', 'paxton']
        females = ['lucy', 'gina', 'kirsten', 'emily']

        if category == 'PI':
            name = 'jeremy'

        elif gender == 'm':
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
            mood_phrase = phrase + 'it\'s AWESOME!!'
        else:
            mood_phrase = phrase + 'it\'s terrible.'

        return(mood_phrase)

class convo:
    def make(gender1, gender2, valence1, valence2):
        sentence1 = chatter.add_valence(chatter.make(gender1), valence1)
        sentence2 = chatter.add_valence(chatter.make(gender2), valence2)

        conversation = 'Hey! ' + sentence1 + '.       Oh really? Well, ' + sentence2

        return(conversation)
