# Define a function that accepts a percentage as an argument and returns a letter grade (A+, A, A-, B+, etc) for that percentage.

# Prompt your user to enter a percentage and display a message showing them the equivalent letter grade.
percent = 0

def get_input():
    wait_for_input=True
    while wait_for_input == True:
        print("Please enter a percentage grade, no need to add %")
        percent = float(input())
        if percent >=0 and percent <=100:
            return(percent)
        else: 
            print("your input was unrecognized or invalid/n")
            print("Please enter a percentage grade, no need to add %")

#
#Letter grade	Percentage	GPA
#A+	97–100%	4.33/4.00 or 4.00/4.00
# A	93–96%	4.00/4.00
# A−	90–92%	3.67/4.00
# B+	87–89%	3.33/4.00
# B	83–86%	3.00/4.00
# B−	80–82%	2.67/4.00
# C+	77–79%	2.33/4.00
# C	73–76%	2.00/4.00
# C-	70–72%	1.67/4.00
# D+	67–69%	1.33/4.00
# D	63–66%	1.00/4.00
# D-	60–62%	0.67/4.00
# F	0–59%	0.00/4.00


def percent_to_grade(percent):
    if percent >= 97 and percent <=100:
        return("A+")
    elif percent >=93 and percent<97:
        return ("A")
    elif percent >=90 and percent<93:
        return("A")
    elif percent >=87 and percent<90:
        return("B+")
    elif percent >=83 and percent<87:
        return("B")
    elif percent >=80 and percent<83:
        return("B-")
    elif percent >=77 and percent<80:
        return("C+")
    elif percent >=73 and percent<77:
        return("C")
    elif percent >=70 and percent<73:
        return("C-")
    elif percent >=67 and percent<70:
        return("D+")
    elif percent >=63 and percent<67:
        return("D")
    elif percent >=60 and percent<63:
        return("D-")
    else:
        return("F")


percent = get_input()
print("A percent grade of {} is equivilent to a letter grade of {}".format(percent,percent_to_grade(percent)))