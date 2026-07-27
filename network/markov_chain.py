import random

states = ["sunny", "rainy"]

transitions = {
    "sunny": [("sunny", 0.8), ("rainy", 0.2)],
    "rainy": [("sunny", 0.4), ("rainy", 0.6)]
}


def get_next_state(current_state):
    rand = random.random()  
    cumulative = 0

    for state, prob in transitions[current_state]:
        cumulative += prob
        if rand < cumulative:
            return state 
        
        

def simulate_with_stats(days, start="sunny"):
    current = start
    counts = {"sunny": 0, "rainy": 0}

    for _ in range(days):
        counts[current] += 1
        current = get_next_state(current)

    total = sum(counts.values())

    for state in counts:
        print(state, ":", counts[state] / total)




start_state = random.choice(states)
print("Initial state:", start_state)

simulate_with_stats(1000, start_state)