def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if(number < 0):
        print("Negative number does not have a square root")
        return None
    
    left = 0
    righ = number
    middle = 0

    while left <= righ:
        middle = (righ + left) // 2
        target = middle*middle
        if target == number:
            return middle
        elif target < number:
            left = middle + 1
        elif target > number:
            righ = middle - 1
    
    return middle


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (None == sqrt(-5)) else "Fail")
print("Pass" if (0 == sqrt(-0)) else "Fail")
