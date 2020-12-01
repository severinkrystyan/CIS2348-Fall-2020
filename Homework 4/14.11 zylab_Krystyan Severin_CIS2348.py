"""Name: Krystyan Severin
   PSID: 1916594"""


def selection_sort_descend_trace(integers):
    for number in range(len(integers)):
        # Sets first number of iteration as largest number
        largest = number
        for i in range(number+1, len(integers)):
            # Checks for number in list that is larger than the number initially set
            if integers[i] > integers[largest]:
                largest = i
        # Sets the largest number found to be first element
        integers[number], integers[largest] = integers[largest], integers[number]
        if number != len(integers)-1:
            print(*integers, '')


if __name__ == '__main__':
    numbers = input().split()
    integer_list = [int(number) for number in numbers]
    selection_sort_descend_trace(integer_list)
