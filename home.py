import pprint
import time
print("Welcome to PillPal")
print("Please enter all time in 24 hour formant (HH:MM).")
inputMain = input("Are you a doctor or patient? ")
alarmsOn = False
patientList = { "John Doe": {
        "Advil": ["16:08", "16:09"],
    }}
    
def doctorMenu():
    print("*****************")
    print("Please enter from below options")
    print("Type 1 to add a patient")
    print("Type 2 to view current patients")
    print("Type 3 to remove a patient")
    print("Type 4 to change prescriptions")
    print("Type -1 to go back")
    print("*****************")
    doctorInput = input("Enter your input: ")
    return doctorInput
    
def patientMenu():
    print("*****************")
    print("Please enter from below options")
    print("Type 1 to turn alarms off")
    print("Type 2 to turn alarms on")
    print("Type 3 to view all prescriptions")
    print("Type -1 to go back")
    print("*****************")
    patientInput = input("Enter your input: ")
    return patientInput
    
def displayAlert():
    global alarmsOn

    while alarmsOn:
        current_hour = int(time.strftime("%H"))  # Get current hour as an integer
        current_minute = time.strftime("%M")
        
        adjusted_hour = (current_hour - 4) % 24
        
        if adjusted_hour < 10:
            adjusted_hour = "0" + str(adjusted_hour)
        else:
            adjusted_hour = str(adjusted_hour)
            
        adjusted_time = adjusted_hour + ":" + current_minute

        if len(timeList) != 0:
            if adjusted_time in timeList:
                idx = timeList.index(adjusted_time)
                medicine = medicineList[idx]
                print("Time to take " + medicine + " at " + adjusted_time + "!")
            
            time.sleep(30)
        else:
            print("Ask your doctor to add your medicine first.")
            alarmsOn = False
    
def doctor1():
    doctorInput1 = input("Enter patient name to add: ")
    if doctorInput1 in patientList:
        print("Patient is already in the system")
    else:
        patientList[doctorInput1] = {}
        print("Patient added succesfully")
        
def doctor3():
    doctorInput3 = input("Enter patient name to remove: ")
    if doctorInput3 in patientList:
        del patientList[doctorInput3]
        print("Patient removed succesfully.")
    else:
        print("Patient doesn't exist.")
        

while True:   
    if inputMain == "doctor":
        while True:
            doctorInputA = doctorMenu()
            if doctorInputA != "1" and doctorInputA != "2" and doctorInputA != "3" and doctorInputA != "4" and doctorInputA != "-1":
                print("Please enter a valid input.")
                break
            
            doctorInputA = int(doctorInputA)
            if doctorInputA == 1:
                doctor1()
            elif doctorInputA == 2:
                print("Current Patients and Prescriptions: ")
                pprint.pprint(patientList, sort_dicts=False, width=60)
            elif doctorInputA == 3:
                doctor3()
            elif doctorInputA == 4:
                doctorInput4PatName = input("Enter patient name whose prescription needs to be changed: ")
                
                if doctorInput4PatName not in patientList:
                    print("Patient doesn't exist. Please add patient first.")
                    break
                    
                doctorInput4 = input("""-----------------
Type 1 to add a prescription
Type 2 to remove a prescription
Enter your input: """)
                
                if doctorInput4 == "1":
                    doctorInput4PreNameAdd = input("Enter prescription name to add: ")
                    doctorInput4PreTimeAdd= input("Enter time to take prescription: ")
                    if doctorInput4PreNameAdd in patientList[doctorInput4PatName]:
                        patientList[doctorInput4PatName][doctorInput4PreNameAdd].append(doctorInput4PreTimeAdd)
                        print("Prescription time added succesfully.")
                    else:
                        patientList[doctorInput4PatName][doctorInput4PreNameAdd] = []
                        patientList[doctorInput4PatName][doctorInput4PreNameAdd].append(doctorInput4PreTimeAdd)
                        print("Prescription & Prescription time added succesfully.")
                elif doctorInput4 == "2":
                    doctorInput4PreNameRemove = input("Enter prescription name to remove: ")
                    doctorInput4PreTimeRemove= input("Enter prescription time to remove: ")
                    
                    if doctorInput4PreNameRemove in patientList[doctorInput4PatName]:
                        if doctorInput4PreTimeRemove in patientList[doctorInput4PatName][doctorInput4PreNameRemove]:
                            if len(patientList[doctorInput4PatName][doctorInput4PreNameRemove])>=2:
                                patientList[doctorInput4PatName][doctorInput4PreNameRemove].remove(doctorInput4PreTimeRemove)
                                print("Prescription time removed succesfully.")
                            else:
                                del patientList[doctorInput4PatName][doctorInput4PreNameRemove]
                                print("Prescription & Prescription time removed succesfully.")
                        else:
                            print("Prescription time doesn't exist.")
                            break
                    else:
                        print("Prescription doesn't exist.")
                        break
                else:
                    print("Please enter a valid input.")
                    
            elif doctorInputA == -1:
                inputMain = input("Are you a doctor or patient? ")
                break

    elif inputMain == "patient":
        patientName = input("Enter your name: ")
        if patientName not in patientList:
                print("You are not on the list. Please tell your doctor to add you to the list.")
                inputMain = input("Are you a doctor or patient? ")
                continue

        while True:
            patientInputA = patientMenu()
            if patientInputA != "1" and patientInputA != "2" and patientInputA != "3" and patientInputA != "-1":
                print("Please enter a valid input.")
                break
    
            patientInputA = int(patientInputA)
            if patientInputA == 1:
                alarmsOn = False
                print("All alarms are off!")
                
            elif patientInputA == 2:
                timeList.clear()
                medicineList.clear()
                
                for preName in patientList[patientName]:
                    for preTime in patientList[patientName][preName]:
                        timeList.append(preTime)
                        medicineList.append(preName)
                alarmsOn = True
                displayAlert()
            
            elif patientInputA == 3:
                patientMedicine = patientList[patientName]
                print("Your medicine is: " + str(patientMedicine))
                
            elif patientInputA == -1:
                inputMain = input("Are you a doctor or patient? ")
                break
                
    else:
        print("Please enter doctor or patient.")
        inputMain = input("Are you a doctor or patient? ")