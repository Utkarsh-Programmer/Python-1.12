from typing import List, Tuple, Dict, Union
# Here, type of variables are signified while declaration.
# it helps when we type `variable_name.` it shows all the methods available for that particular data type.
num: int = 5
name: str = "Harry"


# Here, this function take 'a' and 'b' as integer and return the output as integer.
def sum(a: int, b: int) -> int:
    return a+b


# Advanced type hints...
# list of integers
numbers: List[int] = [1, 2, 3, 4,  5]

# tuple of string and integer
person: Tuple[str, int] = ("Alice",  30)

# dictionary with string keys and integer values
scores: Dict[str, int] = [{"Alice": 90, "Bob": 5}]

# union type for variables that can store multiple data types
identifier: Union[str, int] = "ID123"
