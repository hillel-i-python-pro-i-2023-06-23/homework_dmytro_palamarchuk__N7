"""Processing the user data"""

from typing import TypeAlias

from app.data_provider import T_HUMANS

# pylint: disable= invalid-name
T_GROUPS_DATA: TypeAlias = dict[str, list[str]]
# pylint: enable= invalid-name


def organize_data(humans: T_HUMANS) -> T_GROUPS_DATA:
    """
    Organize user by space stations

    Parameters
    ----------
    humans: THumans
        list of humans to organize

    Returns
    -------
    group_list : T_GROUPS_DATA
        The human groups list
    """
    group_list = {}
    for human in humans:
        group = human["group"]
        name = human["name"]
        if group in group_list:
            group_list[group].append(name)
        else:
            group_list[group] = [name]

    return group_list


def get_formatted_output(data: T_GROUPS_DATA) -> str:
    """
    Get output string. That can be used to print in console.

    Parameters
    ----------
    data: T_GROUPS_DATA
        list of groups members

    Returns
    -------
    formatted_output : str
        The formatted output string
    """
    formatted_output = ""

    for group, humans in data.items():
        formatted_output += f"Group: {group} - {len(humans)} \n"
        formatted_output += f"Members: {', '.join(humans)}\n"
        formatted_output += "============================\n"

    return formatted_output
