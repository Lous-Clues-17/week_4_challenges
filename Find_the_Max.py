def find_max(numbers):
    # Check if the list is empty 
    if not numbers:
        return None
    
    # Start with the first number as "current max"
    max_val = numbers[0]
    
    # Loop through the rest of the list
    for num in numbers:
        if num > max_val:
            # Bigger number found! Update max.
            max_val = num
            
    return max_val

# Testing
print(find_max([4, 8, 5, 21, 15]))   # Output: 21
print(find_max([-8, -6, -1, -14]))   # Output: -1
print(find_max([-6, 5, 34, -14]))   # Output: 34