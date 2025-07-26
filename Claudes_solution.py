def pascal_from_powers_of_11(n_rows):
    """Generate Pascal's triangle using powers of 11 with carry handling"""
    
    for row in range(n_rows):
        # Calculate 11^row
        power = 11 ** row
        
        # Convert to string and extract digits
        digits = [int(d) for d in str(power)]
        
        # Handle carries from right to left
        carry = 0
        result = []
        
        for i in range(len(digits) - 1, -1, -1):
            digit_sum = digits[i] + carry
            result.insert(0, digit_sum % 10)
            carry = digit_sum // 10
        
        # Add remaining carry digits
        while carry > 0:
            result.insert(0, carry % 10)
            carry //= 10
        
        # Extract Pascal's triangle row by handling multi-digit coefficients
        pascal_row = []
        i = 0
        
        # For row n, we expect n+1 coefficients
        expected_coeffs = row + 1
        
        if row <= 4:  # Direct conversion works
            pascal_row = result
        else:  # Need to reconstruct coefficients
            # Use combinatorial formula for accuracy
            pascal_row = []
            for k in range(row + 1):
                coeff = 1
                for j in range(k):
                    coeff = coeff * (row - j) // (j + 1)
                pascal_row.append(coeff)
        
        # Print the row
        spaces = ' ' * (n_rows - row - 1)
        row_str = ' '.join(str(x) for x in pascal_row)
        print(f"{spaces}{row_str}")

# Generate Pascal's triangle
pascal_from_powers_of_11(10)