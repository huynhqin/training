import os

employees = []

def is_id_exist(emp_id):
    for employee in employees:
        if employee["ID"] == emp_id:
            return True
    return False

def create_employee():
    #os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        emp_id = input("Enter employee ID: ")
        if is_id_exist(emp_id):
            print("Employee ID already exists. Please enter a different ID.")
            continue
        name = input("Enter employee name: ")
        employee = {"ID": emp_id, "Name": name}
        employees.append(employee)
        print("Employee created successfully!")
        
        cont = input("Do you want to create another employee? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

def update_employee():
    #os.system('cls' if os.name == 'nt' else 'clear')
    emp_id = input("Enter employee ID to update: ")
    for employee in employees:
        if employee["ID"] == emp_id:
            employee["Name"] = input("Enter new name: ")
            print("Employee updated successfully!")
            return
    print("Employee not found!")

def delete_employee():
    #os.system('cls' if os.name == 'nt' else 'clear')
    emp_id = input("Enter employee ID to delete: ")
    for employee in employees:
        if employee["ID"] == emp_id:
            employees.remove(employee)
            print("Employee deleted successfully!")
            return
    print("Employee not found!")

def read_employees():
    #os.system('cls' if os.name == 'nt' else 'clear')
    if not employees:
        print("No employees found.")
    else:
        print("\nList of Employees:")
        for employee in employees:
            print(f"ID: {employee['ID']}, Name: {employee['Name']}")

def display_menu():
    print("\nEmployee Management System")
    print("1. Create Employee")
    print("2. Read Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            create_employee()
        elif choice == '2':
            read_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()