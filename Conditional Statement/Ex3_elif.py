
marks=20

#  48>=65
if marks>=65:
    print("Distinction")
    #48>=60   and  62<65  -> true
elif marks>=60 and marks<65:
    print("1st class")
    #48>=50  and 55<60 -> true
elif marks>=50 and marks<60:
    print("2nd class")
    #48>=35  and 48<50
elif marks>=35 and marks<50:
    print("Pass")
else:
    print("Fail")


# true and true -> true
# true and false -> false
# false and true -> false
# false and false -> false

# if condition1:
#     body1
# elif condition2:
#     body2
# elif condition3:
#     body3
# elif condition4:
#     body4