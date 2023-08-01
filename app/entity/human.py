"""Human entity file"""

from typing import TypedDict, TypeAlias

# pylint: disable= invalid-name
T_GROUP_NAME: TypeAlias = str
T_GROUP_NAMES: TypeAlias = list[T_GROUP_NAME]
# pylint: enable= invalid-name


class Human(TypedDict):
    """Human entity"""

    name: str
    group: T_GROUP_NAME
