class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        summ=nums[0]+nums[1]+nums[2]
        
        for i in range(0,len(nums)-1):
            
            if(i>0 and nums[i]==nums[i-1]):
                continue
                
            l,r=i+1,len(nums)-1
            
            while(l<r):
                
                sumNow=nums[i]+nums[l]+nums[r]
                
                if(abs(target-summ)>abs(target-sumNow)):
                    summ=sumNow
                else:
                    pass
                
                if(sumNow>target):
                    r-=1
                else:
                    l+=1
                    
                
        return summ
    
    #Run time= O(n^2)
    #Number of times solved this problem-- Once
        













































                                                                                                                        1. Buenas tardes, me llamo Yeabkal. 
                                                                                                                        2. Soy de Cuba. 
                                                                                                                        3. voy a la universidad de connecticut.
                                                                                                                        4. me gusta la informática y las matemáticas
                                                                                                                            Tengo cuatro clases
                                                                                                                            esta es mi primera vez aprendiendo-
                                                                                                                        español

                                                                                                                        5. me gusta jugar futbol y al musica
                                                                                                                        7. me gusta escuchar a bob marley
                                                                                                                        8. los fines de semana me gusta pasar -
                                                                                                                            el tiempo con mis amigos y estudiar en la biblioteca.

                                                                                                                        10. me gusta ir al gimnasio
                                                                                                                        11. no me gusta la política
                                                                                                                        12. Soy inteligente y al paciente
                                                                                                                        13. No soy pessimista
                                                                                                                        14. Estoy sano
                                                                                                                        15. tengo una hermana y al un perro
                                                                                                                        17. el nombre de mi perro es Django -
                                                                                                                            y de mi hermana es kebron

                                                                                                                            amo los dos
                                                                                                                        18.  El nombre de mi mejor amigo es John
                                                                                                                        20. Nuestra profesora de español-
                                                                                                                            es hermosa
