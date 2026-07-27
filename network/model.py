import random

P_Rain = {
    'none': 0.7,
    'light': 0.2,
    'heavy': 0.1
}


P_Maintenance = {
    ('none', 'yes'): 0.4,
    ('none', 'no'): 0.6,
    ('light', 'yes'): 0.7,
    ('light', 'no'): 0.3,
    ('heavy', 'yes'): 0.9,
    ('heavy', 'no'): 0.1
}

P_Train = {
    ('none','yes','on-time'): 0.8,
    ('none','yes','delayed'): 0.2,
    ('none','no','on-time'): 0.6,
    ('none','no','delayed'): 0.4,

    ('light','yes','on-time'): 0.6,
    ('light','yes','delayed'): 0.4,
    ('light','no','on-time'): 0.4,
    ('light','no','delayed'): 0.6,

    ('heavy','yes','on-time'): 0.3,
    ('heavy','yes','delayed'): 0.7,
    ('heavy','no','on-time'): 0.1,
    ('heavy','no','delayed'): 0.9,
}


def joint_probability(rain, maintenance, train):
    return (
        P_Rain[rain] *
        P_Maintenance[(rain, maintenance)] *
        P_Train[(rain, maintenance, train)]
    )


def probability_train_delayed():
    total = 0

    for rain in P_Rain:
        for maintenance in ['yes', 'no']:
            total += joint_probability(rain, maintenance, 'on-time')
    return total




def query(variable_values, evidence):
    probs = {}

    for value in variable_values:
        total = 0

        for rain in P_Rain:
            for maintenance in ['yes', 'no']:
                for train in ['on-time', 'delayed']:


                    if evidence.get('Train') and train != evidence['Train']:
                        continue


                    if value != rain:
                        continue

                    total += joint_probability(rain, maintenance, train)

        probs[value] = total


    norm = sum(probs.values())
    for k in probs:
        probs[k] /= norm

    return probs







# sampeling inference


def random_sample():
    rain = random.choices(list(P_Rain.keys()), weights=P_Rain.values())[0]

    maintenance = random.choices(
        ['yes', 'no'],
        weights=[P_Maintenance[(rain, 'yes')], P_Maintenance[(rain, 'no')]]
    )[0]

    train = random.choices(
        ['on-time', 'delayed'],
        weights=[
            P_Train[(rain, maintenance, 'on-time')],
            P_Train[(rain, maintenance, 'delayed')]
        ]
    )[0]

    return rain, maintenance, train






def sampling_inference(evidence, N=10000):
    counts = {}

    for _ in range(N):
        P_rain, P_Maintenance, P_Train = random_sample()  

        if evidence.get('Rain') and P_rain != evidence['Rain']:
            continue

        counts[P_Train] = counts.get(P_Train, 0) + 1

    total = sum(counts.values())
    for k in counts:
        counts[k] /= total

    return counts



e = {'Rain': 'heavy',}
print(sampling_inference(e, N=10000))
    


    
#print(query(['none', 'light', 'heavy'], {'Train': 'on-time'}))
#print(probability_train_delayed())