#!/usr/bin/env python3
import string
from sys import argv, exit
from collections import Counter

#Input check
if len(argv) != 2:
    print("Usage: substitutions.py <FILE>")
    exit(1)
#Read data, convert to lowercase to make life easier
with open(argv[1],'r') as f:
    data = f.read().strip().lower()

#For frequency analysis, remove anything that's not lowercase ascii
to_count = filter(lambda c: c in string.ascii_lowercase, data)
counts = Counter(to_count)
#Sort letters by descending count
ordered_letters = sorted(counts, key = lambda c: counts[c], reverse = True)
#English letters by frequency
english_ordered = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
#Pair up each letter to it's substitution
substitutions = {ordered_letters[i]:english_ordered[i] for i in range(len(ordered_letters))}
#Handle letters that were not in the text
included = len(ordered_letters)
missing_letters = list(set(string.ascii_lowercase) - set(ordered_letters))
substitutions.update({missing_letters[i]:english_ordered[included+i] for i in range(26-included)})
#Interactive loop: swap pairs of letters until done
while True:
    #Information for current subsitution
    print(substitutions)
    print("".join([substitutions[c] if c in substitutions else c for c in data]))
    #Get next action
    user_in = input("Please enter 2 characters to swap, or press enter to finish.\n>>> ")
    if len(user_in) == 0:
        #Writeout and end
        break
    if len(user_in) == 2:
        #Swap two given characters
        a,b = user_in
        #Need to find where each of these is in the substitution
        a_index = list(filter(lambda c:substitutions[c]==a,string.ascii_lowercase))[0]
        b_index = list(filter(lambda c:substitutions[c]==b,string.ascii_lowercase))[0]
        substitutions[a_index] = b
        substitutions[b_index] = a
    #Repeat until user exits with empty line

#Write out to file_decoded.txt
dot_index = argv[1].rfind('.')
filename = argv[1][:dot_index] + '_decoded' + argv[1][dot_index:]
with open(filename,'w') as f:
    f.write("".join([substitutions[c] if c in substitutions else c for c in data]))
print("Saved to {}".format(filename))