def first(word):
    return word[0]


def acronym(words):
    acro = ''
    acro = acro.join(list(map(first, words))).upper()
    return acro

words = ['in', 'my', 'humble', 'opinion']
acro = acronym(words)
print(acro)
