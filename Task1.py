students={'Alice':85 ,'Mark':62,'Carol':96 ,
          'Mary':89, "Jony":87,'Jason':90}
name=input("Enter the student's name:" )
name=name.strip()
if name in students:
    print(f"{name}'s marks : {students[name]}")
else:
    print("The student is not listed in the given list .")
