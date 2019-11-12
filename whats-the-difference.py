cattos = open("cattos.jpg", "rb").read()
kitters = open("kitters.jpg", "rb").read()
 
flag = ""
 
for i in range(len(cattos)):
	if cattos[i] != kitters[i]:
		flag += cattos[i]
 
print(flag)