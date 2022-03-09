import pandas as pd 
data=pd.read_csv("Records.csv")
df=pd.DataFrame(data)
Add_data=False

# Here we are making a function if we want to add data in the dataframe.
def Add_Data(reg,name,fname,cnic,add,dob,bg,sec):
    dict= {"Registration Number": reg, "Full Name": name, "Father's Name": fname, "CNIC": cnic, "Postal Address": add, "Date of Birth": dob, "Blood Group": bg, "Section": sec }
    df.loc[len(df)] = dict
    df.to_csv("Records.csv", index=False)

# Starting the while loop (the main program).
run=True
while run:
    while True:
        try:
            # asking the user to choose an option between 1 and 4 .If entry is greater then 4 ,except command will be excuted.
            a=eval(input("Enter 1 to search by reg number, 2 to generate section list, 3 to add student data  and 4 to exit command: "))
            break
        except:
            print("Invalid entry please try again!")    
    if a == 1:
        while True:
            # the program runs and will ask for a registration number if the user enters "1".
            try:
                reg=eval(input("Enter Registration number: "))
                pd.set_option('display.max_columns', None)
                break
            # this command will be excuted if the registration number is not in the dataframe
            except:
                print("Invalid entry please try again!") 
        o=df[df["Registration Number"] == reg]
        # if the entered registration number is not in the dataframe the the use has the choice to add student data only if give registration number is not found in this command.
        # The choice/program to to ask user if he wants to add another student data.
        if o.empty:
            try:
                e = input("Record not found.Do you want to add student record ? (yes or no): ")
            except:
                print("Invalid entry please try again!")
            if e.lower() == "yes":
                Add_data = True
            else:
                pass
        else:
            print(o)
    elif a == 2:
        # This program is to generate section list based upon the user entry.
        sec=input("Enter Section(A or B): ")
        sec=sec.upper()
        pd.set_option('display.width', 300)
        o=df[df["Section"] == sec]
        print(o)
        if o.empty:
            print("Section not avaiable!!")
    elif a == 3:
        # This program is to add student data if the user enters "3".
        Add_data = True
    elif a == 4:
        # This command is to exit the program if the user enters "4".
        print("Have a good day")
        exit()
    elif a > 4 or a < 1:
        # This command is to print the given statement is the entry is greater than "4" or less than 1.
        print("Invalid entry please try again!") 

    # If the use wants to add another student data this is program will run,this program is connected to the function above.
    if Add_data == True:
        reg=int(input("Registration Number: "))
        name=input("Full name: ")
        fname=input("Father's name: ")
        cnic=input("CNIC Number(Use DASH): ")
        add=input("Postal Address: ")
        dob=input("Date of Birth: ")
        bg=input("Blood Group: ")
        sec=input("Section: ")
        Add_Data(reg,name,fname,cnic,add,dob,bg,sec)
exit()
