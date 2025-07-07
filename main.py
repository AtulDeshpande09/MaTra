from rules import to_mr

def translate():

    print("English → Marathi (Rule-based FST Translator)")

    sentence1 = "She eats apple."
    mr_1 = to_mr(sentence1)
    print(sentence1)
    print(mr_1)

    sentence2 = "He drinks water."
    mr_2 = to_mr(sentence2)
    print(sentence2)
    print(mr_2)



if __name__ == '__main__':

    translate()
