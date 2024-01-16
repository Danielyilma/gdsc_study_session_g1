

def add(StudentDataBase, studnames, name, age, sex, grade):
    StudentDataBase[name] = [age, sex, grade]
    studnames.append(name)


def view(StudentDataBase, name):
    print("name: {}".format(name))
    print("age: {}".format(StudentDataBase[name][0]))
    print("sex: {}".format(StudentDataBase[name][1]))
    print("grade: {}".format(StudentDataBase[name][2]))

def list_all_stud(StudentDataBase):
    print(StudentDataBase.key())

def delete(StudentDataBase ,name):
    del(StudentDataBase[name])

def update(StudentDataBase):
    print("enter the name of the student to update: ", end="")
    name = input()
    print("enter the information with order age, sex, grade separate with space: ")
    info = input()
    result = info.split(' ')
    StudentDataBase[name] = result
    





def main():
    StudentDataBase: dict[str, list] = {}
    studnames = [] # studentDataBase.key()

    while True: 
        print("   Menu    ")
        print(" 1 to add student\n 2 to view specific student\n 3 to list all student\n 4 to delete specific student\n 5 to update\n 0 to exit\n")
        print(" Enter: ", end="")
        num = int(input())

        if num == 1:
           print("enter name: ", end="")
           name = input()
           print("enter age: ", end="")
           age = int(input())
           print("enter sex: ", end="")
           sex = input()
           print("enter grade: ", end="")
           grade = float(input())
           add(StudentDataBase, name, age, sex, grade)
        elif num == 2:
            print("enter the name: ", end="")
            name = input()
            view(StudentDataBase, name)
        elif num == 3:
            list_all_stud(studnames)
        elif num == 4:
            print("enter the name u want to delete: ", end="")
            name = input()
            delete(StudentDataBase, name)
        elif num == 5:
            update(StudentDataBase, )
        elif num == 0:
            break

       


main()
