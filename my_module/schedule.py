"""A collection of functions for doing my project."""


def read_file(file):
    """Reads a file containing the schedules of two people.

    Parameters
    ----------
    file: string
        String representing the file to be read.

    Returns
    -------
    schedule: list
        A list containing the schedules read from the file.
    """

    schedule = []
    with open(file) as schedule_file:

        # Read each schedule time in the file and add it to the schedule list
        for line in schedule_file:
            schedule.append(line.replace('\n', ''))

    return schedule


def get_schedules(schedule):
    """Gets the two schedules in the given list.

    Parameters
    ----------
    schedule: list
        A list containing the two schedules.

    Returns
    -------
    schedule_1: list
        The first schedule obtained.
    schedule_2: list
        The second schedule obtained.
    """

    # Get the first schedule
    schedule_1 = []
    index = 0
    for time in schedule:

        index += 1
        if time == '#':
            break

        schedule_1.append(time)

    # Get the second schedule
    schedule_2 = []
    for time in schedule[index:]:
        schedule_2.append(time)

    return schedule_1, schedule_2


def find_free_time(schedule_1, schedule_2):
    """Finds a time when the first person can have the room to themselves.

    Parameters
    ----------
    schedule_1: list
        The schedule of the first person.
    schedule_2: list
        The schedule of the second person.

    Returns
    -------
    schedule: list
        A list containing the schedules read from the file
    """

    for time_2 in schedule_2:

        is_free = False
        for time_1 in schedule_1:
            if time_2 == time_1:
                is_free = False
                break
            else:
                is_free = True

        if is_free:
            print(time_2)
