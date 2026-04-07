def is_palindrome(text):
    # 1. Normalize: Lowercase and remove spaces
    # .replace(" ", "") only handles spaces; .lower() handles casing
    clean_text = text.lower().replace(" ", "")
    
    # 2. Reverse: Use the slicing trick from the last challenge
    reversed_text = clean_text[::-1]
    
    # 3. Compare: Return the Boolean (True or False)
    return clean_text == reversed_text

# Testing
print(is_palindrome("Madam"))                       # Output: True
print(is_palindrome("CodeYou"))                     # Output: False
print(is_palindrome("Forever is a feeling"))        # Output: False
print(is_palindrome("Civic "))                      # Output: True
