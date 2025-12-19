#https://leetcode.com/problems/count-primes/

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

#Sieve of Eratosthenes

import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        prime=[True]*n
        prime[0]=prime[1]=False
        
        for j in range(2,math.isqrt(n)+1):
            if prime[j]: #if prime[j]==True:
                for k in range(j*j,n,j):
                    prime[k]=False
        return sum(prime)

  #Time complexity-O(n log logn)----Sieve runs in O(n log log n) because each prime p marks n/p numbers, and the sum of reciprocals of primes up to n is log log n.
  #Space Complexity-O(n)
