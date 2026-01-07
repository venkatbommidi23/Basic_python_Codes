https://leetcode.com/problems/number-of-common-factors/
 
#For calculating common factors we need to get the gcd of 2numbers and then run a loop untill the sqrt of gcd because
#we get factors in pairs

#Find gcd(a, b) and count its divisors up to √gcd.

import math
class Solution(object):
    def commonFactors(self, a, b):
        def gcd(a,b): #euclidean algorithm
            while b:
                a,b=b,a%b
            return a    
        g=gcd(a,b)
        #g=math.gcd(a,b)  #we can simply get gcd using this math operation
        count=0
        for i in range(1,int(math.sqrt(g))+1):
            if g%i==0:  #if i divides g means i is a factor
                count+=1
                if i!=g//i:  #we check this because when g is a perfect sqaure we avoid counting twice
                    count+=1
        return count
#Time-O(sqrt(gcd(a,b))
#Space-O(1)
