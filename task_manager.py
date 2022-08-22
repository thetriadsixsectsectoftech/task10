'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
'''This is the section where you will import libraries'''

#while loop variable
login = True



import datetime as DT

#====Login Section=====#

'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
# empty dictionary to store usernames and
usename = {} 

# the following file sequence complets the login section

with open("user.txt","r+",encoding="utf-8") as user_log:
    for line in user_log:
        sline = line.replace("\n", "").split(", ")
        usename.update({sline[0] : sline[1]})



# if entries are wrong the user will be in this loop until they right 
while login:


    user_login = input(" Please enter your username: ")
    user_password = input("Entern a password:  ")


    if user_login in usename.keys() and user_password == usename[user_login]:
        login = False




# while not user_login in useName:
#     print("invalid user")
    
#     user_login = input(" Please enter your username:  ")
            


# while not user_password in passwords:
#     print("invalid user")

#     user_password = input("Entern a password:  ")

#             # full_login = user_login.split(",")
            
#             if user_login[0] == sline[0]:
#                 print("username is okay")
            
                        
#             elif user_login[0] != sline[0]:
                
#                 break
            
#             user_pass = input(" Please enter your password:  ")

#             if user_pass[0] == sline[0]:
#                 print("password is okay")
            
            
#             if full_login[1] == sline[1]:
#                 print("password okay u man now proceed")
            
#             elif full_login[1] != sline[1]:
#                break
#            
while True:
    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()


    if menu == 'r':

        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        
        Admin_username = str(input("please enter your admin username to register a new user?"))
        
        if Admin_username == "admin":
            print("you may now register a new user.")

            username = str(input("please enter new username for the user?: "))
            password = str(input("please enter a password for the user?: "))
            
            confirmation_password = password

            please_confirm = str(input("Please re-enter the password to confirm.: "))
            
            if please_confirm == confirmation_password:
                print("password saved succesfully")

                with open("user.txt","r+",encoding="utf-8") as user_log:
                    #this line moves the cursor of readlines() to the start of the file
                    user_log.seek(0) 
                   

                    # this line reads the data
                   
                    data = user_log.readlines() 

                     #if the file contains data
                    if len(data) > 0: 
                       
                        # add a new line
                        user_log.write("\n") 
                    # write output to file    
                    user_log.write(f"{username}, {confirmation_password}" )
            else:
                print("the passwords you have entered dont match")
        
        else:
            print("looks like your not a admin...you cant regsiter a new user ")

    elif menu == 'a':   
        
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

        assigned_task = str(input("please enter the username of the peroson assigned to the task: "))
        task_title = str(input("please enter the name of the task: "))
        task_description = str(input("please enter the description of the task: "))
        task_due_date = str(input("please enter the due-date of the task|| DD//MM//YYYY: "))
        

        assignment_date = DT.datetime.now()
        
        day = assignment_date.strftime("%d")
        Month = assignment_date.strftime("%b")
        year = assignment_date.year
        
         #live date uses the date time modula to get the current date 
        live_date =(f"{day} {Month} {year}")


        task_complete = 'no' #|| task_due_date = No

        with open("tasks.txt","r+",encoding="utf-8") as task_log:
          
            task_log.seek(0)
                
            data = task_log.readlines()
            

            if len(data) > 0:
                task_log.write("\n")
            
            task_log.write(f"{assigned_task},{task_title},{task_description},{live_date},{task_due_date},{task_complete}")
    
    elif menu == 'va':
       
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
        with open("tasks.txt","r",encoding="utf-8") as tfile:
            for line in tfile.readlines():
                sline = line.split(",")
                
                print(F"TASK: {sline[1]}")

                print(f"Assigned to: {sline[0]}")

                print(f"Date assigned: {sline[3]}")

                print(f"Due date: {sline[4]}")

                print(f"Task Complete: {sline[5]}")

                print(f"Task Description:\n{sline[2]}")
                    

    
    
    elif menu == 'vm':
      
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
        
        # user_login = str(input("please enter your user name?: "))
        with open("tasks.txt","r",encoding="utf-8") as tfile:
            for line in tfile.readlines():
                sline = line.split(",")
                
                if user_login == sline[0]:
                    # with open("tasks.txt","r",encoding="utf-8") as tfile:
                    #     for line in tfile.readlines():
                    #         sline = line.split(",")    

                    print(F"TASK: {sline[1]}")

                    print(f"Assigned to: {sline[0]}")

                    print(f"Date assigned: {sline[3]}")

                    print(f"Due date: {sline[4]}")

                    print(f"Task Complete: {sline[5]}")

                    print(f"Task Description:\n{sline[2]}")








                
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")