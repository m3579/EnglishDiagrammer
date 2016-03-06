"""Contains the Diagrammer class that makes grammar diagrams of English sentences"""

import HTTPRequestManager


class Diagrammer():
    """A class that makes grammar diagrams of English sentences"""

    def diagram(self, sentence):
        """Return a string containing a grammar diagram of the sentence argument"""

        # Convert the sentence into a list of tokens (such as ["The", "cat", "ate", "food"])
        lexer = lexer.Lexer(sentence)
        tokens = lexer.lex()

        # Parse the tokens and obtain JSON (in the form of a dictionary) representing the grammar diagram
        parser = parser.Parser(sentence)
        diagram = parser.parse()

        # Format the diagram (which is currently JSON) to look like a visual diagram
        formatter = formatter.Formatter(diagram)
        formatted_diagram = formatter.format()

        # Return a string representing the final diagram
        return formatted_diagram
        
        
