"""#
# This is a module that manages communication with Hexy.
#"""

#To do: order moves from longest to shortest in order of operations
#allow for 3 word move names
#teach Hexy to provide a list of possible moves

#sys configuration
import sys
sys.path.append("Moves")        #include the Moves folder

#imports
import os, re, sqlite3, ast
from random import randrange

class Input(object):
    """Receive and parse input from Hexy."""
    def __init__(self, user_input):
        self.user_input = user_input
        self.split_input = self.getSplitInput()
        self.is_move, self.move_name = self.isMove()
        self.type = self.getType()

    def getSplitInput(self):
        #split input into list of lower-case strings and remove punctuation
        punctuation = "!?.,"
        return [x.strip(punctuation) for x in self.user_input.lower().split()]

    def getType(self):
        #determine the kind of input
        #either a question or a statement
        questions = ["?"]
        statements = [".", "!"]
        for word in self.user_input.split():
            for mark in questions:
                if mark in word:
                    return "question"
                    break
            for mark in statements:
                if mark in word:
                    return "statement"
                    break
        return "unknown"

    def separateInput(self):
        #separate an input string into individual queries
        pass

    def read(self):
        #return just the name of the move
        return self.move_name.title()

    def isMove(self):
        #determine if an input relates to a move
        #generate a list of moves
        moves = []
        is_move = False

        for fileName in os.listdir("Moves"):
            if os.path.splitext(fileName)[1] == '.py':
                fileName = os.path.splitext(fileName)[0]
                s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', fileName)
                moves.append(s1)
        for move in moves:
            position = -1
            for word in move.split():
                is_move = word.lower() in self.split_input
                if is_move == False:
                    move_name = None
                    break
                elif is_move == True and self.split_input.index(word.lower()) == position + 1 or word == move.split()[0]:
                    position = self.split_input.index(word.lower())
                else:
                    is_move = False
                    move_name = None
                    break
            if is_move == True:
                move_name = move
                break
        return is_move, move_name

    def inputParse(self):
        #parse user input that isn't a move
        curs = sqlite3.connect("memory.sql").cursor()
        inputs = curs.execute("""select * from inputs join outputs on 
                                 output_id = outputs.id""").fetchall()
        for line in inputs:
            inputs = ast.literal_eval(line[1])
            mood = line[4]
            action = line[5]
            responses = ast.literal_eval(line[6])
            for string in inputs:
                if string.lower() in self.user_input.lower():
                    return responses[randrange(len(responses))], action
            return "I don't understand what you mean.", 0

    def getMoves(self):
        #determine if an input relates to a move
        #generate a list of moves
        moves = []
        is_move = False

        for fileName in os.listdir("Moves"):
            if os.path.splitext(fileName)[1] == '.py':
                fileName = os.path.splitext(fileName)[0]
                s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', fileName)
                moves.append(s1)
        return moves