class Symbol:
    def __init__(self, name):
        self.name = name

    def evaluate(self, model):
  
        return model.get(self.name, False)

    def __repr__(self):
        return self.name


class NOT:
    def __init__(self, operand):
        self.operand = operand

    def evaluate(self, model):
        return not self.operand.evaluate(model)

    def __repr__(self):
        return f"NOT({self.operand})"


class AND:
    def __init__(self, *operands):
        self.operands = list(operands)

    def add(self, operand):
        self.operands.append(operand)

    def evaluate(self, model):
        return all(op.evaluate(model) for op in self.operands)

    def __repr__(self):
        return f"AND({', '.join(map(str, self.operands))})"


class OR:
    def __init__(self, *operands):
        self.operands = list(operands)

    def evaluate(self, model):
        return any(op.evaluate(model) for op in self.operands)

    def __repr__(self):
        return f"OR({', '.join(map(str, self.operands))})"


class IMPLIES:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, model):
        return (not self.left.evaluate(model)) or self.right.evaluate(model)

    def __repr__(self):
        return f"IMPLIES({self.left}, {self.right})"


def model_check(KB, query, symbols):

    def check_all(symbols, model):
        if not symbols:
           
            if KB.evaluate(model):
                return query.evaluate(model)
            return True  
        remaining = symbols.copy()
        p = remaining.pop()

        model_true = model.copy()
        model_true[p.name] = True

        model_false = model.copy()
        model_false[p.name] = False


        return check_all(remaining, model_true) and check_all(remaining, model_false)

    return check_all(symbols, {})