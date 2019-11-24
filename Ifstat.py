a = "Male"
b = "Tall"

if a == "Male" and b == "Tall":
    print ("You are a " + b + " " +a)
elif a == "Male" and b != "Tall":
    print ("You are a "+ a + " but not " + b)
elif a != "Male" and b == "Tall":
    print ("You are not a " + a + " but you are " + b)
else :
    print ("You are neither a " + a + " nor " + b)