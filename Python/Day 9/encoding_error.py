

def read_data(path="puzzle_input.txt"):
    fin = open(path, "r")
    lines = [int(line.strip()) for line in fin.readlines() if line.strip()]
    return lines


def find_invalid_number(code, start, end):
    """
    Finds the first invalid number in eXchange-Masking Addition System (XMAS).
    :param code: list of numbers
    :param start: start of preamble idx
    :param end: end of preamble idx
    :return:
    """
    preamble = code[start:end]

    for number in code[end:]:
        is_number_valid = False

        # Sum every two number in preamble and check for invalid number
        for idx, i in enumerate(preamble):
            for j in preamble[idx + 1:]:
                if i + j == number:
                    is_number_valid = True

        # If none of summed preamble numbers was equal to number, return the number
        if not is_number_valid:
            return number

        # Extract next preamble
        preamble, start, end = increment_preamble(code, start, end)


def find_contiguous_set(code, start, end):
    """
    Finds a list of numbers within a preamble that sums up to the first invalid number.
    Then returns the sum of the minimum and maximum numbers of that list
    :param code: list of numbers
    :param start: start of preamble idx
    :param end: end of preamble idx
    :return:
    """
    # Extract the number to check in summed list
    first_invalid_number = find_invalid_number(code, start, end)

    preamble = code[start:end]
    for number in code[end:]:

        # Add up preamble numbers and check if sum equals invalid number
        for idx, i in enumerate(preamble):
            check_number = [i]
            for j in preamble[idx + 1:]:
                check_number.append(j)
                if sum(check_number) == first_invalid_number:
                    return min(check_number) + max(check_number)

        # Extract next preamble
        preamble, start, end = increment_preamble(code, start, end)


def increment_preamble(code, start, end):
    """ Extracts the next preamble """
    start += 1
    end += 1
    preamble = code[start:end]
    return preamble, start, end


def main():

    code = read_data()

    start_of_preamble, end_of_preamble = 0, 25

    # Task 1
    invalid_number = find_invalid_number(code, start_of_preamble, end_of_preamble)
    print(f"{invalid_number} is an invalid number in XMAS list")

    # Task 2
    invalid_number_sum = find_contiguous_set(code, start_of_preamble, end_of_preamble)
    print(f"The sum of the smallest and largest number in contiguous set: {invalid_number_sum}")


main()


