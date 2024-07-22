# Problem 2
# write a program to find out whether a student has passed or failed, if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter your marks: "))
sub2 = int(input("Enter your marks: "))
sub3 = int(input("Enter your marks: "))

total_percent = ((sub1+sub2+sub3)*100)/300

if total_percent >= 40 and sub1 > 33 and sub2 > 33 and sub3 > 33:
    print("You are pass, your percentage is", total_percent)
else:
    print("You failed, try again next year, your percentage is", total_percent)
