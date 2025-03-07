#!/usr/bin/env python3
#Author SMISHRA27 / 137285227
import sys

def read_file(filename: str) -> list:

    """Opeining a file, return its contents as a list of lines. Return a message if the file is not found."""

    try:

        with open(filename, 'r') as file:

            return file.readlines()

    except FileNotFoundError:

        return ["File not found!\n"]



def main():

    if len(sys.argv) < 2:

        print("Error: no file specified.")

        return

    

    filename = sys.argv[1]

    content = read_file(filename)



    for line in content:

        print(line, end='')  # Printing  lines without extra newlines



    print(f"\nNumber of lines: {len(content)}")



if __name__ == "__main__":

    main()


