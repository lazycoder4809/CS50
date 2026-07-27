import random

# this is hidden markov model, we have hidden states and observable states, we want to predict the hidden state based on the observable state

rainny = {
    'umbrella': 0.8,
    'no-umbrella': 0.2
}
sunny = {   
    'umbrella': 0.1,
    'no-umbrella': 0.9
}

state_predictions = {
    'umbrella': {
        'rainy': 0.8,
        'sunny': 0.2
    },
    'no-umbrella': {
        'rainy': 0.1,
        'sunny': 0.9
    }
}

def get_observation(state):
    rand = random.random()
    if state == 'rainy':
        if rand < rainny['umbrella']:
            return 'umbrella'
        else:
            return 'no-umbrella'
    else:
        if rand < sunny['umbrella']:
            return 'umbrella'
        else:
            return 'no-umbrella'
        
def predict_state(observation):
    for i in state_predictions[observation]:
        rand = random.random()
        if rand < state_predictions[observation][i]:
            print("Predicted state:", i)
            return i


state = random.choice(['sunny', 'rainy'])
print("State:", state)
print(get_observation(state))
predict_state(get_observation(state))