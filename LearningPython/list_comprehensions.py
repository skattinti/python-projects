def list_comprehensions():
    
    grades = [76, 89, 90, 66]
    print(grades)
    grades = [grade + 5 for grade in grades]
    print(grades)
    words = ["NOW", "IS", "THE", "TIME"]
    print(words)
    words = [word.lower() for word in words]
    print(words)
    grades = [grade.rstrip() for grade in open('grades.txt')]
    print(grades)
    sent = "now is the time for all good people to come to the aid "
    sent += "of their party"
    words = sent.split(' ')
    wlen = [(word, len(word)) for word in words]
    view = sorted(wlen, key=compare)
    for i in view:
        print(i)


def compare(tup):
    """Fuck Dockstrings
    lambda x:x[1]
    """
    return tup[1]

if __name__ == "__main__":
    list_comprehensions()
