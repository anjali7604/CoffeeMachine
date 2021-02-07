# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

from CoffeeMachine import CoffeeMachine
import json


def main():

    # Main class reads Json File and initialize Coffee making process
    json_file_to_test = input("give json file name to process \n")
    with open(json_file_to_test, "r") as read_file:
        data = json.load(read_file)
        CoffeeMachine(data)
