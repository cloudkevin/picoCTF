password = "jU5t_a_sna_3lpm16g84c_u_4_m0r846"
var i;
var buffer = Array(32);
for (i=0; i<8; i++) {
	buffer[i] = password.charAt(i);
}
for (; i<16; i++) {
	buffer[i] = password.charAt(23-i);
}
for (; i<32; i+=2) {
	buffer[i] = password.charAt(46-i);	
}
for (i=31; i>=17; i-=2) {
	buffer[i] = password.charAt(i);
}
console.log("picoCTF{" + buffer.join("") + "}");