class Solution:
    def addStrings(self, s1: str, s2: str) -> str:
        output=[]

        l1=len(s1)
        l2=len(s2)

        minLen=min(l1,l2)
        maxLen=max(l1,l2)

        excess=0
        summ=0
    
      #Take care of the sum till we runout of digits to add from the min num
        for i in range (1,minLen+1):
            summ=int(s1[-i])+int(s2[-i])+excess
            if(summ<10):
                output.append(str(summ))
                excess=0
            else:
                excess=0
                output.append((str(summ))[1])
                excess+=int((str(summ))[0])
        
        
        
        
        if(len(s1)==len(s2)):
            if(summ<10):
                output.reverse()
                return "".join(output)
            else:
                output.append(str(excess))
                output.reverse()
                return "".join(output)
                
        else:
            if(summ<10):
                excess=0
            if(len(s1)<len(s2)):
                s1=s2
        summ=0
        
        #Compute for the remaining digits of the max num
        for i in range(maxLen-minLen-1, -1, -1):
            summ=int(s1[i])+excess

            if(summ<10):
                output.append(str(summ))
                excess=0
            else:
                excess=0
                output.append((str(summ))[1])
                excess+=int(str(summ)[0])
        if(summ>=10):
            last_str=output.pop()
            correct_sum=str(excess)+last_str
            output.append(correct_sum)
        
        output.reverse()
        return "".join(output)