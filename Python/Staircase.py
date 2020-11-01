'''
This code is a solution to hackerrank's staircase generator problem.
Example input:
4
Example output:
   #
  ##
 ###
####
Generate a triangle generator with the base and height being the same as the input.
'''
n = int(input('Enter N value for your triangle '))
def staircase(n):
    n = n+1
    for i in range(1,n):
        spaces = (n-i)-1
        print(' '*spaces+'#'*i)
staircase(n)