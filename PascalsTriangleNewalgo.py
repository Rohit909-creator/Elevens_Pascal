n = 6

def elevens_pascal(n:int):
    
    out = [1]
    for _ in range(1,n):
        
        out = carry_consolidator(out)
        print(f"Number: {out}")
        
    print(out)


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
            
            pascal_form = pascal_form +[carry*10+remainder]
            # print(f"After pascal_form[n-i-2]: {pascal_form}")
        else:
            pascal_form = pascal_form+[result]
            
    
    return pascal_form[::-1]
if __name__ == "__main__":
    
    # carry_consolidator(digits=[1,3,3,1])
    # carry_consolidator(digits=[1,5,10,10,5,1])
    # carry_consolidator(digits=[1,6,15,20,15,6,1])
    # carry_consolidator(digits=[1])
    
    print(elevens_pascal(15))
    
    