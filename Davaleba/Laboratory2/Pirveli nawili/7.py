num = input("Please enter Year")
if int(num)%4==0:
    print("Es weli nakiania")
elif int(num) >= 400:
    if int(num)%100==0 and int(num)%400==0:
        print("Es weli nakiania")
    else:
        print("Es weli nakiani ar aris")
else:
    print("es weli nakiani ar aris")