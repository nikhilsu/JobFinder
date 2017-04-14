from texttable import Texttable
import re


class InputOutput(object):
    @staticmethod
    def input(prompt=''):
        return raw_input(prompt)

    @staticmethod
    def output(string):
        print (string)

    @staticmethod
    def get_valid_password():
        return InputOutput.get_valid_input('Password (1 uppercase, 1 lowercase, 1 number, 1 special character, '
                                           'min length - 8) : ', r'[A-Za-z0-9@#$!%^&+=]{8,}')

    @staticmethod
    def get_valid_phone_number():
        return InputOutput.get_valid_input('Phone Number : ', r'[0-9]{8,}')

    @staticmethod
    def get_valid_input(prompt, regex_matcher):
        user_input = InputOutput.input(prompt)
        while True:
            if re.match(regex_matcher, user_input):
                return user_input
            else:
                user_input = InputOutput.input('Invalid input, re-enter : ')


class JobOutput(object):
    @staticmethod
    def tabular_display(jobs):
        table = Texttable()
        table.header(['SlNo', 'Job Description', 'Job Location', 'Web Link'])
        table.set_cols_width([8, 50, 50, 60])
        table.set_cols_align(['c', 'l', 'l', 'l'])
        for index, job in enumerate(jobs):
            table.add_row([index] + job.to_string_array())

        InputOutput.output(table.draw())


class Color(object):
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
