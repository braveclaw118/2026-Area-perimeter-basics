#ask for width and loop until they enter a number that's more than 0


error = "Please enter a number that is more than 0\n"
while True:
    try:
        width= float(input("Width= "))

        if width > 0:
            break
        else:(print(error))
    except ValueError:
        print (error)