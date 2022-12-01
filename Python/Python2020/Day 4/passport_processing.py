import re


def read_data(path):
    """ Reads puzzle input """
    with open(path, 'r') as f:
        data = f.read().split('\n\n')
    return data


class ProcessPassport:
    def __init__(self, passport):
        self.required_fields = ['byr', 'iyr', 'eyr',
                                'hgt', 'hcl',
                                'ecl', 'pid']
        self.passport = passport

    def check_byr(self):
        """ Use regex to extract 4 digits after byr: then check if in range"""
        data_field = re.findall(r'byr:([0-9]{4})', self.passport)
        return True if 1920 <= int(data_field[0]) <= 2002 else False

    def check_iyr(self):
        """ Use regex to extract 4 digits after iyr: then check if in range"""
        data_field = re.findall(r'iyr:([0-9]{4})', self.passport)
        return True if 2010 <= int(data_field[0]) <= 2020 else False

    def check_eyr(self):
        """ Use regex to extract 4 digits after eyr: then check if in range"""
        data_field = re.findall(r'eyr:([0-9]{4})', self.passport)
        return True if 2020 <= int(data_field[0]) <= 2030 else False

    def check_hgt(self):
        """ Use regex to extract digits and the unit after hgt: """
        data_field = re.findall(r'hgt:([0-9]*)([cmin]{2})', self.passport)
        if len(data_field) > 0:
            if data_field[0][1] == 'cm':
                return True if 150 <= int(data_field[0][0]) <= 193 else False
            elif data_field[0][1] == 'in':
                return True if 59 <= int(data_field[0][0]) <= 76 else False
        return False

    def check_hcl(self):
        """ Use regex to extract 6 letters or digits within a-f or 0-9 after hcl:# """
        data_field = re.findall(r'hcl:#([a-f0-9]{6})', self.passport)
        if len(data_field) > 0:
            return True if len(data_field[0]) == 6 else False
        return False

    def check_ecl(self):
        """ Use regex to extract 3 letters from a-z, then check if they match any of the required colors"""
        data_field = re.findall(r'ecl:([a-z]{3})', self.passport)
        if len(data_field) > 0:
            if data_field[0] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return True
        return False

    def check_pid(self):
        """ Use regex to extract x number of digits. Check if number of extracted digits = 9 """
        data_field = re.findall(r'pid:([0-9]*)', self.passport)
        if len(data_field) > 0:
            return True if len(data_field[0]) == 9 else False
        return False

    def check_valid_fields(self):
        """ Process a passport by checking that all fields required are present"""
        valid_pass = [fields in self.passport for fields in self.required_fields]
        return all(valid_pass)  # If all elements are True, return True


    def check_valid_field_data(self):
        """ Checks that fields contains valid data """

        data_checker = [self.check_byr()]
        data_checker.append(self.check_iyr())
        data_checker.append(self.check_eyr())
        data_checker.append(self.check_hgt())
        data_checker.append(self.check_hcl())
        data_checker.append(self.check_ecl())
        data_checker.append(self.check_pid())
        return all(data_checker)


def process_passport(passports):
    """
    Processes passports for validation
    :param passports:
    :return:
    """

    valid_counter = 0
    # Loop through each passport to check
    for passport in passports:

        # Create a class for the current passport.
        passport_processer = ProcessPassport(passport)

        # Check passport for required fields (first task)
        validated_fields = passport_processer.check_valid_fields()

        # If required fields are there, check if data behind it is also meeting correct policy requirement (second task)
        if validated_fields:
            validated_data = passport_processer.check_valid_field_data()
            valid_counter += validated_fields * validated_data

    print(f"Valid passports: {valid_counter}")


if __name__ == '__main__':

    data = read_data("puzzle_input.txt")
    process_passport(data)



