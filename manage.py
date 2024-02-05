#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():


    print("hello")

    my_str = 'String to chec'
    rev_str = my_str[::-1]

    if my_str == rev_str:
        print("It is palindrome")
    else:
        print("It is not palindrome")

    # """Run administrative tasks."""
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asklobORM.settings')
    # try:
    #     from django.core.management import execute_from_command_line
    # except ImportError as exc:
    #     raise ImportError(
    #         "Couldn't import Django. Are you sure it's installed and "
    #         "available on your PYTHONPATH environment variable? Did you "
    #         "forget to activate a virtual environment?"
    #     ) from exc
    # execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
