#Comp 1020 Assginment 3
import random


import string


def random_choice_from_list(phrase_list):


   return random.choice(phrase_list)






def make_list_from_file(filename):


   with open(filename, 'r') as file:


       return [line.strip() for line in file.readlines()]


def make_response_dictionary(response_list):


   response_dict = {}


   for line in response_list:


       key, response = line.split(',', 1)


       response_dict[key.strip()] = response.strip()


   return response_dict


class ChatBot:


   def __init__(self, greetings_file, responses_file, default_response):


       self.greetings = make_list_from_file(greetings_file)


       responses = make_list_from_file(responses_file)


       self.keyword_and_response = make_response_dictionary(responses)


       self.default_response = default_response


   def greet(self):
       return random_choice_from_list(self.greetings)


   def respond(self, human_text):
       human_text = human_text.lower()


       human_text = human_text.translate(str.maketrans('', '', string.punctuation))


       words = human_text.split()
       potential_responses = []
       for word in words:
           if word in self.keyword_and_response:


               potential_responses.append(self.keyword_and_response[word])
       if not potential_responses:


           return self.default_response


       return random_choice_from_list(potential_responses)
