
def inflect_verb(root , gender , tense ):

    if tense == "present":
        if gender == 'F':
            return root[:-2]+"ते"
        elif gender == 'M' :
            return root[:-2]+"तो"

    return root

