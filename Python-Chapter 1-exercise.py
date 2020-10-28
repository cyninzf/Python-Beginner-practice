Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Hello ():
	print("hello")
	print ("Computers are fund!")

	
>>> hello ()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    hello ()
NameError: name 'hello' is not defined
>>> hello ()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    hello ()
NameError: name 'hello' is not defined
>>> hello()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    hello()
NameError: name 'hello' is not defined
>>> Hello()
hello
Computers are fund!
>>> Hello ()
hello
Computers are fund!
>>> def hello():
	print("Hello")
	Print("Computers are fun!")

	
>>> hello()
Hello
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    hello()
  File "<pyshell#13>", line 3, in hello
    Print("Computers are fun!")
NameError: name 'Print' is not defined
>>> Hello()
hello
Computers are fund!
>>> def hello2():
	print("Hello")
	Print("Computers are fun!")

	
>>> hello2()
Hello
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    hello2()
  File "<pyshell#17>", line 3, in hello2
    Print("Computers are fun!")
NameError: name 'Print' is not defined
>>> def hello2 ():
	print ("Hello")
	print (Computers are fun!")
	       
SyntaxError: invalid syntax
>>> 
>>> def hello2():
	print ("Hello")
	print ("Computers are fun!")

	
>>> hello2()
Hello
Computers are fun!
>>> 