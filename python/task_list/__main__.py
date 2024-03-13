import sys

from task_list.adapter.controller import Controller
from task_list.adapter.console import Console

def main():
    Controller(Console(sys.stdin, sys.stdout)).run()

if __name__ == "__main__":
    main()

