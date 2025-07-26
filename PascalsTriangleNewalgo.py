n = 6

def elevens_pascal(n:int):
    
    for i in range(1,n):
        
        out = carry_consolidator(i)
        
        


def carry_consolidator(digits:list):
    
    length = len(digits)
    
    shifted_digits = digits + [0]
    digits = [0] + digits 
    
    pascal_form = []
    
    for i in range(length+1):
        
        result = digits[i] + shifted_digits[i]
        if result >= 10:
            
            carry = result//10
            remainder = result%10
            # print(f"Digit:{digits[i]} Digit:{shifted_digits[i]} Result: {result} Carry:{carry} Remainder:{remainder}")
            # print(f"Before: {pascal_form}")
            # pascal_form[n-i-1] = remainder
            pascal_form = pascal_form+[carry]
            # print(f"After pascal_form[n-i-1]: {pascal_form}")
            pascal_form = pascal_form+[remainder]
            # print(f"After pascal_form[n-i-2]: {pascal_form}")
        else:
            pascal_form = pascal_form+[result]
            
    # print(f"Digits: {digits}")
    # print(f"ShiftedDigits: {shifted_digits}")
    # print(f'Pascal form: {pascal_form}')
    
    # print(f"{digits}")
    # print(f"{shifted_digits}")
    # print(f'{pascal_form}')
    return pascal_form
if __name__ == "__main__":
    
    # carry_consolidator(digits=[1,3,3,1])
    # carry_consolidator(digits=[1,4,6,4,1])
    carry_consolidator(digits=[1])
        
            
    
    