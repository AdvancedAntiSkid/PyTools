# What is PyTools?
PyTools is a very simple but very useful tool for python developers

# Installation
`git clone https://github.com/TheInfiniteCode001/PyTools/blob/master/pytools.py wherever-you-want`

# Usage
## CallTracker
Basically it doesn't do anything by itself, but it is required to other functions

## RequireArgs
'RequireArgs' is checking when the function gets called and passes the certain argument types
#### Example
```py
@CallTracker
@RequireArgs([str, int, str, bool])
def buy_stuff(name, phone, email, has_creditcard):
  print("success")
```
#### Results
```py
buy_stuff("Bill Gates", 123456789, "your@domain.com", True)
>> prints 'success'

buy_stuff("12345678", True, "your@domain.com")
>> error
```
## Returns
'Returns' forces the function to return the certain type of variable
#### Example
```py
@CallTracker
@Returns(int)
def calculate_square(x, y):
  return x * y
  
@CallTracker
@Returns(int)
def has_knowledge_in(topic):
  return True
˙˙`
## Results
```py
calculate_square(2, 3):
>> prints '6'

has_knowledge_in("Javascript")
>> error
```
```
