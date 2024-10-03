# Create 3 variables to store street, city and country, now create address variable to store entire address. 
# Use two ways of creating this variable, one using + operator and the other using f-string. 
# Now Print the address in such a way that the street, city and country prints in a separate line

# street = "Shehwar Street\n"
# city = "Lahore\n"
# country = "Pakistan"
# address = street + city+country
# print(address)


# Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index

earth = "Earth revolves around the sun"
rel = earth.split(" ")
print(rel[1:2]) 
print(rel[-1]) 

# Create two variables to store how many fruits and vegetables you eat in a day.
#  Now Print "I eat x veggies and y fruits daily" 
# where x and y presents vegetables and fruits that you eat everyday. 
# Use python f string for this.
num_fruits = 5
num_veggies = 3
print(f"I eat {num_veggies} veggies and {num_fruits} fruits daily")

#I have a string variable called s='maine 200 banana khaye'. 
# This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. 
# Replace incorrect words in original strong with new ones and print the new string. 
# Also try to do this in one line.

s = "maine 200 bnanana khaye"
s = s.replace("200 bnanana", "10 samosa")
print(s)