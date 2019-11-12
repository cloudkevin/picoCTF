message = 'UFJKXQZQUNB'
key = 'SOLVECRYPTO'
decrypted_message = []

for i in range(len(message)):
	x = (ord(message[i]) - 
		 ord(key[i]) + 26) % 26
	x += ord('A') 
	decrypted_message.append(chr(x))

print(f"Decrypted Text: {''.join(decrypted_message)}")