#ask for width and loop until they enter a number that's more than 0

def num_check(question):

    error = "Please enter a number that is more than 0\n"
    while True:

        try:
            response= float(input(question))

            if response > 0:
                return response
            else:
                (print(error))
        except ValueError:
            print (error)

# main routine goes here

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("width= ")
    height = num_check ("height: ")

    # Calculate area/perimeter
    area = width * height
    perimeter = 2 * (width + height)
    # Display output
    print()
    print(f"Perimeter:{perimeter} units")
    print()
    print(f"Area: {area} units")
    # ask user if the want to keep going
    keep_going = input("If you want to keep going, press enter. if you want to quit, press any other key.")
    print()

print ("Thanks you for using the area/perimeter calculator!")