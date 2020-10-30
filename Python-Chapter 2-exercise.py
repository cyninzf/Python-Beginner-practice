Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=5
>>> x
5
>>> print(x)
5
>>> "Bat"+"man"
'Batman'
>>> "Bat","man"
('Bat', 'man')
>>> print("bat","man")
bat man
>>> print ("bat",man)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print ("bat",man)
NameError: name 'man' is not defined
>>> print("bat","man")
bat man
>>> print(3+4)
7
>>> print(3,4,3+4)
3 4 7
>>> print()

>>> print("The answer is:", 3+4)
The answer is: 7
>>> print("bat""man")
batman
>>> print
<built-in function print>
>>> print()

>>> print ("The answer is:", end="")
The answer is:
>>> print ("The answer is:", end="") print(3+4)
SyntaxError: invalid syntax
>>> print ("The answer is:", end="")
The answer is:
>>> print(3+4)
7
>>> print ("The answer is:", end='')
The answer is:
>>> 
print ("The answer is", end=" ") print(3 + 4)
SyntaxError: invalid syntax
>>> 
print ("The answer is", end=" ")
The answer is 
>>> print ("The answer is", end=' ')
The answer is 
>>> print ("The answer is", end=':')
The answer is:
>>> print("Welcome to" , end = ' ')  
print("GeeksforGeeks", end = ' ')
Welcome to 
>>> 
>>> print("Welcome to" , end = ' ')
print("GeeksforGeeks", end = ' ')
Welcome to 
>>> print ("The answer is", end=' ')
The answer is 
>>> print (3+4)
7
>>> print ("The answer is", end=' ')
>>> print (3+4)
The answer is 
>>> 
>>> print ("The answer is", end=' '), print (3+4)
The answer is 7
(None, None)
>>> print ("The answer is", end=' '), print (3+4)
The answer is 7
(None, None)
>>> print ("The answer is", end=""), print (3+4)
The answer is7
(None, None)
>>> print ("The answer is", end=" "), print (3+4)
The answer is 7
(None, None)
>>> print ("The answer is", end=' '), print (3+4), print ("what!")
The answer is 7
what!
(None, None, None)
>>> print ("The answer is", end=' '), print (3+4), print ("what!"), print (i don't understand)
								       
SyntaxError: invalid syntax
>>> print ("The answer is", end=' '), print (3+4), print ("what!"), print ("i don't understand")
The answer is 7
what!
i don't understand
(None, None, None, None)
>>> print ("The answer is", end=' ') print (3+4)
SyntaxError: invalid syntax
>>> print ("The answer is", end=' ') Print (3+4)SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> print ("The answer is", end=' ') print (3+4)
SyntaxError: invalid syntax
>>> print ("The answer is", end=' ') print (3+4)
SyntaxError: invalid syntax
>>> print ("The answer is", end=' '),print (3+4)
The answer is 7
(None, None)
>>> 