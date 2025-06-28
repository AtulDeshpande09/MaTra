from rules import tokenize , to_mr

def translate():

    print("English → Marathi (Rule-based FST Translator)")

    sentence1 = "She eats apple."
    tok1 = tokenize(sentence1)
    mr_1 = to_mr(tok1)
    print(sentence1)
    print(mr_1)

    sentence2 = "He drinks water."
    tok2 = tokenize(sentence2)
    mr_2 = to_mr(tok2)
    print(sentence2)
    print(mr_2)



if __name__ == '__main__':

    translate()
