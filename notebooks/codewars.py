def narcissistic(value):
    # count number of digits
    num_digits = len(str(value))
    digits = []
    for i in str(value):
        digit = int(i)
        digits.append(digit)
    result = [i**num_digits for i in digits]
    sum = 0
    for i in result:
        sum += i
    return sum == value


def find_outliers(integers):
    # check if array contains odd or even numbers
    odd = (i for i in integers if i%2!=0)
    even=(i for i in integers if i%2==0)
    # compare length of two lists
    # if len(odd) < len(even):
    #     return odd[0]
    # else:
    #     return even[0]
    first_odd=next(odd)
    first_even=next(even)
    if sum(1 for i in odd)<sum(1 for i in even):
        return first_odd
    else:
        return first_even

def validate_pin(pin):
    num_digits=len(str(pin))
    digits=[]
    for i in pin:
        if i.isdigit():
           digit=int(i)
           digits.append(digit)
        else:
           return False
    if num_digits==4 or num_digits==6:
       return True
    else:
       return False 
def split_string(string):
    if len(string) % 2 == 0:
        pairs = [string[i:i+2] for i in range(0, len(string), 2)]
    else:
        pairs = [string[i:i+2] for i in range(0, len(string)-1, 2)]
        pairs.append(string[-1] + '_')
    return pairs
def two_sum(numbers,target):
    num_dict={}
    for i,j in enumerate(numbers):
        complement=target-j
        if complement in num_dict:
            return [num_dict[complement],i]
        num_dict[j]=i
    return None
def increment_string(strng):
    #split the string
    splitted=[i for i in strng]
    if splitted[-1].isdigit():
        #increment last digit
        splitted[-1]=str(int(splitted[-1])+1)
    else:
        splitted.append(str(1))
    return "".join(splitted)
if __name__=="__main__":
    print(increment_string("foo"))
    print(increment_string("foobar23")) 
    print(increment_string("foobar910"))