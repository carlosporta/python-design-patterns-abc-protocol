from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, content: str, status: str) -> None:
        self.content = content
        self.status = status

    @abstractmethod
    def publish(self):
        raise NotImplementedError


class Published(State):
    def __init__(self, content) -> None:
        super().__init__(content, "published")

    def publish(self):
        return self


class Moderation(State):
    def __init__(self, content) -> None:
        super().__init__(content, "moderation")

    def publish(self):
        # simulate a moderation
        self.content = self.content.replace("ERROR", "FIXED")
        return Published(self.content)
    

class Draft(State):
    def __init__(self, content) -> None:
        super().__init__(content, "draft")

    def publish(self):
        return Moderation(self.content)


class Document:
    def __init__(self, state: State) -> None:
        self.state = state

    def render(self):
        print(self.state.content)

    def publish(self):
        self.state = self.state.publish()


if __name__ == "__main__":
    doc = Document(Draft("A text ERROR"))
    print(f"Current status: {doc.state.status}")
    print("Current content")
    doc.render()
    doc.publish()
    print()
    print(f"Current status: {doc.state.status}")
    print("Current content")
    doc.render()
    doc.publish()
    print()
    print(f"Current status: {doc.state.status}")
    print("Current content")
    doc.render()
