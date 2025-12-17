#https://www.geeksforgeeks.org/problems/reversing-the-equation2205/1

#input:
# S = "20-3+5*2"
# Output: 2*5+3-20
# Explanation: The equation is reversed with
# numbers remaining the same.


class Solution:
    def reverseEqn(self, s):
        i=0
        token=[]
        n=len(s)
        
        #Traverse entire string
        while i<n:
            #To form multidigit number
            if '0'<=s[i]<='9':
                nums=""
                
                #To store continuous number
                while i<n and '0'<=s[i]<='9':
                    nums+=s[i]
                    i+=1
                #add full number into token
                token.append(nums)
            #To store operators
            else:
                token.append(s[i])
                i+=1
                
        #Reversing the token and converting into string
        return "".join(token[::-1])

        
        #Time Complexity-O(n)
        #Space Complexity-O(n)
