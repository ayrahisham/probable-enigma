# Assignment 1
# subject code : CSIT110
# name : Nur Suhaira
# student number : 5841549
# date : 02/10/2018

#Write a python program to
#1. Load a student result csv data file. (see appendix)

heading = "Student's details"
partition1 = "=============="
partition2 = "==================================================="
sid = "Student ID"
fname = "First Name"
lname = "Last Name"
mod110 = "CSIT110"
mod121 = "CSIT121"
mod135 = "CSIT135"
mod142 = "CSIT142"
avg = "Average"
ok = False
        
import csv
filePath = "data.csv"
with open(filePath) as csvfile:
    reader = csv.DictReader(csvfile)

    #2.	Ask the user to input the student ID
    idOK = False
    while (idOK == False):
        studentid = input("Enter student ID: ")
        if (not studentid == ""):
            if (len(studentid) == 9):
                if (studentid[0] == 'S' or studentid[0] == 's'):
                    if (studentid[1:8].isdigit() == True):
                        if (studentid[8].isalpha() == True):
                            idOK = True
                            print (partition1)
                            print ()
                            for row in reader:
                                filesid = row['student_id']
                                filefname = row['first_name']
                                filelname = row['last_name']
                                filemod110= int(row['CSIT110'])
                                filemod121 = int(row['CSIT121'])
                                filemod135 = int(row['CSIT135'])
                                filemod142 = int(row['CSIT142'])
                                fileavg = round ((filemod110 + filemod121 + filemod135 +filemod142 ) / 4, 2)

                                #3.	Display the student’s result with that student ID.
                                if (studentid == filesid ):
                                    ok = True
                                    print (heading)
                                    print (partition1)
                                    print ()
                                    print ("{0:<10} | {1:>11} | {2:<11}".format (sid, fname, lname))
                                    print ("{0:<10} | {1:>11} | {2:<11}".format (filesid, filefname, filelname))
                                    print (partition2)
                                    print ("{0:^8} | {1:^8} | {2:^8} | {3:^8} | {4:^8}".format (mod110, mod121, mod135, mod142, avg))
                                    print ("{0:^8} | {1:^8} | {2:^8} | {3:^8} | {4:^8}".format (filemod110, filemod121, filemod135, filemod142, fileavg))
                                    print (partition2)
                        else:
                            print ("Student id must end with an alphabet")
                    else:
                        print ("Student id must consists of 7 digits")
                else:
                    print ("Student id must start with 'S'")
            else:
                print ("Length of student id must be 9")
        else:
            print ("Empty input, please enter again")
    
            
if (ok == False):
    print ("No student record found")
            
