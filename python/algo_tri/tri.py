import sys


def min_element_in_list_simplified(number_list):
    min_value = sys.maxsize

    for number in number_list:
        if number < min_value:
            min_value = number

    return min_value


def selection_sort(number_list):
    sorted_list = []
    min_index = []
    print("Le tri sélection :")

    for i in range(len(number_list)):
        tmp_number_list_without_duplicate_index = [number for j, number in enumerate(number_list) if j not in min_index]
        min_value = min_element_in_list_simplified(tmp_number_list_without_duplicate_index)

        if number_list.index(min_value) in min_index:
            for k in range(len(number_list)):
                if min_value == number_list[k] and k != number_list.index(min_value):
                    min_index.append(k)
        else:
            min_index.append(number_list.index(min_value))

        sorted_list.append(min_value)
        print(sorted_list)

    return sorted_list


def insertion_sort(number_list):
    sorted_list = []
    print("Le tri insertion :")

    for number in number_list:
        if 0 == len(sorted_list):
            sorted_list.append(number)
        else:
            for i in range(len(sorted_list)):
                if number < sorted_list[i]:
                    sorted_list.insert(i, number)
                    break
                elif i == len(sorted_list) - 1:
                    sorted_list.append(number)
                    break

        print(sorted_list)

    return sorted_list


def bubble_sort(number_list):
    sorted_list = number_list.copy()
    print("Le tri bulle :")

    for i in range(len(number_list)):
        print(sorted_list)
        for j in range(len(sorted_list) - 1):
            if sorted_list[j] > sorted_list[j+1]:
                tmp = sorted_list[j]
                sorted_list[j] = sorted_list[j+1]
                sorted_list[j+1] = tmp

    return sorted_list


if __name__ == '__main__':
    selection_sort([14, 5, 7, 12, 3, 4, 5])
    insertion_sort([14, 5, 7, 12, 3, 4, 5])
    bubble_sort([14, 5, 4, 12, 3, 4, 2])
