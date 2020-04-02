"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


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

    if type(first_value) == type(second_value):
        a = first_value * second_value
        return int(a)
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
    if type(int(first_value)) == type(int(second_value)):
        a = int(first_value) * int(second_value)
        return a
    else:
        raise ValueError("Inavalid data")


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

    if isinstance(str(word), str) == isinstance(text, str):
        if word in text:
            return True
        else:
            print(word + " not in " + text + "!")
            return False
    else:
        raise ValueError("Invalid data")


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """

    some_list = []
    i = 0
    while i <= 12:
        if i != 6 and i != 7:
            some_list.append(i)
        i += 1
    return some_list


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([2, 5, -7, 8, -1])
        >>> [2, 5, 8]
    """
    negative_num_list = []
    positive_num_list = []
    new_data = data[:]

    for i in data:
        if i > 0:
            positive_num_list.append(i)
            new_data.remove(i)
        else:
            negative_num_list.append(i)

    return positive_num_list


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    # Const
    ALFABET: str = "abcdefghijklmnopqrstuvwxyz"
    # Dict
    dict_my = {}
    i = 0
    for i in range(len(ALFABET)):
        dict_my[i + 1] = ALFABET[i]
    return dict_my


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    List_copy = []
    comparison_list = []
    list5 = []
    double_number_list = []
    remove_double_val_num_list = []
    sorted_list = []
    index_sort_dict = {}

    # проверка список на ошибки значений и их перевод если это возможно

    if isinstance(List, list):
        for i in List:
            if isinstance(i, int):
                print()
            else:
                # raise ValueError("У вас ошибка в данных значений списка!")
                raise TypeError()
    # elif not isinstance(List, list):
    # for i in range(len(List)):
    # List_copy.append(i)
    # List = List_copy[:]

    # raise Exception("Ваши данные не являются списком!")
    # else:
    # raise TypeError()
    # print(List)

    # Рабочая программа
    for k in List:
        # создание списка значений с исключением проверяемого значение
        for v in List[:List.index(k)]:
            comparison_list.append(v)
        for v in List[List.index(k) + 1:]:
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
                print("Число большее чем", k, "равно:", v)
                list5.append(v)
        # print("Значение ", v)
        # print("Содержит", len(list5), "значение в списке: ", list5)
        index_sort_dict[len(list5)] = k
        list5.clear()
        # Поиск максимального значения раскрыть комментарий
        """
        list6 = list5[:]
        if not list6:
            max_value = k
            print("Max: ", max_value)
        list6.clear()    
        """

        comparison_list.clear()

    # print("Всего в словаре: ", len(index_sort_dict))

    i = 0
    while i in range(len(List)):
        if i in index_sort_dict:
            sorted_list.append(index_sort_dict[i])
            print(index_sort_dict)
            print(sorted_list)
            i += 1
        else:
            i += 1

    print(sorted_list)

    # print("remove_double_val_num_list",remove_double_val_num_list)
    # print("Дупликаты: ", double_number_list)
    # удаление одного значения со списка дупликата, так как он содержится в sorted_list
    for v in remove_double_val_num_list:
        double_number_list.remove(v)

    for n in sorted_list:
        if n in double_number_list:
            double_number_list.remove(n)  # удаление одного значения со списка дупликата
            index = sorted_list.index(n)  # добавление одного значения со списка дупликата в sorted_list
            # print(n, "индекс которого ", index)
            sorted_list.insert(index, n)

        # else:
        # print(n)

    sorted_list = sorted_list[::-1]  # sorted_list в порядке возрастания

    return sorted_list
