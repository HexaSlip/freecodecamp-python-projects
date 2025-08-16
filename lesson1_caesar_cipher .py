#========================
#Caesar Cipher Starter
# =======================

# 1. Variables
number = 5
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# 2. String basics 
print("Original text:", text) 
print("Character at index 6:", text[6])  # 'W'
print("Last Character:", text[-1])       # 'd'
print("Length of text:", len(text))      # 11
print("Type of text:", type(text))       # <class str >
print("Type of shift:", type(shift))     # <class 'int'> 

# 3. Alphabet reference 
print("Alphabet:", alphabet)
print("Index of 'z':", alphabet.find('z'))  # 25

# 4. Lowercase conversion 
lower_text = text.lower() 
print("Lowercased text:", text.lower())

# 5. Find index of first character
first_char = lower_text[0]                # 'h'
index = alphabet.find(first_char)         #  7
print("Index of the first character:", index)

#6. Apply Caesar shift (example for first character only)
shifted = alphabet[index + shift]
print("Shifted character:", shifted)
