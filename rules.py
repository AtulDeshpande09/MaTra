from lexicon import lexicon
from morph import inflect_verb


def tokenize(sentence):
    sentence = sentence.strip('.?!').lower()
    return sentence.split()


def to_mr(tokens):

    sub_en , verb_en , obj_en = tokens[0] , tokens[1][:-1] , tokens[2]
    
    #print(verb_en)

    sub = lexicon.get(sub_en)
    verb = lexicon.get(verb_en)
    obj = lexicon.get(obj_en)

    sub_mr = sub["mr"]
    obj_mr = obj['mr']

    verb_rt = verb['root']
    gender = sub['gender']
    tense = verb["tense"]

    verb_mr = inflect_verb(verb_rt , gender , tense)

    return f"{sub_mr} {obj_mr} {verb_mr}"

