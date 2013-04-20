"""#
# This is a module that manages communication with Hexy.
#"""

# sys configuration
import sys
sys.path.append("./Moves/")        # include the Moves folder

# imports
import os, re, sqlite3, ast, basic_moves
from random import randrange

class Input:
    """
    Receive and parse input from Hexy.
    """
    def __init__(self, user_input):
        self.user_input = user_input

    def getSplitInput(self):
        """
        str -> list of strings

        Split input into a list or lists of important words to be processed.
        Some words should be omitted because they're not important.
        Some words should function as identification that there are multiple commands
        that must be processed.
        """
        result = re.findall("[a-z]+|[0-9]+", self.user_input.lower())
        return result

    def isBasicMove(self, perform = True):
        """
        list of strings -> bool, function call

        Check to see if self.user_input is a basic move and return True if it is. Also,
        perform the move if perform = True.
        """

        test_case = self.getSplitInput()
        move_list = [re.split("([A-Z][a-z]+)", x) for x in dir(basic_moves) if not "__" in x and not "time" in x]
        move_list = [[y.lower() for y in x if not y == ""] for x in move_list]
        move_list = [x for x in move_list if x[0] in test_case]
        if len(move_list) > 0:
            for word in range(1, max(len(x) for x in move_list)):
                try:
                    move_list = [x for x in move_list if x[word] == test_case[test_case.index(x[0])+word]]
                except IndexError:
                    pass
        if len(move_list) < 1 or len(test_case) <= len(move_list):
            return False
        elif len(move_list) == 1:
            print move_list
            if perform:
                move = [move_list[0][0]] + [x.title() for x in move_list[0][1:]]
                try:
                    parameter = re.sub("[a-z]+", "", test_case[test_case.index(move_list[0][-1:][0])+1])
                except IndexError:
                    parameter = ""
                print parameter
                eval("basic_moves." + "".join(move) + "(%s)" % (parameter))
            return True