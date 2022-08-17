import cmd
import mysql.connector as mysql

db= mysql.connect(host='localhost', user='root', password='', database='college')
cmd_handler=db.cursor(buffered=True)

def adminSession():
    while 1:
        print('*'*20)
        print('Admin menu:')
        print('1. Register new Student')
        print('2. Register new Teacher')
        print('3. Delete existing Student')
        print('4. Delete existing Teacher')
        print('5. Print all users')
        print('6. logout')

        userOption = input(str('Option : '))
        if userOption=='1':
            print('*'*20)
            print('Registering new student:')
            username= input(str('Student username : '))
            password= input(str('Student password : '))
            values=(username,password)
            cmd_handler.execute("insert into users (username, password, access) values (%s, %s,'student')", values)
            db.commit()
            print(username+' has been registered successfully as a student')

        elif userOption=='2':
            print('*'*20)
            print('Registering new Teacher:')
            username= input(str('Teacher username : '))
            password= input(str('Teacher password : '))
            values=(username,password)
            cmd_handler.execute("insert into users (username, password, access) values (%s, %s,'teacher')", values)
            db.commit()
            print(username+' has been registered successfully as a Teacher')

        elif userOption=='3':
            print('*'*20)
            print('Deleting existing student:')
            username= input(str('Enter Student username : '))
            values=(username, 'student')
            cmd_handler.execute("delete from users where username= %s and access= %s", values)
            db.commit()
            if cmd_handler.rowcount <1:
                print('user not found')
            else:
                print(username+' has been deleted successfully!')
        
        elif userOption=='4':
            print('*'*20)
            print('Deleting existing teacher:')
            username= input(str('Enter Teacher username : '))
            values=(username, 'teacher')
            cmd_handler.execute("delete from users where username= %s and access= %s", values)
            db.commit()
            if cmd_handler.rowcount <1:
                print('user not found')
            else:
                print(username+' has been deleted successfully!')


        elif userOption=='5':
            print('*'*20)
            print('Printing all the users in the college')
            cmd_handler.execute('select * from users')
            rows=cmd_handler.fetchall()
            for row in rows:
                for col in row:
                    print(col, end=' ')
                print()

        elif userOption=='6':
            break
        else:
            print('No valid option selected')



def authenticateAdmin():
    print('*'*20)
    print('Admin login')
    print('*'*20)
    username = input(str('Enter username : '))
    password = input(str('Enter password : '))

    if username=='admin':
        if password=='password':
            adminSession()
        else:
            print('Password incorrect!')
    else:
        print('Login credentials not recognized')
def main():
    while 1:
        print('Welcome to college management system')
        print('')
        print('1. Login as Student')
        print('2. Login as Teacher')
        print('3. Login as Admin')

        userOption= input(str('Option: '))
        if userOption=='1':
            print('student login')
        elif userOption=='2':
            print('teacher login')
        elif userOption=='3':
            #print('admin login')
            authenticateAdmin()
        else:
            print('Invalid option')    


main()