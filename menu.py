# -*- coding: utf-8 -*-
"""
* Input prompt example
* run example by writing `python example/input.py` in your console
"""
from __future__ import print_function, unicode_literals
import regex
from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

from examples import custom_style_2

api_endpoint = 'https://paper-api.alpaca.markets'
api_key = ''
secret_key = ''

def main():
    ask_for_api_keys()

print('Welcome to HedgeFun, a comprehensive algorithmic trading CLI.')


def ask_for_api_keys():
    questions = [
        {
            'type': 'list',
            'name': 'response',
            'message': 'Would you like to input your API keys?',
            'choices': ['Yes', 'No']
        }
    ]
    answer = prompt(questions, style=custom_style_2)
    if (answer['response'] == 'Yes'):
        get_credentials()
    else:
        print('Your credentials are set')    

def get_credentials():
    questions = [
        {
            'type': 'input',
            'name': 'api_key',
            'message': 'Please input your Alpaca API key:',
        },
        {
            'type': 'input',
            'name': ''
        }
    ]

    answers = prompt(questions, style=custom_style_2)
    pprint(answers)

if __name__ == "__main__":
    main()