from abc import ABC, abstractmethod


class NoDriverFoundException(Exception):
    pass


class Person(ABC):
    def __init__(self, mediator: "TravelMediator", name: str) -> None:
        self.name = name
        self.mediator = mediator
        self.status = "Free"


class Driver(Person):
    def __init__(self, mediator: "TravelMediator", name: str, location: str) -> None:
        super().__init__(mediator, name)
        self.location = location


class User(Person):
    def __init__(self, mediator: "TravelMediator", name: str) -> None:
        super().__init__(mediator, name)

    def request_travel(self, location: str) -> "Travel":
        return self.mediator.request_travel(self, location)


class Travel:
    def __init__(self, user: User, driver: Driver, destiny: str) -> None:
        self.user = user
        self.driver = driver
        self.destiny = destiny


class TravelMediator(ABC):
    def __init__(self) -> None:
        self.users: list[User] = []
        self.drivers: list[Driver] = []

    def registry_user(self, user: User) -> None:
        self.users.append(user)

    def registry_driver(self, driver: Driver) -> None:
        self.drivers.append(driver)

    @abstractmethod
    def request_travel(self, user: User, location: str) -> Travel:
        pass


class Uber(TravelMediator):
    def request_travel(self, user: User, location: str) -> Travel:
        drivers = [driver for driver in self.drivers if driver.location == location]
        if drivers:
            driver = drivers[0]
            user.status = "Traveling"
            driver.status = "Traveling"
            return Travel(user, driver, location)
        raise NoDriverFoundException()


if __name__ == "__main__":
    uber = Uber()
    driver_1 = Driver(uber, "Driver 1", "ABC")
    driver_2 = Driver(uber, "Driver 2", "XYZ")
    user = User(uber, "User 1")
    uber.registry_user(user)
    uber.registry_driver(driver_1)
    uber.registry_driver(driver_2)

    print("Current status")
    print(f"User 1: {user.status}")
    print(f"Driver 1: {driver_1.status}")
    print(f"Driver 2: {driver_2.status}")

    print()

    travel = user.request_travel("XYZ")
    print("Travel started")
    print(f"User: {travel.user.name}")
    print(f"Traveling with: {travel.driver.name}")
    print(f"Destiny: {travel.destiny}")

    print()

    print("Current status")
    print(f"User 1: {user.status}")
    print(f"Driver 1: {driver_1.status}")
    print(f"Driver 2: {driver_2.status}")
