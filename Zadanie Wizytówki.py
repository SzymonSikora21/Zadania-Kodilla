import faker
import string

faker = faker.Faker()


class BaseContact:

    def __init__(self, name: str, surname: str, phone_number: str, email: str):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email



class BusinessContact(BaseContact):

    def __init__(self,
                 name: str,
                 surname: str,
                 phone_number: str,
                 email: str,
                 work_position: str,
                 company: str,
                 work_phone_number: str
    ):
        super().__init__(name, surname, phone_number, email)
        self.work_position = work_position
        self.company = company
        self.work_phone_number = work_phone_number
