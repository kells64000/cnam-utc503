import sys


def is_integer(variable):
    return isinstance(variable, int)


def is_float(variable):
    return isinstance(variable, float)


def max_element_in_list(number_list):
    max_value = -sys.maxsize - 1

    for number in number_list:
        if is_integer(number) or is_float(number):
            if number > max_value:
                max_value = number
        else:
            raise TypeError("La liste {} ne contient pas que des nombres".format(number_list))

    return max_value


def min_element_in_list(number_list):
    min_value = max_element_in_list(number_list)

    for number in number_list:
        if number < min_value:
            min_value = number

    print("La plus petit nombre de la liste {} est {}".format(number_list, min_value))
    return min_value


if __name__ == '__main__':
    try:
        min_element_in_list([5, 8, 6, 1, 3])
        min_element_in_list([2.5, 1.2, 0.4, 3.6])
        min_element_in_list(["2.5", 1.2, 0.4, 3.6])
    except TypeError as error:
        print(error)
