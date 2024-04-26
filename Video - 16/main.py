# New Topic is Match case 

x = int(input("Enter Value of x: "))

match x:

    case 0:
        print("Yor Number is Zero")

    case 10:
        print("This Number is So Special")

    case 50:
        print("this Number is 50 means its half century")

    case _ if x < 100:
        print("Your Value is smaller than 100: ",x)

    case _:
        print("your Number is: ",x)
