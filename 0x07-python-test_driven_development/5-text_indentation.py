#!/usr/bin/python3
"""text_indentation function"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after each of these characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
         s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s == "" else s + "\n\n" + i + d

    print(s[:-3], end="")
