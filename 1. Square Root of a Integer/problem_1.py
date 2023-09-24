def sqrt(number):
    """
    Calculate the floored square root of a number
    If input is negative, return number to multiply by i

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # Return 0 if input number is 0
    if number == 0:
        return 0

    # Change negative number to positive
    if number < 0:
        number = number * -1

    current_guess = 10

    # Lowest real value possible
    lower = 0  

    # Use 10 as the original upper bound for the guess range
    upper = 10  

    # Shift the bounds of the guess range based on the (upper bound)^2 relative to the input number
    while upper * upper < number:
        lower = upper
        upper = upper * 2

    # If you got the guess right on the first try
    if upper * upper == number:
        return current_guess

    # Otherwise we need to iterate between the lower and the upper bound
    while abs(current_guess - (upper + lower)//2) > 0:
        # Find the middle of the range
        midpoint = (upper + lower)//2

        # Maybe the midpoint was the answer?
        if midpoint * midpoint == number:
            return midpoint

        # Otherwise adjust the range appropriately based on the value of (midpoint)^2 relative to the bounds
        elif midpoint * midpoint > number:
            upper = midpoint
        else:
            lower = midpoint

        current_guess = midpoint

    return current_guess


# Test case 1
print("Pass" if (5 == sqrt(27)) else "Fail")
# Test case 2
print("Pass" if (9 == sqrt(90)) else "Fail")
# Test case 3
print("Pass" if (6 == sqrt(40)) else "Fail")
# Test case 4
print("Pass" if (11 == sqrt(140)) else "Fail")
# Test case 5
print("Pass" if (3 == sqrt(9)) else "Fail")
# Test case 6
print("Pass" if (0 == sqrt(0)) else "Fail")
# Test case 7
print("Pass" if (5 == sqrt(-27)) else "Fail")
# Test case 8
print("Pass" if (0 == sqrt(124)) else "Fail")