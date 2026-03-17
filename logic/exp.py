from logic import Symbol, NOT, OR, AND, IMPLIES, model_check



Sclaret = Symbol("Sclaret")
Port = Symbol("Port")
Sherry = Symbol("Sherry")

kithchen = Symbol("kithchen")
living_room = Symbol("living_room")
liabary = Symbol("liabary")

knife = Symbol("knife")
gun = Symbol("gun")
wrench = Symbol("wrench")


KB = AND(
    OR(Sclaret, Port, Sherry),
    OR(kithchen, living_room, liabary),
    OR(knife, gun, wrench),) 

symbols_1 = [Sclaret, Port, Sherry, kithchen, living_room, liabary, knife, gun, wrench]
def check_knowledge(symbols):
    for symbol in symbols: 
        if model_check(KB, symbol, symbols):
            print(f"\033[92m{symbol} True\033[0m")
        elif model_check(KB, NOT(symbol), symbols):
            pass
        else:
            print(f"{symbol} maybe")
    

KB.add(NOT(Port))
KB.add(NOT(kithchen))
KB.add(NOT(gun))
KB.add(OR(NOT(Sclaret), NOT(liabary),NOT(wrench)))
KB.add(NOT(living_room))
KB.add(NOT(Sherry))
check_knowledge(symbols_1)