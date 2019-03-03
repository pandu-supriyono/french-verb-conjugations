# French Verb Conjugations
A JSON list of all verbs in the French language and their corresponding conjugations.
The list of verbs are forked from [Einenlum/french-verbs-list](https://github.com/Einenlum/french-verbs-list) and the conjugations are parsed from [la-conjugaison.nouvelobs.com](https://la-conjugaison.nouvelobs.com/).

## Dependencies for parsing
If for whatever reason you wish to run the python script to re-parse all the conjugations for the verbs found in verbs.json, you can do so by running verbs.py after having installed the relevant libraries:
```
$ sudo pip install beautifulsoup4 unidecode
```

Python 3.x was used to create the scripts.
If you prefer to use 2.x, you may need to use urllib2 vis-à-vis urllib.

## Work in progress
This is a work in progress.
Currently, the list only contains conjugations of the "mode indicatif".
Some verbs found in verbs.json do not have a corresponding entry in the website from which the list is parsed.
Those missing verbs are found in the folder missing_verbs/.
Additionally, note that the accuracy and/or quality of the conjugations may not be entirely accurate due to the parsing process.



