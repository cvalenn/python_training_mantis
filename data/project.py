from model.project import Project
import random
import string


constant = [
    Project(name="name1"),
    Project(name="name2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Project(name=random_string("name", 7))
    for i in range(3)]