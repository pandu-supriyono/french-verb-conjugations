#!/usr/bin/env python

from cjg import conjugaison
import json


with open('verbs.json') as jsonFile:
    verbsJson = json.load(jsonFile)

verbs = verbsJson['verbs']
firstGroup = verbsJson['verbs']['first_group']
secondGroup = verbsJson['verbs']['second_group']
thirdGroup = verbsJson['verbs']['third_group']

def parseConjugations(verbGroup):
    print("Initializing parsing: " + groupName)
    conjugations = {}
    missingVerbs = []

    counter = 0
    for verb in verbGroup:
        try:
            conjugations[verb] = conjugaison(verb)
            print(verb)
        except Exception:
            missingVerbs.append(verb)
            print("ERROR: Failed to parse " + verb)
            pass
        counter +=1
        print(str(counter) + "/" + str(len(verbGroup)))

    with open("conjugations/" + groupName.lower().replace(" ", "_") + '.json', 'w') as f:
        json.dump(conjugations, f, indent=2)

    with open("missing_verbs/missing_" + groupName.lower().replace(" ", "_") + '.json', 'w') as f:
        json.dump(missingVerbs, f, indent=2)

print("(1) First group")
print("(2) Second group")
print("(3) Third group")

selectedGroup = int(input("Select which verb group to parse. (1-3, q to quit): "))

while selectedGroup != "q":
    if selectedGroup == 1:
        parseGroup = firstGroup
        groupName = "First group"
        break
    elif selectedGroup == 2:
        parseGroup = secondGroup
        groupName = "Second group"
        break
    elif selectedGroup == 3:
        parseGroup = thirdGroup
        groupName = "Third group"
        break
    else:
        print("That is not a valid option.")
        selectedGroup = int(input("Select which verb group to parse. (1-3, q to quit): "))

if selectedGroup != "q":
    parseConjugations(parseGroup)


