import regex
import sys

name = sys.argv[1:]

if not name: name = 'test.c'
else: name = name[0]

tf = open (name, 'r')
ft = tf.read()
tf.close()

m = regex.search ('{((?:[^{}]|(?R))*)}', ft)
print (m.group())
