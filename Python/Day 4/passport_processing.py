import re
import numpy

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
        """ Checks for correct birth year data """
        data_field = re.findall(r'byr:([0-9]{4})', self.passport)
        return True if 1920 <= int(data_field[0]) <= 2002 else False

    def check_iyr(self):
        data_field = re.findall(r'iyr:([0-9]{4})', self.passport)
        return True if 2010 <= int(data_field[0]) <= 2020 else False

    def check_eyr(self):
        data_field = re.findall(r'eyr:([0-9]{4})', self.passport)
        return True if 2020 <= int(data_field[0]) <= 2030 else False

    def check_hgt(self):
        """ Checks for correct height data """
        data_field = re.findall(r'hgt:([0-9]*)([cmin]{2})', self.passport)
        if len(data_field) > 0:
            if data_field[0][1] == 'cm':
                return True if 150 <= int(data_field[0][0]) <= 193 else False
            elif data_field[0][1] == 'in':
                return True if 59 <= int(data_field[0][0]) <= 76 else False
        return False

    def check_hcl(self):
        data_field = re.findall(r'hcl:#([a-f0-9]{6})', self.passport)
        if len(data_field) > 0:
            return True if len(data_field[0]) == 6 else False
        return False

    def check_ecl(self):
        data_field = re.findall(r'ecl:([a-z]{3})', self.passport)
        if len(data_field) > 0:
            valid_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if data_field[0] in valid_color:
                return True
        return False

    def check_pid(self):
        data_field = re.findall(r'pid:([0-9]{9})', self.passport)
        if len(data_field) > 0:
            return True if len(data_field[0]) == 9 else False
        return False

    def check_valid_fields(self):
        """ Process a passport by checking that all fields required are present"""
        valid_pass = [fields in self.passport for fields in self.required_fields]
        valid_pass = all(valid_pass)

        return valid_pass

    def check_valid_field_data(self):
        """ Checks that fields contains valid data """
        valid_data = []
        valid_data.append(self.check_byr())
        valid_data.append(self.check_iyr())
        valid_data.append(self.check_eyr())
        valid_data.append(self.check_hgt())
        valid_data.append(self.check_hcl())
        valid_data.append(self.check_ecl())
        valid_data.append(self.check_pid())
        return all(valid_data)


def process_passport(passports):
    """
    Processes passports
    :param passports:
    :return:
    """

    valid_counter = 0
    for passport in passports:
        passport_processer = ProcessPassport(passport)

        validated_fields = passport_processer.check_valid_fields()
        if validated_fields:
            validated_data = passport_processer.check_valid_field_data()
            valid_counter += validated_fields * validated_data

    print(f"Valid passports: {valid_counter}")


if __name__ == '__main__':

    data = read_data("puzzle_input.txt")
    process_passport(data)


    
