"""
A unit test for the lexer portion of the diagrammer (the part responsible for
splitting the sentence into individual "tokens\").

"""


import lexer

l = lexer.Lexer("For in him all things were created: things in heaven and on earth, visible and invisible, whether thrones or rulers or powers or authorities; all things were created through him and for him. He is before all things, and in him all things hold together. Colossians 1:16-17")
tokens = l.lex()

print()
print(tokens)
