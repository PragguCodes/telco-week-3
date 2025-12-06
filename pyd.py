from typing import Annotated, List
from annotated_types import Gt, Len, Predicate

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class MyClass:
    # Age must be > 18
    age: Annotated[int, Gt(18)]

    # factors must be a list of integers AND each integer must be prime
    factors: List[Annotated[int, Predicate(is_prime)]]

    # my_list must be a list of integers with length between 0 and 10
    my_list: Annotated[List[int], Len(0, 10)]

# Valid
valid_age = 25
valid_factors = [2, 3, 5, 7]
valid_list = [1, 2, 3]
# Invalid
invalid_age = 15
invalid_factors = [4, 6, 9]
invalid_list = list(range(20))
