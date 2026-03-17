import logic as op

Rain = op.Symbol("Rain")
Weekend = op.Symbol("Weekend")
Exam = op.Symbol("Exam")
Hagrid = op.Symbol("Hagrid")
Dumbledore = op.Symbol("Dumbledore")
Library = op.Symbol("Library")

KB = op.AND(
    op.NOT(op.AND(Hagrid, Dumbledore)),
    op.NOT(op.AND(Hagrid, Library)),
    op.NOT(op.AND(Dumbledore, Library)),
    op.IMPLIES(Rain, Dumbledore),
    op.IMPLIES(Exam, Library),
    op.IMPLIES(op.AND(Weekend, op.NOT(Exam)), Hagrid),
    op.OR(Hagrid, Dumbledore, Library)
)

symbols = [Rain, Weekend, Exam, Hagrid, Dumbledore, Library]

print("Does KB entail Hagrid?")
print(op.model_check(KB, Hagrid, symbols))
print("Does KB entail Library?")
print(op.model_check(KB, Library, symbols))