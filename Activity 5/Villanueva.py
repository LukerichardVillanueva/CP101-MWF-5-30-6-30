lukeString = "Luke White Hat@0128"

lowercase = 0
uppercase = 0
digitcount = 0
specialcharacters = 0

for luke in lukeString:
 if luke.islower():
  lowercase += 1
  
 elif luke.isupper():
  uppercase += 1
	
 elif luke.isdigit():
  digitcount += 1
  
 else:
  specialcharacters += 1
	
print("Lowercase letters: ", lowercase)

print("Uppercase letters: ", uppercase)

print("Digits: ", digitcount)

print("Special Characters: ", specialcharacters)
