from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError


class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier) -> None:
        self.__notifier = notifier

    def notify(self) -> None:
        self.__notifier.notify()


class WhatsappNotifier(Notifier):
    def notify(self) -> None:
        print("Notifying through Whatsapp")


class SMSNotifier(Notifier):
    def notify(self) -> None:
        print("Notifying through SMS")


class EmailNotifier(Notifier):
    def notify(self) -> None:
        print("Notifying through Email")


class WhatsappNotifierDecorator(NotifierDecorator):
    def __init__(self, notifier: Notifier) -> None:
        super().__init__(notifier)
        self.__notifier = WhatsappNotifier()

    def notify(self) -> None:
        self.__notifier.notify()
        super().notify()


class SMSNotifierDecorator(NotifierDecorator):
    def __init__(self, notifier: Notifier) -> None:
        super().__init__(notifier)
        self.__notifier = SMSNotifier()

    def notify(self) -> None:
        self.__notifier.notify()
        super().notify()


class EmailNotifierDecorator(NotifierDecorator):
    def __init__(self, notifier: Notifier) -> None:
        super().__init__(notifier)
        self.__notifier = EmailNotifier()

    def notify(self) -> None:
        self.__notifier.notify()
        super().notify()


if __name__ == "__main__":
    wn = WhatsappNotifier()
    en = EmailNotifierDecorator(wn)
    sn = SMSNotifierDecorator(en)

    wn.notify()
    print()
    en.notify()
    print()
    sn.notify()
