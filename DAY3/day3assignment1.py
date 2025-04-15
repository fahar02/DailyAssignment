'''
flatten(lst)       
Flattens the list ie input = [1,2,3, [1,2,3,[3,4],2]]
output = [1,2,3,1,2,3,3,4,2]
'''
#input data = [1,2,3, [1,2,3,[3,4],2]]
#output data=[1, 2, 3, 1, 2, 3, 3, 4, 2]

#function defination for flattens
def flattens(input):
    temp=[]
    #using this type *args and sliceing that to get output
    for i in input:
        if isinstance(i,list):
            temp.extend(flattens(i))
        else:
            temp.append(i)
    return temp
    
if __name__=='__main__':
    #input data
    input = [1,2,3, [1,2,3,[3,4],2]]
    
    #function call 
    result=flattens(input)
    print(result)
    #output=[1, 2, 3, 1, 2, 3, 3, 4, 2]
    #conclusion=using slicing to store the elements
