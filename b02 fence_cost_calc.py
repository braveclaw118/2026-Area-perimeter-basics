# Check all numbers are above 0
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

#main things
keep_going = ""
while keep_going == "":
    # get user input for width, height and cost per meter
    width = num_check("width: ")
    height = num_check("height: ")
    meter_cost = num_check("meter cost: ")
    # calculate the perimeter
    perimeter = ((width + height) * 2)
    # calculate the cost
    overall_cost = (perimeter * meter_cost)
    # output cost and perimeter
    print(f"Perimeter is {perimeter}")
    print()
    print(f"Total fence cost is ${overall_cost:.2f}")
    print()
    # ask user if they want to do it again (<enter> for loop, any key to stop)
    keep_going = input("If you want to keep going, press enter. if you want to quit, press any other key.")
    print()
print ("Thank you for using the fence cost calculator.")