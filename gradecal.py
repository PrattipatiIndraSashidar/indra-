math=int(input("marks in math:"))
science=int(input("marks in science:"))
english=int(input("marks in english:"))
total_marks=math+science+english
average=total_marks/3
percentage=(total_marks/300)*100
grade=" "
if percentage >84:
    grade="A"
elif percentage >80 and percentage<=84:
    grade="B"
elif percentage >70 and percentage<=80:
    grade="C"
elif percentage >60 and percentage<=70:
    grade="D"
else:
    grade="F"
print(f"Total Marks:{total_marks} \nAverage:{average} \nGrade:{grade}")
