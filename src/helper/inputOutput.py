from texttable import Texttable
import re
import getpass


class InputOutput(object):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}

    @staticmethod
    def input(prompt, valid_input=None):
        if valid_input is None:
            return raw_input(prompt)
        else:
            user_input = raw_input(prompt + ' (' + '/'.join(valid_input) + ') : ')
            while True:
                if user_input in valid_input:
                    return user_input
                else:
                    user_input = raw_input('Invalid input, re-enter : ')

    @staticmethod
    def input_yes_no(question, default='yes'):
        if default is None:
            prompt = ' [y/n] '
        elif default.lower() == 'yes':
            prompt = ' [Y/n] '
        elif default.lower() == 'no':
            prompt = ' [y/N] '
        else:
            raise ValueError("invalid default answer: '%s'" % default)

        while True:
            choice = InputOutput.input(question + prompt).lower()
            if default is not None and choice == '':
                return InputOutput.valid[default]
            elif choice in InputOutput.valid:
                return InputOutput.valid[choice]
            else:
                InputOutput.output("Please respond with 'yes' or 'no'(or 'y' or 'n').")

    @staticmethod
    def output(string):
        print (string)

    @staticmethod
    def get_valid_password():
        user_input = getpass.getpass('Password (1 uppercase, 1 lowercase, 1 number, 1 special character, min length '
                                     '- 8) : ')
        while True:
            if re.match(r'(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[@#$!%^&+=])[A-Za-z\d@#$!%^&+=]{8,}', user_input):
                return user_input
            else:
                user_input = getpass.getpass('Invalid input, re-enter : ')

    @staticmethod
    def get_valid_phone_number():
        user_input = InputOutput.input('Phone Number : ')
        while True:
            if re.match(r'[0-9]{8,}', user_input):
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
