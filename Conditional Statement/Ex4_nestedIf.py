
# syntax

# if condition1:
#     body1
#     if condition2:
#         body2
#     else:
#         elseBody2
# else:
#     elsebody1


PEM=400

#   400>=300
if PEM>=300:            #outer if
    print("selected in prelim Exam")
    print("preparing for mains Exam")

    MEM=900
    #  900>=800
    if MEM>=800:                #nested or inner if
        print("got selected in mains Exam")
    else:
        print("Rejected in main Exam")

else:
    print("Rejected in prelim exam")