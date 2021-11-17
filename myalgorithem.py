import csv
import sys
import copy
import calculator
from jsontodic import Building, Csv


def main():
    #  if you want to get the three strings from the terminal use sys.argv
    file = sys.argv[1:]
    b = Building(file[0])
    c = Csv(file[1])

    '''if you want to check specified strings use this format
    b = Building("../data/Ex1_input/Ex1_Buildings/B5.json")
    c = Csv("../data/Ex1_input/Ex1_Calls/Calls_d.csv")'''

    elev = copy.deepcopy(b.my_elevators())  # list of the the elevators
    call = copy.deepcopy(c.my_calls())  # list of the calls
    calculator.proper_algo(call, elev)

    final_call = []
    for c in call:
        final_call.append(c.__dict__.values())

    #  if you want to get the three strings from the terminal use this
    file_name = file[2]
    '''if you want to choose the name use this
    file_name = "B5-Ca.csv"'''
    with open(file_name, "w", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(final_call)


if __name__ == '__main__':
    main()
    
    
