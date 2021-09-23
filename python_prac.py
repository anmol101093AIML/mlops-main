import string
table=str.maketrans("S","M")
s="SSS"
print(s.translate(table))
print(string.punctuation)
table = str.maketrans('a','a',string.punctuation)
print("hello-world".translate(table))

print(b'anmol'.decode())