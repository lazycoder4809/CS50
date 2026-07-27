import nltk


grammar = nltk.CFG.fromstring("""
S -> NP VP

NP -> Det N
NP -> Det Adj N

VP -> V
VP -> V NP

Det -> "the" | "a"

Adj -> "big" | "small"  

N -> "dog" | "cat" | "bird"

V -> "chased" | "ran" | "saw" 
""")

parser = nltk.ChartParser(grammar)
sentence = input("Sentence: ").split()

for tree in parser.parse(sentence):
    print(tree) 