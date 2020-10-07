                                            #faulty calculater

while (True):
 a = float(input("Enter Your First Number:"))
 c= input("Which Action Do You Wants Enter Here:")
 b = float(input("Enter Your Second Number:"))

 re1 = a+b
 re2 = a*b
 re3 = a/b
 re4 = a-b

 if a==56 and b==9 and c=="+":
    print(77)

 elif a==56 and b==6 and c=="/":
    print(4)

 elif a==45 and b==3 and c=="*":
    print(555)

 #swaping numbers.

 elif a==9 and b==56 and c=="+":
    print(77)

 elif a==6 and b==56 and c=="/":
    print(4)

 elif a==3 and b==45 and c=="*":
    print(555)


 else:
    if "+" in c:
        print(re1)
    elif "/" in c:
        print(re3)
    elif "*" in c:
        print(re2)
    elif "-" in c:
        print(re4)
    else:
        print("Error.")

    A = input("if You Wants T Re Calculate Enter 'Y' Else Enter 'N':")

    if "n"in A:

        print("Thanks .")
        break
    if "y" in A:

        print("Then Enjoying !!!")
        continue

    else:

       print("Error.")
       print("Please Type 'Y' Or 'N' , Nothing Else.")
       break

