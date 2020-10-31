from typing import List

def demo_function(x: int, y: List[str]) -> None:
    """Print the integer and items in the list

    Args: 
    x: an integer
    y: List of string
    """
    print(f"The input integer is: {x}")
    for idx, word in enumerate(y):
        print(idx, word)

def sum(a: int, b: int) -> int:
    """Apply addition to two numbers
    
    Args:
    a: an integer
    b: an integer 
    """
    # return True
    return a+b