import types
import functools
import asyncio

def NonNull(func):
    @functools.wraps(func)
    def wrapper(*args):
        wrapper.has_been_called = True
        to_return = func(*args)
        if to_return != None:
            return to_return
        raise Exception("Method have to not return NoneType object!")
    wrapper.has_been_called = False
    return wrapper 

__returns = []

class ReturnsType:
    def __init__(self, func, objtype):
        self.func = func
        self.objtype = objtype

def add_returns(func, objtype):
    __returns.append(ReturnsType(func, objtype))

def run_returns(func, objtype):
    for rtype in __returns:
        if rtype.func == func:
            if not rtype.objtype == objtype:
                raise Exception("Method didn't pass the required return type! declared:", rtype.objtype, "given:", objtype)

__calls = []

class Call:
    def __init__(self, func, action):
        self.func = func
        self.action = action

def add_call_result(func, action):
    __calls.append(Call(func, action))
    
def run_call(func):
    for call in __calls:
        if call.func == func:
            try:
                call.action()
            except Exception as error:
                print(error)

__reqargs = []

class ReqArgs:
    def __init__(self, func, args):
        self.func = func
        self.args = args

def add_reqargs_check(func, args):
    __reqargs.append(ReqArgs(func, args))

def run_reqarg(func, args):
    args = list(args)
    for reqarg in __reqargs:
        if reqarg.func == func:
            args_check(reqarg.args, to_types(args))

def args_check(declared: list, given: list) -> bool:
    if len(declared) == len(given):
        for i in range(0, len(declared)):
            if not declared[i] == given[i]:
                raise Exception("Invalid parameters! declared:", declared, "given:", given)
        return True
    raise Exception("Invalid parameters length")

def to_types(args: list) -> list:
    newlist = []
    for arg in args:
        newlist.append(type(arg))
    return newlist

def CallTracker(func):
    @functools.wraps(func)
    def wrapper(*args):
        wrapper.has_been_called = True
        to_return = func(*args)
        run_call(func)
        run_returns(func, type(to_return))
        if(len(args) > 0):
            run_reqarg(func, list(args))
        return to_return
    wrapper.has_been_called = False
    return wrapper

class CallResult(object):
    def __init__(self, action):
        self.action = action
    def __call__(self, method):
        add_call_result(method, self.action)
        return method

class RequireArgs(object):
    def __init__(self, args: list):
        self.args = args
    def __call__(self, method):
        add_reqargs_check(method, self.args)
        return method

class Returns(object):
    def __init__(self, objtype):
        self.objtype = objtype
    def __call__(self, method):
        add_returns(method, self.objtype)
        return method

def runAsnyc(method, *args):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(method(*args))
    loop.close()
    
def null():
    pass
