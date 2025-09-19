
text = "Python"

print("First character:", text[0])       # P
print("Last character:", text[-1])       # n
print("From index 0 to 3:", text[0:4])   # Pyth
print("From index 2 to end:", text[2:])  # thon

print("\n")  # Just adds a blank line for readability


word = "hello world"

print("Uppercase:", word.upper())                   # HELLO WORLD
print("Lowercase:", word.lower())                   # hello world
print("Split into words:", word.split())            # ['hello', 'world']
print("Replace word:", word.replace("world", "Python"))  # hello Python

print("\n")


sentence = "I love coding in Python"

print(sentence.upper())          # I LOVE CODING IN PYTHON
print(sentence.lower())          # i love coding in python
print(sentence.split())          # ['I', 'love', 'coding', 'in', 'Python']
print(sentence.replace("Python", "Java"))  # I love coding in Java

print("\n")

word = "programming"

print(word.upper()[0:6])   # PROGRA
print(word.lower()[3:10])  # grammin
