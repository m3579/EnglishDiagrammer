"""

The entry point into the diagrammer application. The user
will type English sentences at the prompt, and it will make grammar
diagrams of them.

"""

import diagrammer

d = diagrammer.Diagrammer()

while True:
    sentence = input("Sentence: ")
    print(d.diagram(sentence))