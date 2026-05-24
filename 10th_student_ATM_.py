pin = 1234
chances = 3
ATM_stored_amount = float(20000)
o = float(ATM_stored_amount)
print("Press ''1'' to check balance")
print("press ''2'' to withdrw cash  ")
menu = int(input("Enter Here:    "))
if menu == 1:
	pin2 = int(input("Enter Pin:   "))
	if pin2 == pin:
		print("₹",o,"is your balance")
elif menu == 2:
    while chances > 0:
    	pin1 = int(input("Enter your pin:   "))
    	if pin1 != pin:
    		chances -= 1
    		print("Wrong pin ,Try Again")
    		if chances ==0:
    			print("System blocked")
    			break
    	elif pin1 == pin:
    		print("Enter Cash")
    		
    		amount = float(input("Enter Here:  "))
    		if amount > ATM_stored_amount:
    			print("Out of maximum Amount")
    		elif amount <= ATM_stored_amount:
    			ATM_stored_amount -= amount
    			print("Debited  ₹",amount," Successfully")
    			break
else:
	print("You Entered Wrong Option")
