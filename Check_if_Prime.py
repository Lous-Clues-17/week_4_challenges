def is_prime(n):
    # 1. Handle Edge Cases: Anything less than 2 is NOT prime
    if n < 2:
        return False
    
    # 2. Check Divisibility: Look at every number from 2 up to (but not including) n
    for i in range(2, n):
        if n % i == 0:
            # We found a divisor! It's not prime.
            return False
            
    # 3. If the loop finishes without finding a divisor, it IS prime
    return True

# Testing
print(is_prime(21)) # True
print(is_prime(13)) # False
print(is_prime(1))  # False