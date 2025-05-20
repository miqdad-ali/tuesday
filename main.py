# THREE POINTS
def count_vowels(string: str) -> int:
    
    """
    This function takes a string input and counts the number of vowels in it.
    Your task:
    - Use a loop to iterate through each character in the string.
    - Check if the character is a vowel (a, e, i, o, u) and count it.
    - Make sure to handle capital letters.

    Example:
    count_vowels("house of balloons") -> 6
    """
    
    pass


# FIVE POINTS
def filter_even_numbers(numbers):
    """
    This function takes a list of integers `numbers` and returns a new list 
    containing only the even numbers from the original list.

    Your task:
    - Use a loop or list comprehension to filter out the even numbers.
    - Return the new list.

    Example:
    filter_even_numbers([1, 2, 3, 4, 5, 6]) → [2, 4, 6]
    """

    pass


# BONUS: TEN POINTS

def diagonal_sum(matrix: list[list[int]]) -> int:
    """
    This function takes a 2D square matrix (list of lists of integers)
    and returns the sum of the main diagonal elements.

    Parameters:
    - matrix: list[list[int]] → a square matrix of integers

    Returns:
    - int → sum of the elements on the main diagonal

    Example:
    diagonal_sum([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]) → 15
    Why? the diagonal sum is taking 1, 5 and 9.
    """