#project 1 form my captain
#to create a csv file that contains students_info_list

import csv

def write_into_csv(info_list):
    with open('students_info_.csv', 'a',newline='')as csvfile:
        writer = csv.writer(csvfile)

        if csvfile.tell()==0:
            writer.writerow(['Name','Age','Contact number','Email id'])
        writer.writerow(info_list)

if __name__==__name__:
    condition=True
    student_num=1

    while (condition):
        students_info_=input("Enter student information for the student #{} in the following format (Name Age Contact_number Email_id): ").format(student_num)
        
        

        #using split function
        students_info_list= students_info_.split(' ')
        

        print("\nThe entered information is -\nName: {}\nAge: {}\nConatct number: {}\nEmail id: {}"
            .format(students_info_list[0],students_info_list[1],students_info_list[2],students_info_list[3]))

        choice_check=input("Is the entered information is correct[yes/no] : ")

        if choice_check=="yes":
            write_into_csv(students_info_list)

            condition_check=input("Enter(yes/no) if you want to enter the information of another student :")
            if condition_check=="yes":
                condition=True
                student_num=student_num+1
            elif condition_check=="no":
                condition=False
        elif choice_check=="no":
            print("\nPlease check once again!") 
        
