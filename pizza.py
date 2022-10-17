print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":           #Small
  bill += 15
elif size == "M":         #m
  bill += 20
else:                     #Large
  bill += 25

if add_pepperoni == "Y":  #pepperoni
  if size == "S":         #small with pepperoni
    bill += 2
  else:                   #large or med with pepperoni
    bill += 3
#cheese    
if extra_cheese == "Y":
  bill += 1  
print(f"Your final bill is: ${bill}.")

