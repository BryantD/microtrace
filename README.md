# microtrace

Micro = microblog (Twitter, Mastodon) and trace = tracery. See, it's easy.

This used to be just my Twitter Blades in the Dark bot but when I got
off Twitter I went the rest of the way towards generalizing it. You can
find the output from one bot using this at https://botsin.space/@doskvolscores.

## Usage

```
microtrace.py [-h] --grammar GRAMMAR [--maxlen MAXLEN] [--print]
                     [--toot] [--tweet] --config CONFIG

Tracery-based microblogging bot

options:
  -h, --help         show this help message and exit
  --grammar GRAMMAR  JSON grammar
  --maxlen MAXLEN    Maximum message length
  --print            Print
  --toot             Toot
  --tweet            Tweet
  --config CONFIG    Config file
```

### Config

The configuration file is a TOML file, as follows:

```
[twitter]
consumer_key = "XXX"
consumer_secret = "XXX"
access_token = "XXX"
access_token_secret = "XXX"

[mastodon]
access_token = "XXX"
base_url = "XXX"
```

If you're not using it for one of the services, you can leave the appropriate
section out.

## Contributions

* Kate Compton's [Tracery](https://tracery.io/)
* Allison Parrish's awesome [pytracery](https://github.com/aparrish/pytracery) port of Tracery
* [Tweepy](http://www.tweepy.org), which is nice and simple
* [Mastodon.py](https://mastodonpy.readthedocs.io/en/stable/), also simple and easy
* John Harper's [Blades in the Dark](https://bladesinthedark.com/), a tabletop RPG (with permission)
* Off Guard Games' [Scum & Villainy](https://offguardgames.com/scum-and-villainy/), another tabletop RPG (with permission)
