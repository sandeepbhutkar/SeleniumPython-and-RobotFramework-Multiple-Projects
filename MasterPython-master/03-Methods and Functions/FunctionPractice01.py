# Write a function that returns the lesser of two given numbers if both numbers are even, but return greater
# if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        # both numbers are even
        if a < b:
            result = a
        else:
            result =b
    else:
        # one or both numbers are odd
        if a > b:
            result = a
        else:
            result = b
    return result

print(lesser_of_two_evens(2,12))

