#!/usr/bin/python

# Set
s1 = set([8, 2, 5])
s2 = set([2, 8])
s3 = set([2, 5, 8])

print "set 1:", s1
for i in s1:
    print i

print "set 2:", s2
for i in s2:
    print i

print "set 3:", s3
for i in s3:
    print i

# Teilmenge, echte Teilmenge

if s2 < s1:
    print "s2 ist echte Teilmenge von s1"
if s3 <= s1:
    print "s3 ist Teilmenge von s1"
