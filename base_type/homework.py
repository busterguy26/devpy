"""
This is a list of functions that should be completed.
"""

from typing import Any, Dict
from typing import List
import string

class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    return first == second


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """

    return id(first) == id(second)


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """

    if isinstance(first_value, int) == isinstance(second_value, int):
        return first_value * second_value
    else:
        raise ValueError("Wrong Value!")


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        ValueError

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    if isinstance(int(first_value), int) == isinstance(int(second_value), int):
        return int(first_value) * int(second_value)
    else:
        raise ValueError("Invalid data")


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
    try:
        return bool(word in text)
    except ValueError:
        print("Invalid data!")


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    return [x for x in range(13) if x != 6 and x != 7]


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([2, 5, -7, 8, -1])
        >>> [2, 5, 8]
    """

    return [x for x in data if x > 0]


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    # Const
    ALPHABET = list(string.ascii_lowercase)

    return {x: ALPHABET[x - 1] for x in range(1, len(ALPHABET)+1)}


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """

    comparison_list = []
    list5 = []
    double_number_list = []
    remove_double_val_num_list = []
    sorted_list = []
    index_sort_dict = {}

    # проверка список на ошибки значений и их перевод если это возможно

    if isinstance(data, list):
        for i in data:
            if isinstance(i, int):
                print()
            else:
                raise TypeError()

    # Рабочая программа
    for k in data:
        # создание списка значений с исключением проверяемого значение
        for v in data[:data.index(k)]:
            comparison_list.append(v)
        for v in data[data.index(k) + 1:]:
            comparison_list.append(v)
        # добавление дубликатов в отдельный список
        if k in comparison_list:
            if k in double_number_list:
                index = double_number_list.index(k)
                double_number_list.insert(index, k)
            else:
                double_number_list.append(k)
                remove_double_val_num_list.append(k)  # добавление одного значения для дальнейшего удаления

        # print("Значение: ", k)
        # print(comparison_list)

        for v in comparison_list:
            if k < v:
                list5.append(v)
        index_sort_dict[len(list5)] = k
        list5.clear()

        comparison_list.clear()

    i = 0
    while i in range(len(data)):
        if i in index_sort_dict:
            sorted_list.append(index_sort_dict[i])
            i += 1
        else:
            i += 1

    # удаление одного значения со списка дупликата, так как он содержится в sorted_list
    for v in remove_double_val_num_list:
        double_number_list.remove(v)

    for n in sorted_list:
        if n in double_number_list:
            double_number_list.remove(n)  # удаление одного значения со списка дупликата
            index = sorted_list.index(n)  # добавление одного значения со списка дупликата в sorted_list
            sorted_list.insert(index, n)

    sorted_list = sorted_list[::-1]  # sorted_list в порядке возрастания

    return sorted_list
