#!/usr/bin/env python3

import argparse
import json
import tweepy
import tracery
from tracery.modifiers import base_english
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def generate():
    parser = argparse.ArgumentParser(description='Blades in the Dark tweetbot')
    parser.add_argument('--grammar', required=True, help='JSON grammar')
    parser.add_argument('--maxlen', default=280, type=int, help='Max tweet length')
    parser.add_argument('--print', help='Print score', action='store_true')
    parser.add_argument('--tweet', help='Tweet score', action='store_true')
    args = parser.parse_args()

    with open(args.grammar) as data_file:
        rules = json.load(data_file)

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    score = ''
    while len(score) == 0:
        score = grammar.flatten('#origin#')
        if len(score) > args.maxlen:
            score = ''

    if args.print:
        print(score)
    if args.tweet:
        api.update_status(score)

if __name__ == '__main__':
    generate()
