
weight = 10

#Ground Shipping 

if weight <= 2: 
    price_per_pound = 1.50
elif weight <= 6: 
    price_per_pound = 3.00
elif weight <= 10:
    price_per_pound = 4.00
else:
    price_per_pound = 4.75

print("Ground Shipping $", price_per_pound)

#Drone Shipping 

weight = 10

if weight <= 2: 
    price_per_pound = 4.50
elif weight <= 6: 
    price_per_pound = 9.00
elif weight <= 10:
    price_per_pound = 12.00
else:
    price_per_pound = 14.25

print("Drone Shipping $", price_per_pound)

 

