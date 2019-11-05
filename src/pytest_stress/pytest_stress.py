# -*- coding: utf-8 -*-
import shutil
import time

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
SHORTEST_AMOUNT_OF_TIME = 0


class InvalidTimeParameterError(Exception):
    pass


def _get_delay_time(session):
    """
    Helper function to extract the delay time from the session.

    :param session: Pytest session object.
    :return: Returns the delay time for each test loop.
    """
    return session.config.option.delay


def _get_total_time(session):
    """
    Takes all the user available time options, adds them and returns it in seconds.

    :param session: Pytest session object.
    :return: Returns total amount of time in seconds.
    """
    hours_in_seconds = session.config.option.hours * SECONDS_IN_HOUR
    minutes_in_seconds = session.config.option.minutes * SECONDS_IN_MINUTE
    seconds = session.config.option.seconds
    total_time = hours_in_seconds + minutes_in_seconds + seconds
    if total_time < SHORTEST_AMOUNT_OF_TIME:
        raise InvalidTimeParameterError("Total time cannot be less than: {}!".format(SHORTEST_AMOUNT_OF_TIME))
    return total_time


def _print_loop_count(count):
    """
    Helper function to simply print out what loop number we're on.

    :param count: The number to print.
    :return: None.
    """
    column_length = shutil.get_terminal_size().columns
    print("\n")
    print(" Loop # {} ".format(count).center(column_length, "="))


def _timed_out(session, start_time):
    """
    Helper function to check if the user specified amount of time has lapsed.

    :param session: Pytest session object.
    :return: Returns True if the timeout has expired, False otherwise.
    """
    return time.time() - start_time > _get_total_time(session)


def pytest_addoption(parser):
    """
    Add our command line options.
    """
    stress = parser.getgroup("stress")
    stress.addoption(
        "--delay",
        action="store",
        default=0,
        help="The amount of time to wait between each test loop.",
        type=int,
    )
    stress.addoption(
        "--hours",
        action="store",
        default=0,
        help="The number of hours to loop the tests for.",
        type=int,
    )
    stress.addoption(
        "--minutes",
        action="store",
        default=0,
        help="The number of minutes to loop the tests for.",
        type=int,
    )
    stress.addoption(
        "--seconds",
        action="store",
        default=0,
        help="The number of seconds to loop the tests for.",
        type=int,
    )


def pytest_runtestloop(session):
    """
    Reimplement the test loop but loop for the user defined amount of time.

    Note: Check against pytest repo for any updates so we don't fall behind.
    """
    if session.testsfailed and not session.config.option.continue_on_collection_errors:
        raise session.Interrupted("%d errors during collection" % session.testsfailed)

    if session.config.option.collectonly:
        return True

    start_time = time.time()
    count = 1

    while True:
        if _get_total_time(session):
            _print_loop_count(count)
        for index, item in enumerate(session.items):
            next_item = session.items[index + 1] if index + 1 < len(session.items) else None
            item.config.hook.pytest_runtest_protocol(item=item, nextitem=next_item)
            if session.shouldfail:
                raise session.Failed(session.shouldfail)
            if session.shouldstop:
                raise session.Interrupted(session.shouldstop)
        count += 1
        if _timed_out(session, start_time):
            break
        time.sleep(_get_delay_time(session))
    return True
