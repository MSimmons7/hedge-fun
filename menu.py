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


class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = regex.match('^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid phone number',
                cursor_position=len(document.text))  # Move cursor to end

print('Welcome to HedgeFun, a comprehensive algorithmic trading CLI.')

api_endpoint = 'https://paper-api.alpaca.markets'

questions = [
    {
        'type': 'input',
        'name': 'api_key',
        'message': 'Please input your Alpaca API key:',
    },
]

answers = prompt(questions, style=custom_style_2)
pprint(answers)