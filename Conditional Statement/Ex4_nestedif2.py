

SA=2500
 #2500>=500
if SA>=500:         #outer if
    print("free delivery")
    # 2500>=2000
    if SA>=2000:    #inner if or nested if
        print("Additional 10% discount")
    else:
        print("No Additional discount")
else:
    print("RS 50 delivery charges applied")