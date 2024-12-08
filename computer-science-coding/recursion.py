# Write pseudocode for a recursive routine to find the sum of all the even numbers between 0 and n when called with an even number. Show how the subroutine would be called and the result output.

sum = 0

def evenSum(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        print(n + evenSum(n-1))
    else:
        print(evenSum(n-1))

evenSum(8)
		
			