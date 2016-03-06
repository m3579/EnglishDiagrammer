"""Contains the Lexer class, a tool that splits English text into individual "tokens\""""
import sys
import string

class Lexer:
    """

    A class that splits English text into tokens. A token is a single
    unit of a sentence, like a word or a punctuation mark. Whitespace
    separates tokens.

    """

    def __init__(self, sentence):
        """Initializes a Lexer object with the given sentence"""

        self.sentence = sentence

        print(len(self.sentence))

        self.punctuation_marks = [".", "?", "!", ":", ";", "-", "(", ")", "[", "]", "...", ";", "'", "\"", "/", ","]

        self.delimiter_chars = [" ", "\t", "\n"]

        # TODO: add numbers to this list
        self.normal_chars = list(string.ascii_letters) + [str(i) for i in range(0, 10)]

        
    def lex(self):
        """Convert the sentence that this Lexer is configured it into a list of tokens, """

        tokens = []

        # Iterate over each character in the sentence and "collect" them
        # into tokens.

        # Each "test" in the lexer (for punctuation marks, delimiters, etc.) will move
        # the counter to the first character of the next token.

        # I use a while condition...counter++ instead of a for loop here
        # because I need to increment the counter within the loop itself,
        # which (as far as I have tried) does not work in a for loop
        i = 0
        while i <= len(self.sentence) - 1:
            char = self.sentence[i]

            add_to_tokens = True

            print("Testing char |" + char + "|")

            token = ""

            # Test if the char is a punctuation mark
            if char in self.punctuation_marks:
                print("Found punctuation mark")
                if char == '.':
                    # If there are at least two more characters (leaving room for an ellipse ["..."])
                    # and if those next two characters are both periods, then it is an ellipse

                    # Because the short-circuit "and" operator will exit the if statement if the first
                    # condition is false, we can be sure that by the time it reaches self.sentence[i + x],
                    # self.sentence will be long enough for it not to throw an index error
                    if i < len(self.sentence) - 3 \
                            and (self.sentence[i + 1] == '.' and self.sentence[i + 2] == '.'):
                        print("It's an ellipse!")
                        token = "..."

                        # We need to move the counter to the first character of the next token
                        i += 2
                    else:
                        print("It's just a period")
                        token = char

                        # We need to move the counter to the first character of the next token
                        i += 1
                else:
                    print("It's not a period")
                    token = char

                    # We need to move the counter to the first character of the next token
                    i += 1

            # Test if the char is a token delimiter (a character that ends a token, such as whitespace)
            elif char in self.delimiter_chars:
                print("Found delimiter")
                add_to_tokens = False
                while char in self.delimiter_chars:

                    i += 1
                    if i <= len(self.sentence) - 1:
                        char = self.sentence[i]
                    else:
                        break

            # Test if the char is a normal letter or number
            elif char in self.normal_chars:
                print("Found normal character")
                while char in self.normal_chars:
                    token += char
                    print("Token is " + token)
                    i += 1
                    if i <= len(self.sentence) - 1:
                        char = self.sentence[i]
                    else:
                        break

            if add_to_tokens:
                if token != '':
                    tokens.append(token)
                else:
                    print("Error: cannot understand character " + char)
                    sys.exit(0)

            print(tokens)
            print(i)

        return tokens