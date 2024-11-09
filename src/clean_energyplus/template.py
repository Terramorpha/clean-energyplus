"""When a user of this library runs a simulation of EnergyPlus, which sensor
readings would they like to receive and in what shape would they like them?

This module collects facilities for a user to construct "templates"; objects
with holes which are filled by the right sensor readings at each simulation
step.

"""

import typing

T = typing.TypeVar("T")


def search_replace(
    obj: typing.Any,
    SomeType: typing.Type[T],
    func: typing.Callable[[T], typing.Any],
):
    if type(obj) == dict:
        return {k: search_replace(v, SomeType, func) for k, v in obj.items()}
    elif type(obj) == list:
        return [search_replace(v, SomeType, func) for v in obj]
    elif type(obj) == tuple:
        return tuple(search_replace(v, SomeType, func) for v in obj)
    elif type(obj) == SomeType:
        return func(obj)
    else:
        return obj