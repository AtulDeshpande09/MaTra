import pickle

filepath = "models/verbs.pkl"

with open(filepath , "rb") as file:
    model = pickle.load(file)

encode = {
    0 : {'fp' : 0 , 'sp' : 1 , 'tp' :2 } ,
    1 : {'sg' : 0 , 'pl' : 1 } ,
    2 : {'M' : 0 , 'F' : 1 } ,
    3 : {'present' : 0 , 'past' : 1 , 'future' :2 }
}

def make_input(data:list):
    encoded_data = []
    for i , feature in enumerate(data):
        new = encode[i][feature]
        encoded_data.append(new)
    
    return [encoded_data]

def inflect_verb(verb_rt , person , plural, gender , tense ):
    data = [ person , plural, gender , tense ]
    model_input = make_input(data)
    suffix = model.predict(model_input)
    verb = verb_rt[:-2]+ suffix[0]
    return verb

