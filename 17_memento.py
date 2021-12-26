class Memento:
    def __init__(self, title: str, text: str) -> None:
        self.title = title
        self.text = text


class Document:
    def __init__(self, title: str) -> None:
        self.title = title
        self.text = ""
        self.mementos: list[Memento] = [Memento(self.title, self.text)]

    def append_text(self, text: str) -> None:
        self.text += text
        self.save_state()

    def save_state(self) -> None:
        self.mementos.append(Memento(self.title, self.text))

    def rollback(self) -> None:
        memento = self.mementos[-2]
        self.title = memento.title
        self.text = memento.text


if __name__ == "__main__":
    doc = Document("Resume")
    doc.append_text("Foo")
    doc.append_text("\nBar")
    doc.append_text("\nFooBar")
    doc.append_text("\nERROR")
    print(doc.text)
    print("\nRollback ERROR\n")
    doc.rollback()
    print(doc.text)
