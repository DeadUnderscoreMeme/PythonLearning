employee_file = open("employees.txt","r")

print(employee_file.readlines()[1])

employee_file.close()