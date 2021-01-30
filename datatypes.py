a=10
print("value of var a:",a)
print("data type of var a:", type(a))
print("address of var a:", id(a))

#int type
print("------------------------");
print("Int value", 1234)
print("Binary value 1:", 0b11)
print("Binary value 2:", 0B1111111110)

print("Octal value 1:", 0o122)
print("Octal value 2:", 0O1227)

print("Hexa value 1:", 0x456)
print("Hexa value 2:", 0XFF)
print("Hexa value 3:", 0xa)
print("Hexa value 4:", 0xFACE)

print("-----------Base conversion functions----------")
print("bin() conversion of 15:", bin(15));
print("bin() conversion of 0o123:", bin(0o123));
print("bin() conersion of 0xBEEF:", bin(0xBEEF));

print("oct() conversion of 15:", oct(15));
print("oct() conversion of 0b101:", oct(0b101));
print("oct() conversion of OxBEEF:", oct(0xBEEF));

print("hex() conversion of 15:", hex(15));
print("hex() conversion of 0o123:", hex(0o123));
print("hex() conversion of 0b1011:", hex(0b1011));

print("---------------complex data type---------------")
x=10+20j
print(x)
print(type(x))
print("real part: ", x.real)
print("imaginary part: ", x.imag);
y=5+10j
print("addition of complex values: ", x+y);
print("mul of complex values:", x*y);
