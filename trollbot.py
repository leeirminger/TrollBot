# importing regex and random libraries
import re
import random


class TrollBot:
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # random starter questions
    random_tasks = (
        "You can ask me why I am here. ",
        "You can ask me to cube a number. ",
        "You can ask me for an opinion of mine. "
    )

    def __init__(self):
        self.trollbabble = {'troll_opinion': r'.*your\sopinion.*', #'.*\s*opinion.*'
                            'answer_why_intent': r'.*why\sare.*',
                            'cubed_intent': r'.*cube.*(\d+)',
                            'skyisblue': r'.*sky\sis\sblue.*' #'.*sky\s*.*blue.*'
                            }

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(
            rf"Hi {self.name}, I'm Trollbot. Want to have an engaging conversation?\n")
        if will_help in self.negative_responses:
            print("Ok, bye bye!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay, adios!")
                return True

    def chat(self):
        reply = input(random.choice(self.random_tasks)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.trollbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'troll_opinion':
                return self.troll_opinion()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'cubed_intent':
                return self.cubed_intent(found_match.groups()[0])
            elif found_match and intent == 'skyisblue':
                return self.skyisblue()
        if not found_match:
            return self.no_match_intent()

    def troll_opinion(self):
        responses = ("I love the sound of the color orange\n",
                     "Nonsense is the most sensible\n")
        return random.choice(responses)

    def answer_why_intent(self):
        responses = ("Your arguments are feeble!\n", "I am here to help your ideas become less structurally weak.\n",
                     "I am just playing around. C'mon man!\n")
        return random.choice(responses)

    def cubed_intent(self, number):
        number = int(number)
        cubed_number = number * number * number
        return f"The cube of {number} is {cubed_number}. Isn't that cool?\n"
    
    def skyisblue(self):
        responses = ("The sky is not blue!\n", "You have the color wrong!\n",
                     "Are you colorblind!?\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
        "Why do you think that?\n", "How do you know/n", "What difference does it make?\n", "I do not agree. Can you say something that makes sense?\n",
        "Interesting. Please can state that more clearly and in a less peculiar way?\n", "What if you are wrong?\n", "Why?\n",
        "How do you think I feel when you say that?\n")
        return random.choice(responses)


TrollBot = TrollBot()
TrollBot.greet()