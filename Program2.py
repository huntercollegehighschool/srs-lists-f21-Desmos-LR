'''
*********
PROGRAM 2
*********
Define a function odd_reverse that takes a list as an argument. The function creates a new list containing only the elements in the odd indices (indices 1, 3, 5, ...) and then reverses it. The function returns that list.
'''
def odd_reverse(lst):
  newlst=[]
  i=0
  for integer in lst:
    if lst.index(integer) %2 !=0:
      newlst.append(lst[-i-1])
    else:
      newlst.append(integer)
    i+=1
  return newlst
  
