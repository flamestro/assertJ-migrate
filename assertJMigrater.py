#!/usr/bin/python3

"""assertJMigrater.py: This is an script to easily migrate JUnit Assert to AssertJ"""

__author__ = "Ahmet Kilic https://github.com/flamestro"

import fileinput
import os
import sys


def substring_maker(inputstring, start, end, index=0):
    return (inputstring.split(start))[-1].split(end)[index]


file_path = input("Please enter the absolute path to the file you want to migrate :")
file_name = file_path.rsplit("/", 1)[1]
file_dir = file_path.rsplit("/", 1)[0]
print(file_dir, file_name, file_path)
os.system("cd {}".format(file_dir))
for line in fileinput.input(file_name, inplace=True):
    start_line = line
    if not line.endswith(";"):
        if len(line.split(";")) > 1:
            line = line.split(";")[0] + ";"
        else:
            sys.stdout.write(line)
            continue
    if "assertEquals" in line and line.endswith(";"):
        parameters = substring_maker(line, "assertEquals(", ");")
        actual = parameters.split(",")[1]
        expected = parameters.split(",")[0]
        if actual.startswith(" "):
            actual = actual[1:]
        new_line = "assertThat({}).isEqualTo({});\n".format(actual, expected)
    elif "assertTrue" in line and line.endswith(";"):
        parameter = substring_maker(line, "assertTrue(", ");")
        actual = parameter
        if actual.startswith(" "):
            actual = actual[1:]
        new_line = "assertThat({}).isTrue();\n".format(actual)
    elif "assertFalse" in line and line.endswith(";"):
        parameter = substring_maker(line, "assertFalse(", ");")
        actual = parameter
        if actual.startswith(" "):
            actual = actual[1:]
        new_line = "assertThat({}).isFalse();\n".format(actual)
    elif "assertNull" in line and line.endswith(";"):
        parameter = substring_maker(line, "assertNull(", ");")
        actual = parameter
        if actual.startswith(" "):
            actual = actual[1:]
        new_line = "assertThat({}).isNull();\n".format(actual)
    elif "assertNotNull" in line and line.endswith(";"):
        parameter = substring_maker(line, "assertNotNull(", ");")
        actual = parameter
        if actual.startswith(" "):
            actual = actual[1:]
        new_line = "assertThat({}).isNotNull();\n".format(actual)
    else:
        new_line = start_line
    sys.stdout.write(new_line)
