alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("""HELLO WELCOME TO CAESAR CIPHER \n""")
button= True
try:
	
	while button == True: 
		direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
		if not (direction== "encode" or direction== "decode") :
			print("please enter valid value")
			continue
		text = input("Type your message:\n").lower()
			
		shift = int(input("Type the shift number:\n"))
		shift = shift % 26
	
		def caesar(new_text,shifting,direction_of_the_system):
			empty= ""
			
			if direction_of_the_system == "decode":
				shifting *= -1
			
			for letters in new_text:
				
				if letters in alphabet:
					position= alphabet.index(letters)
					new_position = position + shifting
					empty += alphabet[new_position]
				else:
					empty += letters
			
			print("The {}d text is '{}' ".format(direction_of_the_system,empty))
		caesar(new_text=text,shifting=shift,direction_of_the_system=direction)
		
		permission = input("do you want to quit? 'yes' or 'no' \n ").lower()
		if permission == "yes":
			button = False
			break
		elif permission== 'no':
			continue
except:
	print('please enter valid value')
	pass
	
#source:
#Dr. Angela Yu's python course on Udemy
