from functools import wraps
from typing import Callable
from datetime import datetime

def logger(txtfile:str='logs.txt',
           printlog:bool=False,
           raiseexc:bool=False,
           time:bool=False,
           only_exception:bool=True
           ):
    def wrapper(func:Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            exc,res=None,None
            try:
                res=func(*args, **kwargs)
            except Exception as e:
                exc=e

            if printlog:
                if only_exception and exc :
                    print(f"Func nme:{func.__name__}"
                          f"\nargs:{args}\nkwargs:{kwargs}"
                          f"\nres:{res}"
                          f"{f'\nexc:{exc}' if exc else '' }")
            if only_exception and exc :
                with open(txtfile, 'a', encoding="utf-8") as f:
                    f.write(f"\n"
                            f"{f"\n{datetime.now()}" if time else ''}"
                            f"\nFunc nme:{func.__name__}"
                            f"\nargs:{args}"
                            f"\nkwargs:{kwargs}"
                            f"\nres:{res}"
                            f"\n{f"\n{'-'*10}\nexc:{exc}\n{'-'*10}\n" if exc else ''}")
            if exc and raiseexc: raise exc
            return res
        return inner
    return wrapper

def make_log(
        text:str="EmptyLog",
        txtfile:str='logs.txt',
        time:bool=False,
        printlog:bool=False,
):
    if printlog:
        print(f"{f"\n{datetime.now()}" if time else ''}"
                f"\n{text}")
    with open(txtfile, 'a', encoding="utf-8") as f:
        f.write(f"{f"\n{datetime.now()}" if time else ''}"
                f"\n{text}")

