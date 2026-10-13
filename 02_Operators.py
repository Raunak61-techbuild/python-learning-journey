#OPERATORS

#1. ARITHMETIC
a = 10
b = 8
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #modulo (remainder)
print(a**b) #exponent


#2. RELATIONAL
a = 10
b = 5
print(5 > 8)
print (a == b)
print (a != b)


#3. ASSINGMENT
a = 10
print(a)
a+=5 #15 (add)
print(a)
a-=5 #10 (subtract)
print(a)
a*=5 #50 (multiply)
print(a)
a/=5 #10 (divide) a = a/5
print(a)
a%=5 #0 (modulus)
print(a)
a**=5 #0 (exponent)
print(a)


#LOGICAL
#not (Convers False -> True and True to false)
var = False
print(not var) #True (Becuase NOT CONVERTS FALSE TO TRUE & TRUE TO FALSE)
print(not 5>8)
print(not "France is Better than Japan") #False (Becuase NOT CONVERTS FALSE TO TRUE & TRUE TO FALSE)

#and (False if any one of them is false and returns false if both are false))
print(3>2 and 4>1) #True (Becuase both are true)
print(3>2 and 4<1) #False (Becuase ONE OF THEM is FALSE)

#or - only returns false when both are false
print(3>2 or 4<1) #True (Becuase ONE OF THEM is TRUE)
print(3>12 or 4<1) #FALSE (Becuase BOTH ARE FALSE)

