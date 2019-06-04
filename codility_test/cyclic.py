def solution(A):
    # write your code in Python 3.6
    import math

    def minimum_value(i,dg):
        j = round(math.sqrt(i))
        val =  int(math.log10(j))+1 

        if(val== 1) and (j*j == i):
            return(i)
        else:
            while(dg < 2):
                dg -=1 
                print(i)
                res = minimum_value(math.sqrt(i),dg)
                return res

    range_list = [A]
    digits = int(math.log10(A))+1 

    for i in range_list:
        print(i)
        mimum_value = (minimum_value(i,digits))
        if mimum_value**digits == i:
            return mimum_value
       

print(solution(16))



