# -*- coding: utf8 -*-
from __future__ import unicode_literals
import codecs
import random
import glob
from enum import IntEnum
import argparse


class Column(IntEnum):
    LEFT = 0,
    RIGHT = 1,
    RANDOM = 2

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return Column[s]
        except KeyError:
            raise ValueError()


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--append", help="Append mistakes to existing file?", default=False, action="store_true")
parser.add_argument("-r", "--readonly", help="Read only mode?", default=False, action="store_true")
parser.add_argument('-c', "--column", help="Show value from which column?", type=Column.from_string,
                    choices=list(Column),
                    default=Column.RANDOM)
args = parser.parse_args()

files = glob.glob("*.txt")
print("Available files:", glob.glob("*.txt"))
val = input("Choose file: ")
if val:
    files = [val]

content = []

for file in files:
    print("reading file:", file)
    f = codecs.open(file, 'r', 'utf-8')
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        tokens = line.split(u'/')
        if len(tokens) >= 2:
            key = tokens[0].strip()
            value = tokens[1].strip()
            if not key or not value:
                print("INVALID LINE:", line)
                continue
            content.append([key, value])
        else:
            print("INVALID LINE:", line)
    f.close()

print("Phrase count:", len(content))
print("\n------------------")
print("CONFIGURATION:")
print("Append wrong answers to existing file:", args.append)
print("Show column:", args.column)
print("Read only:", args.readonly)
print("------------------\n")

wrong_answers = {}
correct_answers = []

while len(content) > 0:
    column = int(args.column.value)
    if args.column == Column.RANDOM:
        column = random.randint(0, 1)

    pos = random.randint(0, len(content) - 1)
    word = content[pos][column]
    translation = content[pos][1 - column]

    try:
        if args.readonly:
            val = input(word)
            print(translation, "\n")
        else:
            print(word)
            val = input("Translation: ")
            if val.lower().strip() == translation.lower().strip():
                print("Well done!\n")
                correct_answers.append(content[pos])
            else:
                print()
                print("Correct answer: ", translation, "\n")
                wrong_answers[content[pos][0]] = content[pos][1]
        content.pop(pos)
    except:
        break

print("\n------------------")
print("STATISTICS:\n")

if not args.readonly:
    print("Correct answers:", len(correct_answers))
    print("Wrong answers:", len(wrong_answers))
print("Skipped:", len(content))
print("------------------")

read_type = "a"
if not args.append:
    read_type = "w"

f = codecs.open("wrong_answers.txt", read_type, "utf-8")
for word, translation in wrong_answers.items():
    f.write(word + " / " + translation + "\n")
f.close()
