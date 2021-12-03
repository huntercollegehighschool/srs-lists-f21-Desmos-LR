'''
*********
PROGRAM 1
*********
Define a function number_of_odds that takes a list of integers as an argument. The function returns how an integer, how many odd numbers are in the list.
'''
def number_of_odds(lst):
  x=0
  for integer in lst:
    if integer%2!=0:
      x+=1
  return (x)

