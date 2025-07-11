def calculate_grade(avg):

    if avg >=90:
        return 'A+'
    
    elif avg>=80:
        return "A"
    elif avg>=70:
        return "B"
    
    elif avg>=60:
        return "C"
    
    elif avg>=50:
        return "D"
    
    else:
        print("Better luck next time!")
        return "F"
    
def report_card():
    no_student=int(input("How many srudent?: "))
    student_data={}

    for i in range(no_student):
        name=input(f"\nEnter the student name{i+1}:")
        math=int(input("Enter math Number: "))
        sci=int(input("Enter Sci Number:  "))
        eng=int(input("Enter Eng Number: "))

        total=math+sci+eng
        avg=total/3
        grade=calculate_grade(avg)

        student_data[name]={
            "Total":total,
            "Average":round(avg,2),
            "Grade": grade

        }
    
    print("\n-----Report Card-----")

    for name,data in student_data.items():
        print(f"\nName: {name}")
        print(f"Total: {data['Total']}")
        print(f"Average:{data['Average']}")
        print(f"Grade: {data['Grade']}")

report_card()