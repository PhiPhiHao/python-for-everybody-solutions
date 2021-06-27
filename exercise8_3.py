#!/usr/bin/env python3
"""
Exercise  8.3: Rewrite the guardian code in the above example without two if
statements. Instead, use a compound logical expression using the and logical
operator with a single if statement.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


fhand = open('exercise8_2.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])

"""or use Demogen Logical law to use 'and' logical operator in the code"""

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    # print("Debug:",words)
    if not( not (len(words)< 3) and  words[0] == 'From' ): 
        continue
    #change the satement from : if len(words) < 3 or words[0] != 'From': continue
    #to :if not( not (len(words)< 3) and  words[0] == 'From' ): continue
    #because Demogen Law :~(A or B) == (~A)and(~B)
    #A or B == ~((~A)and(~B))
    print(words[2])
