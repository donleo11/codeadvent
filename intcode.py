class Intcode:

    def __init__(self, integer_list: list):
        self.integer_list: list = integer_list

    def get_instruction(self):
        return self.integer_list[0]

    def get_location(self):
        return self.integer_list[3]

    def get_first_location(self):
        return self.integer_list[1]

    def get_second_location(self):
        return self.integer_list[2]