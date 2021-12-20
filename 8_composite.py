# https://www.sihui.io/design-pattern-composite/#:~:text=A%20Real%20Life%20Example%3A%20Group%20Messaging&text=1.-,The%20Composite%20Pattern%20allows%20you%20to%20compose%20objects%20into,to%20represent%20part%2Dwhole%20hierarchies.&text=In%20this%20example%2C%20Contacts%20is,people%20or%20a%20single%20person.

from abc import ABC, abstractmethod
from typing import Iterable


class Contact(ABC):
    @abstractmethod
    def send_message(self, text: str) -> None:
        raise NotImplementedError


class PersonContact(Contact):
    def __init__(self, name: str, number: str) -> None:
        self.name = name
        self.number = number

    def send_message(self, text: str) -> None:
        print("Message sent")
        print(f"Contact: {self.name} - {self.number}")
        print(f"Text: {text}")


class GroupContact(Contact):
    def __init__(self, name: str, contacts: Iterable[Contact]) -> None:
        self.name = name
        self.contacts = contacts

    def send_message(self, text: str) -> None:
        print('-' * 40)
        print(f"Group: {self.name}")
        for c in self.contacts:
            c.send_message(text)


if __name__ == "__main__":
    # family
    mom = PersonContact("Mom", "123")
    dad = PersonContact("Dad", "321")
    family = GroupContact("Family", (mom, dad))

    # work - officers
    ceo = PersonContact("CEO", "234")
    cio = PersonContact("CIO", "432")
    officers = GroupContact("Officers", (ceo, cio))

    # work - my department
    dev = PersonContact("Dev", "345")
    ui_designer = PersonContact("UI Designer", "543")
    my_department = GroupContact("My department", (dev, ui_designer))

    # work
    work = GroupContact("Work", (officers, my_department))

    # all
    all_contacts = GroupContact("All", (family, work))
    all_contacts.send_message("Hi")