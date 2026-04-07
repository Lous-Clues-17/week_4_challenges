def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        # Handle Uppercase
        if char.isupper():
            # ord('A') is 65. We subtract 65 to get 0-25 range.
            # Then shift, wrap with % 26, and add 65 back.
            index = ord(char) - ord('A')
            new_index = (index + shift) % 26
            result += chr(new_index + ord('A'))
            
        # Handle Lowercase
        elif char.islower():
            # ord('a') is 97. We subtract 97 to get 0-25 range.
            index = ord(char) - ord('a')
            new_index = (index + shift) % 26
            result += chr(new_index + ord('a'))
            
        # Handle Non-letters (Spaces, !, 123)
        else:
            result += char
            
    return result

# Testing
print(caesar_cipher("xyz", 3))            # Output: def
print(caesar_cipher("def", 2))            # Output: zab
print(caesar_cipher("Hello, World!", 5))  # Output: Mjqqt, Btwqi!