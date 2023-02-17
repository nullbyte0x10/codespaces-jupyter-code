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


if __name__ == "__main__":
    print(find_outliers([2, 4, 0, 100, 4, 11, 2602, 36]))
    print(find_outliers([160, 3, 1719, 19, 11, 13, -21]
                        ))
