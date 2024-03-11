import re

# Superclass for Contacts
class Contact:
    contact_list = []

    def __init__(self, first_name, last_name):
        self.name_first = first_name
        self.name_last = last_name

    def get_name_first(self):
        return self.name_first

    def set_name_first(self, value):
        self.name_first = value

    def get_name_last(self):
        return self.name_last

    def set_name_last(self, value):
        self.name_last = value

# Subclass for Emails
class ContactEmail(Contact):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.email = None

    def validate(self, email):
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return bool(pattern.match(email))

    def set_info(self, value):
        if self.validate(value):
            self.email = value
            self.contact_list.append(self)
        else:
            raise ValueError("Invalid email format")

    def get_info(self):
        return self.email

# Subclass for Phone Numbers
class ContactPhone(Contact):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.phone = None

    def validate(self, phone):
        pattern = re.compile(r'^[2-9]\d{2}-\d{3}-\d{4}$')
        return bool(pattern.match(phone))

    def set_info(self, value):
        if self.validate(value):
            self.phone = value
            self.contact_list.append(self)
        else:
            raise ValueError("Invalid phone number format")

    def get_info(self):
        return self.phone
