def is_integer(variable):
    return isinstance(variable, int)


def is_even(number):
    even = False

    if is_integer(number) and 0 == number % 2:
        print("{} est pair !".format(number))
        even = True
    elif not is_integer(number):
        print("{} est un {} ! un nombre entier est attendu".format(number, type(number)))
    else:
        is_odd(number)

    return even


def is_odd(number):
    odd = False

    if is_integer(number) and 1 == number % 2:
        print("{} est impair !".format(number))
        odd = True

    return odd


def is_even_recursively(number):
    if 0 == number:
        print("{} est pair !".format(number))
    elif 0 == number % 2:
        print("{} est pair !".format(number))
        is_odd_recursively(number - 1)
    else:
        is_odd_recursively(number)


def is_odd_recursively(number):
    if 1 == number % 2:
        print("{} est impair !".format(number))
        is_even_recursively(number - 1)
    else:
        is_even_recursively(number)


if __name__ == '__main__':
    is_even(1)
    is_even(2)
    is_even(3)
    is_even("1")
    is_even(1.0)
    is_even_recursively(10)
    is_even_recursively(15)
    is_odd_recursively(10)
    is_odd_recursively(15)
