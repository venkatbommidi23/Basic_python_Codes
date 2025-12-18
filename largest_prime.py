#https://www.geeksforgeeks.org/problems/largest-prime-factor2601/1

# Input: n = 24
# Output: 3
# Explanation: The prime factorization of 24 is 23×3. Among the prime factors (2, 3), the largest is 3.

class Solution:
    def largestPrimeFactor(self, n):
        largest=-1
        
        #Keep dividing by 2 while n is even
        while n%2==0:
            largest=2
            n=n//2
        
        #Checking odd factors
        i=3
        #If a number has any factor greater than √n, the corresponding paired factor must be smaller than √n
        #so checking up to √n is sufficient.
        #if number does not a factor <=sqrtroot(n),then it is prime number
        while i*i<=n: #i<=sqrt(n)- because of decimal problem we right i*i<=n
            #Remove all occurences of factor i
            while n%i==0:
                n=n//i
                largest=i
            i+=2    #Move to next odd number
        
        #Remaining n is prime and greater than sqrt(original n)
        if n>1:
            largest=n
        
        return largest
            
        
        #Time Complexity-O(sqrt(n))
        #Space complexity-O(1)
    
                
