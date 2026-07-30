import pandas as pd
import numpy as np

employee_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}
task1_data_frame = pd.DataFrame(employee_dict)
print("Task 1.1 - task1_data_frame:")
print(task1_data_frame)
print()


task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print("Task 1.2 - task1_with_salary:")
print(task1_with_salary)
print()


task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print("Task 1.3 - task1_older:")
print(task1_older)
print()

task1_older.to_csv("employees.csv", index=False)
print("Task 1.4 - employees.csv contents:")
with open("employees.csv") as f:
    print(f.read())
print()

task2_employees = pd.read_csv("employees.csv")
print("Task 2.1 - task2_employees:")
print(task2_employees)
print()

json_employees = pd.read_json("additional_employees.json")
print("Task 2.2 - json_employees:")
print(json_employees)
print()

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("Task 2.3 - more_employees:")
print(more_employees)
print()

first_three = more_employees.head(3)
print("Task 3.1 - first_three:")
print(first_three)
print()

last_two = more_employees.tail(2)
print("Task 3.2 - last_two:")
print(last_two)
print()

employee_shape = more_employees.shape
print("Task 3.3 - employee_shape:")
print(employee_shape)
print()

print("Task 3.4 - more_employees.info():")
more_employees.info()
print()

dirty_data = pd.read_csv("dirty_data.csv")
print("Task 4.1 - dirty_data:")
print(dirty_data)
print()

clean_data = dirty_data.copy()

clean_data = clean_data.drop_duplicates()
print("Task 4.2 - clean_data (duplicates removed):")
print(clean_data)
print()

clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
print("Task 4.3 - clean_data (Age converted to numeric, missing values handled):")
print(clean_data)
print()

clean_data["Salary"] = clean_data["Salary"].replace(
    ["unknown", "n/a", "N/A", "Unknown", "NA", "na", "UNKNOWN"], np.nan
)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("Task 4.4 - clean_data (Salary converted to numeric, placeholders as NaN):")
print(clean_data)
print()

clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print("Task 4.5 - clean_data (missing numeric values filled):")
print(clean_data)
print()
assert clean_data["Age"].isna().sum() == 0
assert clean_data["Salary"].isna().sum() == 0

clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"], format="mixed", errors="coerce"
)
print("Task 4.6 - clean_data (Hire Date converted to datetime):")
print(clean_data)
print()
assert clean_data["Hire Date"].isna().sum() == 0

clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print("Task 4.7 - clean_data (Name and Department cleaned):")
print(clean_data)
print()