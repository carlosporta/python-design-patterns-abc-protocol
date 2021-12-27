from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Button(Component):
    pass


class Checkbox(Component):
    pass


class WindowsButton(Button):
    def render(self) -> str:
        return "rendering a windows button"


class LinuxButton(Button):
    def render(self) -> str:
        return "rendering a linux button"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "rendering a windows checkbox"


class LinuxCheckbox(Checkbox):
    def render(self) -> str:
        return "rendering a linux checkbox"


class ComponentFactory:
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

    @staticmethod
    def create(system: str) -> "ComponentFactory":
        return WindowsFactory() if system == "windows" else LinuxFactory()


class WindowsFactory(ComponentFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class LinuxFactory(ComponentFactory):
    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()


if __name__ == "__main__":
    selected_os = input("Type a OS family (linux (fallback) or windows): ")
    fac = ComponentFactory.create(selected_os)
    button = fac.create_button()
    checkbox = fac.create_checkbox()
    print(button.render())
    print(checkbox.render())
