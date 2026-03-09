#ask user their name
username = input ("Hi there, what is your name?")
# ask user their favourite number (INTEGER)
fav_number= int(input("Okay, what is your favourite number?"))
#double, halve and square users favourite number
double= fav_number * 2
halve= fav_number / 2
square= fav_number * fav_number
#greet user
print(f"\nHi,{username}! Your favourite number is {fav_number}, right? Heh, I knew i remembered correctly!:)")
#output results of doubling, halving and
# squaring their favourite number
print(f"Well, {fav_number} multiplied by 2 is {double}.\n{fav_number} halved is {halve}.\nAnd {fav_number} squared is {square}\nPretty cool, right?")
print()
print(f"Have a nice day, {username}!")