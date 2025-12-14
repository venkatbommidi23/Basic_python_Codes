import math
class Solution:
    def isPrime(self, n):
        if n<2:
            return False
        if n==2:
            return True
        if n%2==0:
            return False
  
        #Why only upto sqrt(n) because any non-prime number will have factor <=sqrt(n)
        #eg:n=36 (1,36) (2,18) (3,12) (4,9) (6,6) after this the factors start repeating
        #a*b one is <=sqrt(n) and other is >=sqrt(n)
      
        sqrt=int(math.sqrt(n))
        for i in range(3,sqrt+1,2):
            if n%i==0:
                return False
        return True

        #Time-O(srqt(n))
        #Space-O(1)
