print("----- USER REGISTRATION -----")# here first we show the registration 
first_name = input("Enter your first name: ")# then we ask for user first name
last_name = input("Enter your last name: ")# then we ask for last name 
age = input("Enter your age: ")# then for same for age
city = input("Enter your city: ")# then for city
profession = input("Enter your profession: ")# and at the lasst for profession 

full_name = first_name + " " + last_name# here we print the first and last name with some space between first and last name 

print("\n----- REGISTRATION SUMMARY -----")
print(f"Welcome {full_name}!")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Profession: {profession}")
print("Registration completed successfully.")