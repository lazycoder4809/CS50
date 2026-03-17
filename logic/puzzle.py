from logic import Symbol, NOT, OR, AND, IMPLIES, model_check

people = ["Harry", "Draco", "Hermione", "Luna", "Neville"]  
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Durmstrang"]

symbols = []
for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

KB = AND()


for person in people:
    KB.add(OR(*[Symbol(f"{person}{house}") for house in houses]))


for person in people:
    for h1 in houses:
        for h2 in houses:
            if h1 != h2:
                KB.add(IMPLIES(Symbol(f"{person}{h1}"), NOT(Symbol(f"{person}{h2}"))))


for house in houses:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                KB.add(IMPLIES(Symbol(f"{p1}{house}"), NOT(Symbol(f"{p2}{house}"))))


KB.add(Symbol("HarryGryffindor"))
KB.add(OR(Symbol("DracoSlytherin"), Symbol("DracoRavenclaw")))
KB.add(Symbol("HermioneRavenclaw"))
KB.add(OR(Symbol("LunaGryffindor"), Symbol("LunaHufflepuff")))
KB.add(OR(Symbol("NevilleGryffindor"), Symbol("NevilleHufflepuff")))


for symbol in symbols:
    if model_check(KB, symbol, symbols):
        print(f"{symbol} is entailed")
