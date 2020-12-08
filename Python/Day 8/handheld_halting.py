from copy import deepcopy


def read_data(path="puzzle_input.txt"):
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    return lines


class AdventGameBoy():

    def __init__(self, input_code):
        self.input_code = [[line.split(" ")[0], int(line.split(" ")[1])] for line in input_code]
        self.code_idxs = self.find_jump_codes()
        self.current_position = 0
        self.current_acceleration = 0
        self.memory = []


    def find_jump_codes(self):
        """ Find indexes of jmps and nops"""
        codes_idx = []
        for i, code in enumerate(self.input_code):
            if code[0] == 'jmp' or code[0] == 'nop':
                codes_idx.append((code[0], i))
        return codes_idx

    def brute_force_instruction_switch(self):
        """ Switch either jmp to nop or vice versa to check if code terminates naturally """
        for code_instruction, idx in self.code_idxs:
            self.reset_game()
            input_code = deepcopy(self.input_code)

            if code_instruction == 'nop':
                input_code[idx][0] = 'jmp'
            elif code_instruction == 'jmp':
                input_code[idx][0] = 'nop'

            self.run_code(input_code)

    def no_operation(self):
        self.current_position += 1

    def accelerate(self, acc_code):
        self.current_acceleration += acc_code
        self.current_position += 1

    def jump_position(self, jmp_code):
        self.current_position += jmp_code

    def check_for_termination(self):
        if self.current_position in self.memory:
            return True
        elif self.current_position > len(self.input_code) - 1:
            self.log_result()
            return True

    def run_code(self, input_code):
        """Runs through a set of input code"""

        # Run game code
        while True:

            # Check termination criteria
            if self.check_for_termination():
                break

            # Retrieve code instructions
            code_instruction, value = input_code[self.current_position][0],\
                                      input_code[self.current_position][1]

            # Add instruction to memory
            self.memory.append(self.current_position)

            # Execute operation
            if code_instruction == 'nop':
                self.no_operation()
            elif code_instruction == 'acc':
                self.accelerate(value)
            elif code_instruction == 'jmp':
                self.jump_position(value)

    def log_result(self):
        """ Prints the result of a game cycle """
        print("Code has terminated. Current acceleration: " + str(self.current_acceleration))

    def reset_game(self):
        """ Resets game parameters """
        self.current_position = 0
        self.current_acceleration = 0
        self.memory = []


def main():
    puzzle_input = read_data()
    console = AdventGameBoy(input_code=puzzle_input)

    # Part 1
    console.run_code(console.input_code)
    console.log_result()

    # Part 2
    console.brute_force_instruction_switch()



main()
