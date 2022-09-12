ageyears = 0
agemonths = 0

birthy = 0
birthm = 0 

deathy = 0
deathm = 0 

print ("Hello, Welcome to my program. This program will take the birth date and death date of a person and it will calculate their time lived in honor of the Queen of England - Code by braindedd")
birthy = input("What is the Birth year of the Person? ")
birthm = input("What is the Birth month of the Person? ")

deathy = input("What is the Death year of the Person? ")
deathm = input("What is the Death month of the Person? ") 
#v takes year and subtracts them from eachother getting the final number of years that they lived
ageyears = (int(deathy)-int(birthy))
#v calculates the birth month, it takes the months and adds them togeather and subtracts 12 because thats how many months in a year 
final = (int(deathm) + int(birthm))
final = (int(final) - 12)

print ("They lived for ", ageyears ," years, and ", final , " months.")
