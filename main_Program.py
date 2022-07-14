import maskpass
from termcolor import *
from pyfiglet import *
import pandas as pd
import random
#Generating unique number of patient
def uniqueNumberGeneration():
    randomNumber=""
    for i in range(6):
        randomNumber+=str(random.randint(0,9))
    return randomNumber

#Generating room number for patient
def roomNumberGeneration():
    randomRoomNumber=""
    for i in range(2):
        randomRoomNumber+=str(random.randint(0,9))
    return int(randomRoomNumber)


# customizing print functions for beautiful display
f = Figlet(font='big')
print(colored(f.renderText("Hospital ManageMent System"), "green"))
print()
print_red = lambda x: cprint(x, "red")
print_green = lambda x: cprint(x, "green")
# creating dataframe for patient,doctor and appointment csv file
df_patients = pd.read_csv(r"C:\Users\VINAY SAHAL\Downloads\Patients_DataBase.csv")
df_doctors = pd.read_csv(r"C:\Users\VINAY SAHAL\Downloads\Doctors_DataBase.csv")
df_appointments=pd.read_csv(r"C:\Users\VINAY SAHAL\Downloads\appointments.csv")
tries = 0
tries_flag = ""
while tries_flag != "Close the program":
    print(colored("-----------------------------------------", "red"))
    print(colored("|", "red") + colored("Enter 1 for Admin mode		      ", "yellow") + colored("|", "red"))
    print(colored("|", "red") + colored("Enter 2 for User mode		      ", "yellow") + colored("|", "red"))
    print(colored("-----------------------------------------", "red"))
    Admin_user_mode = input("Enter your mode : ")

    if Admin_user_mode == "1":  # Admin mode
        print(
            "*****************************************\n|         Welcome to admin mode         |\n*****************************************")
        Password = maskpass.askpass(prompt="Enter password:",mask="*")
        while True:
            if Password == "1234":
                print("-----------------------------------------")
                print(
                    "|To manage patients Enter 1 		|\n|To manag2"
                    "e doctors Enter 2	 	|\n|To manage appointments Enter 3 	|\n|To be back Enter E			|")
                print("-----------------------------------------")
                AdminOptions = input("Enter your choice : ")
                AdminOptions = AdminOptions.upper()

                if AdminOptions == "1":  # Admin mode --> Patients Management
                    print("-----------------------------------------")
                    print("|To add new patient Enter 1	  	|")
                    print("|To display patient Enter 2	  	|")
                    print("|To delete patient data Enter 3		|")
                    print("|To edit patient data Enter 4    	|")
                    print("|To Back enter E      			|")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1":  # Admin mode --> Patients Management --> Enter new patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : ")) - 1
                            if patient_ID in df_patients.index:
                                print_red("ID not usable")
                            else:
                                Name = input("Enter patient name                      : ")
                                Age = input("Enter patient age                       : ")
                                Gender = input("Enter patient gender                    : ")
                                Address = input("Enter patient address                   : ")
                                df_patients.loc[len(df_patients.index)] = [patient_ID + 1,  Name, Age,
                                                               Gender, Address]
                                print_green("----------------------Patient added successfully----------------------")
                        except ValueError:
                            print_red("Patient ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Patients Management --> Display patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : ")) - 1
                            while patient_ID not in df_patients.index:
                                patient_ID = int(input("Incorrect ID, Please Enter patient ID : ")) - 1
                            print_green("\npatient name        : "+df_patients.iloc[patient_ID, 1])
                            print_green("patient age         : "+ str(df_patients.iloc[patient_ID, 2]))
                            print_green("patient gender      : "+ df_patients.iloc[patient_ID, 3])
                            print_green("patient address     : "+ df_patients.iloc[patient_ID, -1])
                            if (df_patients.iloc[patient_ID, 1]) in list(df_appointments.iloc[:,1]):
                                count=list(df_appointments.iloc[:,1]).index(df_patients.iloc[patient_ID, 1])
                                print_green("Department: "+df_appointments.iloc[count,-3])
                                print_green("Doctor Following: "+df_appointments.iloc[count,2])
                                print_green("Room Number: "+str(df_appointments.iloc[count,-2]))
                            else:
                                print("This patient is not followed by Doctor!")
                        except ValueError:
                            print_red("Patient ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Patients Management --> Delete patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : ")) - 1
                            while patient_ID not in df_patients.index:
                                patient_ID = int(input("Incorrect ID, Please Enter patient ID : ")) - 1
                            df_patients = df_patients.drop(patient_ID, axis='index')
                            print_green("----------------------Patient data deleted successfully----------------------")
                        except ValueError:
                            print_red("Patient ID should be an integer number")

                    elif Admin_choice == "4":  # Admin mode --> Patients Management --> Edit patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : ")) - 1
                            while patient_ID not in df_patients.index:
                                patient_ID = int(input("Incorrect ID, Please Enter patient ID : ")) - 1
                            while True:
                                print("------------------------------------------")
                                print("|To Edit patient Name Enter 1 :          |")
                                print("|To Edit patient Age Enter 2 :           |")
                                print("|To Edit patient Gender Enter 3 :        |")
                                print("|To Edit patient Address Enter 4 :       |")
                                print("|To be Back Enter E                      |")
                                print("-----------------------------------------")
                                Admin_choice = input("Enter your choice : ")
                                Admin_choice = Admin_choice.upper()
                                if Admin_choice == "1":
                                    newName= input("\nEnter patient name : ")
                                    df_patients.iloc[patient_ID, 1] =newName
                                    if newName in list(df_appointments.iloc[:1]):
                                        pos=list(df_appointments.iloc[:1]).index(newName)
                                        df_appointments.iloc[pos,1]=newName
                                    print_green(
                                        "----------------------Patient name edited successfully----------------------")

                                elif Admin_choice == "2":
                                    df_patients.iloc[patient_ID, 2] = input("\nEnter patient Age : ")
                                    print_green(
                                        "----------------------Patient age edited successfully----------------------")

                                elif Admin_choice == "3":
                                    df_patients.iloc[patient_ID, -2] = input("\nEnter patient gender : ")
                                    print_green(
                                        "----------------------Patient address gender successfully----------------------")

                                elif Admin_choice == "4":
                                    df_patients.iloc[patient_ID, -1] = input("\nEnter patient address : ")
                                    print_green(
                                        "----------------------Patient address edited successfully----------------------")
                                elif Admin_choice == "E":
                                    break

                                else:
                                    print_red("Please Enter a correct choice")
                        except ValueError:
                            print_red("Patient ID should be an integer number")

                    elif Admin_choice == "E":  # Admin mode --> Pateints Management --> Back
                        break

                    else:
                        print_red("Please enter a correct choice\n")

                elif AdminOptions == "2":  # Admin mode --> Doctors Management
                    print("-----------------------------------------")
                    print("|To add new doctor Enter 1              |")
                    print("|To display doctor Enter 2              |")
                    print("|To delete doctor data Enter 3          |")
                    print("|To edit doctor data Enter 4            |")
                    print("|To be back enter E                     |")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1":  # Admin mode --> Doctors Management --> Enter new doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID : ")) - 1
                            while Doctor_ID in df_doctors.index:  # if Admin entered used ID
                                Doctor_ID = int(input("This ID is unavailable, please try another ID : ")) - 1

                            Department = input("Enter Doctor department : ")
                            Name = input("Enter Doctor name       : ")
                            Address = input("Enter Doctor address    : ")
                            df2 = df_doctors.T
                            df2[Doctor_ID] = [Doctor_ID + 1, Department, Name, Address]
                            print_green("----------------------Doctor added successfully----------------------")
                        except ValueError:
                            print_red("Doctor ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Doctors Management --> Display doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID : ")) - 1
                            while Doctor_ID not in df_doctors.index:
                                Doctor_ID = int(input("Incorrect ID, Please Enter patient ID : ")) - 1
                            else:
                                print_green("\nDoctor name    : "+ df_doctors.iloc[Doctor_ID, 2])
                                print_green("Doctor address : "+ df_doctors.iloc[Doctor_ID, 3])
                                print_green("Doctor is in " + df_doctors.iloc[Doctor_ID, 1] + " department")
                        except:
                            print_red("Doctor ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Doctors Management --> Delete doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID : ")) - 1
                            while Doctor_ID not in df_doctors.index:
                                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : ")) - 1
                            df_doctors.drop(Doctor_ID, axis="index")
                            print_green(
                                "/----------------------Doctor data deleted successfully----------------------/")
                        except ValueError:
                            print_red("Doctor ID should be an integer number")

                    elif Admin_choice == "4":  # Admin mode --> Doctors Management --> Edit Doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID : ")) - 1
                            while Doctor_ID not in df_doctors.index:
                                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : ")) - 1
                            print("-----------------------------------------")
                            print("|To Edit doctor's department Enter 1    |")
                            print("|To Edit doctor's name Enter 2          |")
                            print("|To Edit doctor's address Enter 3       |")
                            print("To be Back Enter E                      |")
                            print("-----------------------------------------")
                            Admin_choice = input("Enter your choice : ")
                            Admin_choice = Admin_choice.upper()
                            if Admin_choice == "1":
                                df_doctors.iloc[Doctor_ID, 1] = input("Enter Doctor's Department : ")
                                print_green(
                                    "/----------------------Doctor's department edited successfully----------------------/")

                            elif Admin_choice == "2":
                                df_doctors.iloc[Doctor_ID, 2] = input("Enter Doctor's Name : ")
                                print_green(
                                    "----------------------Doctor's name edited successfully----------------------")

                            elif Admin_choice == "3":
                                df_doctors.iloc[Doctor_ID, -1] = input("Enter Doctor's Address : ")
                                print_green(
                                    "----------------------Doctor's address edited successfully----------------------")

                            elif Admin_choice == "E":
                                break

                            else:
                                print_red("\nPlease enter a correct choice\n")

                        except ValueError:
                            print_red("Doctor ID should be an integer number")

                    elif Admin_choice == "E":  # Back
                        break

                    else:
                        print_red("\nPlease enter a correct choice\n")

                elif AdminOptions == "3":  # Admin mode --> Appointment Management
                    print("-----------------------------------------")
                    print("|To book an appointment Enter 1         |")
                    print("|To edit an appointment Enter 2       |")
                    print("|To cancel an appointment Enter 3       |")
                    print("|To be back enter E                     |")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()
                    if Admin_choice == "1":  # Admin mode --> Appointment Management --> Book an appointment
                        try:  # To avoid non integer input
                            print("---------------------------------------------------------")
                            print(
                                "|For book an appointment for an exist patient Enter 1   |\n|For book an appointment for a new patient Enter 2      |\n|To be Back Enter E                                     |")
                            print("---------------------------------------------------------")
                            Admin_choice = input("Enter your choice : ")
                            Admin_choice = Admin_choice.upper()
                            if Admin_choice == "1":
                                patient_ID = int(input("Enter patient ID : ")) - 1
                                while patient_ID not in df_patients.index:  # if Admin entered incorrect ID
                                    patient_ID = int(input("Incorrect ID, please Enter a correct patient ID : ")) - 1
                                Department = input("Enter the department to which admission must be done: ")
                                #generating room number
                                roomNumber=roomNumberGeneration()
                                while roomNumber in list(df_appointments.iloc[:,-1]):
                                    roomNumber=roomNumberGeneration()
                                #generating unique id
                                uniqueID=uniqueNumberGeneration()
                                while uniqueID in list(df_appointments.iloc[:,0]):
                                    uniqueID=uniqueNumberGeneration()
                                #finding doctor name
                                doctorIndex=list(df_doctors.iloc[:,1]).index(Department)
                                df_appointments.loc[len(df_appointments.index)]=[uniqueID,df_patients.iloc[patient_ID,1],df_doctors.iloc[doctorIndex,-2],Department,roomNumber,random.choice(['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])]
                                print_green("Appointment done successfully")
                            elif Admin_choice == "2":
                                patient_ID = int(input("Enter patient ID : ")) - 1
                                while patient_ID in df_patients.index:  # if Admin entered used ID
                                    patient_ID = int(input("This ID is unavailable, please try another ID : ")) - 1
                                patient_appnt = input("Which department you want to take admission on?")
                                if patient_appnt not in list(df_doctors.iloc[:, 1]):
                                    print_red("This department not available,please try again")
                                else:
                                    Name = input("Enter patient name    : ")
                                    Age = input("Enter patient age     : ")
                                    Gender = input("Enter patient gender  : ")
                                    Address = input("Enter patient address : ")
                                    RoomNumber = ""
                                    df_patients.loc[patient_ID] = [patient_ID+1, Name, Age,
                                                                   Gender, Address,
                                                                   ]
                                #generating room number
                                roomNumber=roomNumberGeneration()
                                while roomNumber in list(df_appointments.iloc[:,-1]):
                                    roomNumber=roomNumberGeneration()
                                #generating unique id
                                uniqueID=uniqueNumberGeneration()
                                while uniqueID in list(df_appointments.iloc[:,0]):
                                    uniqueID=uniqueNumberGeneration()
                                #finding doctor name
                                doctorIndex=list(df_doctors.iloc[:,1]).index(patient_appnt)
                                df_appointments.loc[len(df_appointments.index)]=[uniqueID,df_patients.iloc[patient_ID,1],df_doctors.iloc[doctorIndex,-2],patient_appnt,roomNumber,random.choice(['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])]
                                print_green("appointment created successfully!")
                            elif Admin_choice == "E":
                                break
                            else:
                                print_red("Please enter correct choice\n")
                        except ValueError:
                            print_red("Doctor ID should be an integer number")
                    elif Admin_choice == "2":  # Admin mode --> Appointment Management --> Edit an appointment
                        try:  # To avoid non integer input
                            patientUniqueID=int(input("Enter patient Unique Number: "))
                            if patientUniqueID in list(df_appointments.iloc[:,0]):
                                positionUniqueID=list(df_appointments.iloc[:,0]).index(patientUniqueID)
                                print("---------------------------------------")
                                print("|To edit patient name Enter 1         |")
                                print("|To edit department Enter 2           |")
                                print("|To edit room number Enter 3          |")
                                print("|To be back enter E                   |")
                                print("---------------------------------------")
                                adminOption=int(input("Enter your choice:"))
                                if adminOption==1:#update both appointment and patient database
                                    newName=input("Enter new name:")
                                    df_appointments.iloc[positionUniqueID,1]=newName
                                    if newName not in list(df_patients.iloc[:1]):
                                        print("Patient Not added,Add first")                        
                                    print_green("Name Updated Successfully!!")
                                elif adminOption==2:#updating both department and doctor name
                                    newDept=input("Enter department:")
                                    df_appointments.iloc[positionUniqueID,-3]=newDept
                                    newDoc=list(df_doctors.iloc[:,1]).index(newDept)
                                    df_appointments.iloc[positionUniqueID,2]=newDoc
                                    print_green("Department Updated Successfully!!")
                                elif adminOption==3:
                                    #generating room number
                                    roomNumber=roomNumberGeneration()
                                    while roomNumber in list(df_appointments.iloc[:,-1]) and roomNumber==df_appointments.iloc[positionUniqueID,-2]:
                                        roomNumber=roomNumberGeneration()
                                    df_appointments.iloc[positionUniqueID,-2]=roomNumber
                                    print_green("Room Number updated successfully")
                                elif adminOption=='E':
                                    break
                                else:
                                    print_red("Please Enter correct choice\n")
                            else:
                                print("Unique ID doesn't exist!")
                        except ValueError:
                            print("Not an Integer input!")
                    elif Admin_choice == "3":  # Admin mode --> Appointment Management --> Delete an appointment
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : ")) - 1
                            while patient_ID not in df_patients.index:
                                patient_ID = int(input("Incorrect ID, Enter patient ID : ")) - 1
                            try:
                                patientName=df_patients.iloc[patient_ID,1]
                                posName=list(df_appointments.iloc[:,1]).index(patientName)
                                df_appointments.drop(posName,axis='index')
                                print_green(
                                    "/----------------------appointment cancelled successfully----------------------/")
                            except:
                                print_red("No Appointment for this patient")
                        except ValueError:  # To avoid no return function
                            print_red("Patient ID should be an integer number")

                    elif Admin_choice == "E":  # Back
                        break

                    else:
                        print_red("please enter a correct choice")

                elif AdminOptions == "E":  # Back and ask whether to save data or not
                    checkDataSave=input("DO you want to save whatever you have edited?Y/n:")
                    if checkDataSave.lower()=='y':
                        df_patients.to_csv(r"C:\Users\VINAY SAHAL\Downloads\Patients_DataBase.csv",index=False)
                        df_appointments.to_csv(r"C:\Users\VINAY SAHAL\Downloads\appointments.csv",index=False)
                        df_doctors.to_csv(r"C:\Users\VINAY SAHAL\Downloads\Doctors_DataBase.csv",index=False)
                    else:
                        break
                else:
                    print_red("Please enter a correct option")

            elif Password != "1234":
                if tries < 2:
                    Password = maskpass.askpass(prompt="Incorrect Password,PLease Try Again:",mask="*")
                    tries += 1
                else:
                    print("Incorrect password, no more tries")
                    tries_flag = "Close the program"
                    break

    elif Admin_user_mode == "2":  # User mode
        print(
            "****************************************\n|         Welcome to user mode         |\n****************************************")
        while True:
            print("\n-----------------------------------------")
            print("|To view hospital's departments Enter 1 |")
            print("|To view hospital's doctors Enter 2     |")
            print("|To view patients' residents Enter 3    |")
            print("|To view patient's details Enter 4      |")
            print("|To be Back Enter E                     |")
            print("-----------------------------------------")
            UserOptions = input("Enter your choice : ")
            UserOptions = UserOptions.upper()

            if UserOptions == "1":  # User mode --> view hospital's departments
                print("Hospital's departments :")
                for i in list(df_doctors.iloc[:, 1]):
                    print_green(i)

            elif UserOptions == "2":  # User mode --> view hospital's Doctors
                print("Hospital's doctors :")
                for i in list(df_doctors.iloc[:, -2]):
                    print_green(
                        i)

            elif UserOptions == "3":  # User mode --> view patients' residents
                for i in list(df_patients.iloc[:, -1]):
                    print_green(i)

            elif UserOptions == "4":  # User mode --> view patient's details
                try:  # To avoid non integer input
                    patient_ID = int(input("Enter patient's ID : ")) - 1
                    while patient_ID not in df_patients.index:
                        patient_ID = int(input("Incorrect Id, Please enter patient ID : ")) - 1
                    print("	patient name        : ", df_patients.iloc[patient_ID, 1])
                    print("	patient age         : ", df_patients.iloc[patient_ID,2])
                    print("	patient gender      : ", df_patients.iloc[patient_ID, 3])
                    print("	patient address     : ", df_patients.iloc[patient_ID, -1])
                    if (df_patients.iloc[patient_ID, 1]) in list(df_appointments.iloc[:,1]):
                        count=list(df_appointments.iloc[:,1]).index(df_patients.iloc[patient_ID, 1])
                        print_green("Department: "+df_appointments.iloc[count,-3])
                        print_green("Doctor Following: "+df_appointments.iloc[count,2])
                        print_green("Room Number: "+str(df_appointments.iloc[count,-2]))
                    else:
                        print("This patient is not followed by Doctor!")
                except ValueError:
                    print("Patient ID should be an integer number")
            elif UserOptions == "E":  # Back
                break

            else:
                print_red("Please Enter a correct choice")

    elif Admin_user_mode == "404":
        print(colored("Thank You for using the software!", "yellow"))
        break
    else:
        print(colored("Please press 1 or 2", "magenta"))