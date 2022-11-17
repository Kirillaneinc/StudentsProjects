import random


def generate_loto():
    columns_names = ["B", "I", "N", "G", "O"]
    exists_in_column_numbers = []
    loto_array = {}
    numbers = []
    counter = 1

    for column in columns_names:
        for i in range(1, 6):
            while True:
                number = random.randint(counter * 15 - 14, counter * 15)
                if not (number in exists_in_column_numbers):
                    numbers.append(number)
                    exists_in_column_numbers.append(number)
                    break
        loto_array[column] = numbers
        numbers = []
        counter += 1
    return [loto_array, columns_names]


def print_loto(data_array):
    for column_name in data_array[1]:
        print(column_name, end='   ')
    print()
    for number_of_string in range(5):
        line_string = str(data_array[0]["B"][number_of_string]) + '  ' + str(data_array[0]["I"][number_of_string]) \
                      + '  ' + str(data_array[0]["N"][number_of_string]) + '  ' \
                      + str(data_array[0]["G"][number_of_string]) + '  ' + str(data_array[0]["O"][number_of_string])
        print(line_string, end=' ')
        print()


print_loto(generate_loto())
