# What is PyTools?
PyTools is a very simple but very useful tool for python developers.
It forces methods to have strict types as it is in eg. java.

# Warning
This project is almost 2 years old and in no longer under development.

# Installation
`git clone https://github.com/AdvancedAntiSkid/PyTools/blob/master/pytools.py wherever-you-want`

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
buy_stuff("John Doe", 123456789, "your@domain.com", True)
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
```
#### Results
```py
calculate_square(2, 3):
>> prints '6'

has_knowledge_in("Javascript")
>> error
```

## NonNull
'NonNull' is like Returns(everithing except None), so it raises an error when the function returns None
#### Example
```py
@CallTracker
@NonNull
def order_pizza(type, amount):
  return "ordered"

@CallTracker
@NonNull
def get_user(username, userid):
  return None
 ```
 #### Results
 ```py
 order_pizza("Margareta", 1)
 >> returns 'ordered'
 
 get_user("Username123", 987654321):
 >> error
 ```

#### Warning
You can not use 'Returns' and 'NonNull' in the same function
