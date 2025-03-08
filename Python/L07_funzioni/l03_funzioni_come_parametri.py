


def media ( n , *nums):
    m = n 
    for num in nums:
        m += num
    return round (m / (len(nums)+1), 2 )

print (media(5,6,7,8,9,1))


def calcola (f, n, *nums):
    return f(n,*nums)

print (calcola(media,5,6,7,8,9,1 ))
