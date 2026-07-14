import csv
import os
import traceback
from datetime import datetime

import custom_module


# Task 2

def read_employees():
    employees = dict()
    rows = list()
    try:
        with open("../csv/employees.csv") as employees_file:
            csv_reader = csv.reader(employees_file)
            first_row = True
            for row in csv_reader:
                if first_row:
                    employees["fields"] = row
                    first_row = False
                else:
                    rows.append(row)
        employees["rows"] = rows
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return employees


employees = read_employees()
print(employees)


# Task 3

def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")


# Task 4

def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]


# Task 5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6

def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches


# Task 7

def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]


sort_by_last_name()
print(employees)


# Task 8

def employee_dict(row):
    result = dict()
    for field, value in zip(employees["fields"], row):
        if field == "employee_id":
            continue
        result[field] = value
    return result


print(employee_dict(employees["rows"][0]))


# Task 9

def all_employees_dict():
    result = dict()
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        result[emp_id] = employee_dict(row)
    return result


print(all_employees_dict())


# Task 10

def get_this_value():
    return os.getenv("THISVALUE")


# Task 11

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


set_that_secret("new secret value")
print(custom_module.secret)


# Task 12

def read_minutes_file(filename):
    minutes = dict()
    rows = list()
    try:
        with open(filename) as minutes_file:
            csv_reader = csv.reader(minutes_file)
            first_row = True
            for row in csv_reader:
                if first_row:
                    minutes["fields"] = row
                    first_row = False
                else:
                    rows.append(tuple(row))
        minutes["rows"] = rows
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return minutes


def read_minutes():
    minutes1 = read_minutes_file("../csv/minutes1.csv")
    minutes2 = read_minutes_file("../csv/minutes2.csv")
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)


# Task 13

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1 | set2


minutes_set = create_minutes_set()


# Task 14

def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return minutes_list


minutes_list = create_minutes_list()
print(minutes_list)



# Task 15

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))

    with open("./minutes.csv", "w", newline="") as minutes_file:
        csv_writer = csv.writer(minutes_file)
        csv_writer.writerow(minutes1["fields"])
        for row in converted_list:
            csv_writer.writerow(row)

    return converted_list


write_sorted_list()