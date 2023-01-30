#  The text below we make a generator
s = "i am generating words from text"
s = s.split()

#  For educational purposes only!
#  print(type(s), s)
#  print(s)


def string_generator(text: list):
    """
    Generator, it takes a list and giving us only a one word
    :param text: list
    :return: one word from a list
    """
    for elements in text:
        yield elements


if __name__ == '__main__':
    for element in string_generator(s):
        print(element)
