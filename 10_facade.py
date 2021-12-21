from abc import ABC, abstractmethod


class IHardwareInfo(ABC):
    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError


class CPUInfo(IHardwareInfo):
    def display(self) -> None:
        print("CPU usage: 10%")


class DiskInfo(IHardwareInfo):
    def display(self) -> None:
        print("Disk usage: 45%")


class MemoryInfo(IHardwareInfo):
    def display(self) -> None:
        print("Memory usage: 37%")


class HardwareInfo(IHardwareInfo):
    def __init__(self) -> None:
        self.cpu_info = CPUInfo()
        self.disk_info = DiskInfo()
        self.memory_info = MemoryInfo()

    def display(self) -> None:
        self.cpu_info.display()
        self.disk_info.display()
        self.memory_info.display()


if __name__ == "__main__":
    hwinfo = HardwareInfo()
    hwinfo.display()
