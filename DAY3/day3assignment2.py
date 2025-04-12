'''
Question-13              
convert(x) Converts like below 
input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]
i[0] [[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]
i[0][0][ '(0,1,2)' , '(3,4,5)']
i[0][1]['(5,6,7)' , '(9,4,2)']
i[0][0][0] '(0,1,2)'
i[0][0][1] '(3,4,5)'
i[0][1][0] '(5,6,7)'
i[0][1][1]  '(9,4,2)'
there are many ways to perform the assignment but is use to nested for loop
to have good undersanting of fundamental concepts
'''
#function defination for converts
def Converts(input):
    final=[]
    for i in input:
        temp1=[]
        for j in i:
            temp2=[]
            for k in j:
                if k.isdigit():
                    temp2.append(int(k))
            temp1.append(temp2)
        final.append(temp1)
    return [final]
    

if __name__=='__main__':
    #input data
    input=[[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
    
    print(input)
    
    #function call 
    result=Converts(input[0])
    print(result)
    #output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]
    #conclusion=using nested for loop