
# now lets see built in error checker: Call stack

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()

# Traceback (most recent call last):
  # File "C:\Users\qq417\Desktop\Python\Python2021\errorchecking.py", line 138, in <module>
    # main()
  # File "C:\Users\qq417\Desktop\Python\Python2021\errorchecking.py", line 136, in main
    # bar('0')
  # File "C:\Users\qq417\Desktop\Python\Python2021\errorchecking.py", line 133, in bar
    # return foo(s) * 2
  # File "C:\Users\qq417\Desktop\Python\Python2021\errorchecking.py", line 130, in foo
    # return 10 / int(s)
# ZeroDivisionError: division by zero

# division by zero is the ultimate error
