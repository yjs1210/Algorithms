# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack += [(i, next)]

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1 
            # Process closing bracket, write your code here
            match = opening_brackets_stack.pop()[1]
            if (next == "}") & (match != "{"):
                return i+1
            elif (next == ")") & (match != "("):
                return i+1
            if (next == "]") & (match != "["):
                return i+1

    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0][0] + 1
    else:
        return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
