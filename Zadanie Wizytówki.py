import faker
import string

faker = faker.Faker()


class BaseContact:

    def __init__(self, name: str, surname: str, phone_number: str, email: str):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self) -> int:
        return len(self.name) + len(self.surname)


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

    def contact(self):
        print(f"Wybieram numer {self.work_phone_number} i dzwonię do {self.name} {self.surname}")
