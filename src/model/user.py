class User:
    def __init__(self, first_name, last_name, phone_number, email_address, password, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.password = password
        self.gender = gender

    def full_name(self):
        return self.first_name + ' ' + self.last_name
