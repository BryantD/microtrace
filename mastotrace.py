#!/usr/bin/env python3

# Copyright 2018-2022 Bryant Durrell
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse
import configparser
import json
from mastodon import Mastodon
import tracery
from tracery.modifiers import base_english


def generate():
    parser = argparse.ArgumentParser(description='Tracery-based tweetbot')
    parser.add_argument('--grammar', required=True, help='JSON grammar')
    parser.add_argument('--maxlen', default=280, type=int, help='Maximum message length')
    parser.add_argument('--print', help='Print score', action='store_true')
    parser.add_argument('--toot', help='Toot score (Mastodon)', action='store_true')
    parser.add_argument('--config', help='Config file', required=True)
    args = parser.parse_args()
    
    config = configparser.ConfigParser()
    config.read(args.credentials)
    consumer_key = config['keys']['consumer_key']
    consumer_secret = config['keys']['consumer_secret']
    access_token = config['keys']['access_token']
    access_token_secret = config['keys']['access_token_secret']

    with open(args.grammar) as data_file:
        rules = json.load(data_file)

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    body = ''
    while len(body) == 0:
        body = grammar.flatten('#origin#')
        if len(body) > args.maxlen:
            body = ''

    body = ' '.join(body.split())

    if args.print:
        print(body)
    if args.mastodon:
	mastodon = Mastodon(
	    access_token=mastodon_access_token,
	    api_base_url = 'https://botsin.space')
	mastodon.toot(text)

if __name__ == '__main__':
    generate()