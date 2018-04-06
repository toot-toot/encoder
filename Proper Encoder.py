
import codecs
a = input("Enter message:")
b = codecs.encode(a, 'rot13')
print (b)
print("To keep screen open, DO NOT press enter.")
input()
