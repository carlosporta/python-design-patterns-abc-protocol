from sys import getsizeof
from typing import Any, Union

BIG_LIST_SIZE = 5_000


class ResourceIntensive:
    def __init__(self) -> None:
        self.big_list = tuple(range(BIG_LIST_SIZE))

    def __sizeof__(self) -> int:
        return getsizeof(self.big_list)


class ResourceSaver:
    big_list = tuple(range(BIG_LIST_SIZE))

    def __sizeof__(self) -> int:
        return getsizeof(self.big_list)


def getmbsizeof(obj: Any) -> float:
    return getsizeof(obj) / 1024 / 1024


def get_resource_usage(
    resources: Union[list[ResourceIntensive], list[ResourceSaver]]
) -> float:
    last_looped_resource = resources[0]
    sizes = [getmbsizeof(last_looped_resource)]
    for r in resources[1:]:
        if id(r.big_list) != id(last_looped_resource.big_list):
            mbsize = getmbsizeof(r)
            sizes.append(mbsize)
        last_looped_resource = r
    return round(sum(sizes), 2)


if __name__ == "__main__":
    resource_intensive_list = [ResourceIntensive() for i in range(BIG_LIST_SIZE)]
    mbsize = get_resource_usage(resource_intensive_list)
    print(f"Resource intensive: {mbsize}MB")

    resource_saver_list = [ResourceSaver() for i in range(BIG_LIST_SIZE)]
    mbsize = get_resource_usage(resource_saver_list)
    print(f"Flyweight: {mbsize}MB")
