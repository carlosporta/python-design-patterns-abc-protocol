from abc import ABC, abstractmethod
from time import sleep


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError

    @abstractmethod
    def get_duration(self) -> float:
        raise NotImplementedError


class UnzipCommand(Command):
    def execute(self):
        sleep(2)
        print("unzip finished")

    def get_duration(self) -> float:
        return 2


class InstallCommand(Command):
    def execute(self):
        sleep(3)
        print("installation finished")

    def get_duration(self) -> float:
        return 3


class FinishCommand(Command):
    def execute(self):
        sleep(2)
        print("setup finished")

    def get_duration(self) -> float:
        return 2


class ProgressBar:
    def __init__(self):
        self._commands: list[Command] = []

    def add_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            print(f"It will takes {command.get_duration()} seconds to finish")
            command.execute()


if __name__ == "__main__":
    progressbar = ProgressBar()
    progressbar.add_command(UnzipCommand())
    progressbar.add_command(InstallCommand())
    progressbar.add_command(FinishCommand())

    progressbar.execute_commands()
