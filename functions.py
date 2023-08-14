def is_even(num):
    """
    This is a doc string used to document the utility of the function
    """
    x=num%2==0
    return x

print(is_even(27))



def is_divisibleByThree(num):
    """
    This function tells whether a given number is divisible by three or not
    Input: any valid integer
    Output: divisible by three or not
    Created By: Vanshika Dargan
    Last Edited: 14-Aug-2023
    """
    return num%3==0

print(is_divisibleByThree(8))



def is_LeapYear(year):
    """
    This function tells whether a given year is leap year or not
    Input: any valid year
    Output: Leap year or not
    Created By: Vanshika Dargan
    Last Edited: 14-Aug-2023
    """

    if (year%400==0) or (year%100!=0 and year%4==0):
        print("Is Leap Year")
    else:
        print("Not a Leap Year")

for year in range(2000,2016):
    print("Year",year,end=' ')
    is_LeapYear(year)

#  how to print the documentation
print(is_LeapYear.__doc__)

print(print.__doc__)

#how to prevent crashing of code is user passes let's say string in place of number

def even(num):
    if type(num) !=int:
        return "Invalid type"
    else:
        if num%2==0:
            return "Even"
        else:
            return "Odd"

print(even(9))


