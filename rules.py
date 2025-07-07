from lexicon import lexicon
from morph import inflect_verb
import spacy

nlp = spacy.load("en_core_web_sm")

def detect_tense_spacy(doc):
    for token in doc:
        if token.pos_ == "VERB":
            if token.tag_ in ["VBD", "VBN"]:
                return "past"  # Past
            elif token.tag_ in ["VBZ", "VBP", "VB"]:
                return "present"  # Present
            elif token.tag_ == "MD":
                return "future"  # Future
    return 0  # Default to present

def analyze_sentence(sentence:list):
    """
    Input : sentence (str)
    Return :
    dict containing - tense , subj , obj , verb .
    """
    sentence = sentence.lower()
    doc = nlp(sentence)
    tense = detect_tense_spacy(doc)
    for token in doc:
        if token.dep_ == "nsubj":
            subj = token.text
        elif token.dep_ == "dobj":
            obj = token.text
        elif token.pos_ == "VERB":
            verb = token.lemma_
    return { "tense" : tense , "subj" : subj , "verb" : verb , "obj" : obj }


def to_mr(sentence):

    sent_dict = analyze_sentence(sentence)

    sub_en = sent_dict["subj"]
    obj_en = sent_dict["obj"]
    verb_en = sent_dict["verb"]
    tense = sent_dict["tense"]
    
    sub = lexicon.get(sub_en)
    verb = lexicon.get(verb_en)
    obj = lexicon.get(obj_en)

    sub_mr = sub["mr"]
    plural = sub["number"]
    person = sub["person"]
    
    gender = sub['gender']
    
    obj_mr = obj['mr']
    verb_rt = verb['root']
    verb_mr = inflect_verb(verb_rt , person , plural, gender , tense)

    return f"{sub_mr} {obj_mr} {verb_mr}"
