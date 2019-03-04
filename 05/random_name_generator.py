from random import choice


first_names = ["Drew", "Mike", "Landon", "Jeremy", "Tyler", "Tom", "Avery"]
last_names = ["Smith", "Jones", "Brighton", "Taylor"]


def random_name(first, last, x):
    """
    :param first: list of names
    :param last:  list of names
    :param x:   number of names
    :return: random names
    """

    names = []
    for i in range(x):
        names.append("{} {}".format(choice(first), choice(last)))
    return set(names)   # here is the highlight


if __name__ == '__main__':
    names = random_name(first_names, last_names, 5)
    print("\n".join(names))     # another highlight



