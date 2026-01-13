 #We can do using prime factorization but 
#Time -O(sqrt(a)+sqrt(b))--SLow for big numbers
#Space-O(no of prime factors)


#HCF is calculated using Euclidean algorithm; LCM is derived using LCM = (a×b)/HCF.

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        def gcd(a,b):
            while(b):
               a,b=b,a%b
            return a
        hcf=gcd(a,b)
        return [a*b//hcf,hcf]
    
    #Time-O(log(min(a,b)))---O(logn)
    #Space-O(1)
