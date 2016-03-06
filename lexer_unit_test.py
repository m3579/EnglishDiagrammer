"""
A unit test for the lexer portion of the diagrammer (the part responsible for
splitting the sentence into individual "tokens\").

"""


import lexer

l = lexer.Lexer("The cat ran")
tokens = l.lex()

print(tokens)
