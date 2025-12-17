#https://www.geeksforgeeks.org/problems/multiply-two-strings/1

# Input: s1 = "0033", s2 = "2"
# Output: "66"
# Explanation: 33 * 2 = 66

class Solution:
    def multiplyStrings(self, s1, s2):
        #checking sign
        sign=1
        if s1[0]=='-':
            sign*=-1
            s1=s1[1:]   # '-' ni remove cheyadam
        if s2[0]=='-':
            sign*=-1
            s2=s2[1:]
        
        
        #Removing leading zeros  
        s1=s1.lstrip('0')
        s2=s2.lstrip('0')
        
        #edge case 
        #if string is empty
        
        if not s1 or not s2:
            return "0"
        
        n=len(s1)
        m=len(s2)
        
        #maximum digits= n+m
        
        res=[0]*(n+m)
        
        #School multiplication
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                
                #Converting char to digit
                m1=ord(s1[i])-ord('0')
                m2=ord(s2[j])-ord('0')
                
                mul=m1*m2
              
                #Storing in correct position
                position=i+j+1
                
                #Adding current value to previous value
                total=mul+res[position]
                
                #Current digit
                res[position]=total%10
                
                #Moving carry to left side
                res[position-1]+=total//10
                
        #Skiping leading zeros     
        result=[]
        for num in res:
            if not result and num==0:
                continue
            result.append(chr(num+ord('0')))
        
        #joining digits
        final_result=''.join(result)
        
        #If negative need to add '-'
        if sign==-1:
            final_result='-' + final_result
        return final_result
        
        #Time complexity-O(N*M)
        #Space complexity-O(N+m)
        
        
                
        
            
        # code here
        
