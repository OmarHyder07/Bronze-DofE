infinitive = input("Input your verb: ")
def make_3sg_form(word):
    if  word.endswith("o") or word.endswith("ch") or word.endswith("s") or word.endswith("sh") or word.endswith("x") or word.endswith("z"):
        word = word + "es"
    elif word.endswith("y"):
        word = word.replace("y", "ies")
    else:
        word = word +"s"
    print(word)

third_person = make_3sg_form(infinitive)
