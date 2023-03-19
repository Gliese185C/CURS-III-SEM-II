import string

inputs = "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
outputs = "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
rot13 = string.maketrans (inputs, outputs)
string = raw_input ("Phrase to convert:")
print string.translate(rot13)


