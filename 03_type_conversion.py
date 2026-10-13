#TYPE CONVERSION (implicit which happens inside python and explicit which is done by the user)
#eg - float + int = float (implicit)
#casting - done by developer (explicit) int(), float(), str(), bool()

ans1 = int(5+10.0) #explicit
ans2 = 5+10.0 #implicit (TYPE CONVERSION HAPPENS INSIDE PYTHON)
print(ans1, type(ans1))
print(ans2, type(ans2))

val = bool(-10)
print(val, type(val)) #True (because 10 is a non-zero value)