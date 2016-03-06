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

        self.punctuation_marks = [".", "?", "!", ":", ";", "-", "(", ")", "[", "]", "...", ";", "'", "\"", "/", ","]

        self.delimiter_chars = [" ", "\t", "\n"]

        # TODO: add numbers to this list
        self.normal_chars = list(string.ascii_letters)

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
        while i < len(self.sentence) - 1:
            char = self.sentence[i]

            add_to_tokens = True

            print("Testing char |" + char + "|")

            token = ""

            # Test if the char is a punctuation mark
            if char in self.punctuation_marks:
                print("Found punctuation mark")
                if char == '.':
                    # There are at least two more characters left to make up
                    # the rest of the possible ellipse ("...")
                    if i < len(self.sentence) - 3:
                        if i + 1 == '.' and i + 2 == '.':
                            token = "..."
                    else:
                        token = char
                else:
                    token = char

                    # We need to move the counter to the first character of the next token
                    i += 1

            # Test if the char is a token delimiter (a character that ends a token, such as whitespace)
            elif char in self.delimiter_chars:
                print("Found delimiter")
                add_to_tokens = False
                while char in self.delimiter_chars:
                    if i < len(self.sentence) - 1:
                        i += 1
                        char = self.sentence[i]
                    else:
                        break

            elif char in self.normal_chars:
                print("Found normal character")
                while char in self.normal_chars:
                    token += char

                    if i < len(self.sentence) - 1:
                        i += 1
                        char = self.sentence[i]
                    else:
                        break

            if add_to_tokens:
                if token != '':
                    tokens.append(token)
                else:
                    print("Error: cannot understand character " + char)
                    sys.exit(0)

            if i >= len(self.sentence) - 1:
                break

            print(tokens)

        return tokens