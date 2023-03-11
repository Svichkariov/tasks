'''
Задание 2.
Коллекции.
Примечание: входные параметры ни в однй из задач не должны быть модифицированы.
'''

from typing import Any, Dict, Iterable, List, Tuple
import copy


# Сконструировать и вернуть список из переданных аргументов.
def build_list_from_args(*args) -> List:
    return list(args)



# Сконструировать и вернуть список из переданных аргументов, имеющих тип int.
def build_int_list_from_args(*args) -> List[int]:
    return [x for x in args if isinstance(x, int)]



# Сконструировать и вернуть список из переданных аргументов, имеющих заданный тип.
def build_list_from_args_using_type(argument_type: type, *args) -> List:
    return [x for x in args if isinstance(x, argument_type)]




# Сконструировать и вернуть список из переданных аргументов, тип которых входит в заданное множество.
# Для более эффективной работы преобразовать `argument_types` в `set`.
def build_list_from_args_using_type_set(argument_types: Iterable, *args) -> List:
    return [x for x in args if type(x) in set(argument_types)]




# Сконструировать и вернуть список из двух списков, переданных в качестве аргументов.
def build_list_from_two_lists(first: List, second: List) -> List:
    return first + second




# Сконструировать и вернуть список из неограниченного числа списков, переданных в качестве аргументов.
def build_list_from_list_args(*lists) -> List:
    my_list = []
    for list_ in lists:
        my_list.extend(list_)
    return my_list



# Сконструировать список из заданного элемента и значения длины (использовать умножение).
def build_list_from_value_and_length(value: Any, length: int) -> List:
    return [copy.deepcopy(value)] * length




# Удалить из списка заданный элемент.
def remove_value_from_list(values: List, value_to_remove: Any) -> List:
    final_list = values.copy()
    while True:
        try:
            final_list.remove(value_to_remove)
        except ValueError:
            break
    return final_list



# Удалить из списка заданный элемент, используя comprehension expression [... for .. in ...].
def remove_value_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [value for value in values if value != value_to_remove]




# Удалить из списка заданный элемент, используя `filter` и lambda-функцию.
def remove_value_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    return list(filter(lambda x: x != value_to_remove, values))



# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list(values: List, values_to_remove: Iterable) -> List:
    return [value for value in values if value not in set(values_to_remove)]



# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list_using_comprehension(values: List, values_to_remove: Any) -> List:
    return [value for value in values if value not in set(values_to_remove)]




# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
# Использовать `filter` и lambda-функцию.
def remove_values_from_list_using_filter(values: List, values_to_remove: Any) -> List:
    return list(filter(lambda value: value not in set(values_to_remove), values))



# Удалить из списка дублирующиеся значения (использовать преобразование в `set` и обратно).
def remove_duplicates_from_list(values: List) -> List:
    return list(set(values))



# Создать и вернуть словарь из заданного набора именованных аргументов, значения которых имеют тип int.
def build_dict_from_named_arguments_of_type_int(**kwargs) -> Dict:
    return {key: value for key, value in kwargs.items() if isinstance(value, int)}



# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)



# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - значение по-умолчанию.
def build_dict_from_keys_and_default(values: Iterable, default: Any) -> Dict:
    return {value: copy.copy(default) for value in values}



# Создать и вернуть словарь, ключами которого являются индексы элементов,
# а значениями - значения элементов iterable параметров (использовать enumerate и dict comprehension).
def build_dict_from_indexed_values(values: Iterable) -> Dict:
    return dict(enumerate(values))



# Создать и вернуть словарь, собранный на основе списка пар ключ-значение.
def build_dict_from_key_value_pairs(kws: List[Tuple]) -> Dict:
    return dict(kws)


# Создать и вернуть словарь, собранный из двух списков, один из которых
# содержит ключ, а второй - соответствующее значение (использовать zip).
def build_dict_from_two_lists(keys: List, values: List) -> Dict:
    return dict(zip(keys, values))



# Сформировать из двух словарей и вернуть его. В случае, если ключи совпадают,
# использовать значение из второго словаря (dict.update).
def build_dict_using_update(first: Dict, second: Dict) -> Dict:
    my_dict = copy.copy(first)
    my_dict.update(second)
    return my_dict



# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Заменить значение в случае совпадения ключей.
def update_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    my_dict = copy.copy(dictionary)
    my_dict.update(kwargs)
    return my_dict



# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Объединить значения в список в случае совпадения ключей.
def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    my_dict = copy.copy(dictionary)
    for key, value in kwargs.items():
        if key in my_dict.keys():
            if not isinstance(my_dict[key], list):
                my_dict[key] = [my_dict[key]]
            my_dict[key] = my_dict[key] + kwargs[key] if isinstance(kwargs[key], list) else my_dict[key] + [kwargs[key]]
        else:
            my_dict[key] = kwargs[key]
    return my_dict



# Объединить два словарь и вернуть результат.
# Объединить значения в список в случае совпадения ключей.
def merge_two_dicts(first: Dict, second: Dict) -> Dict:
    my_first_dict = copy.copy(first)
    for key in second.keys():
        if key in my_first_dict.keys():
            if not isinstance(my_first_dict[key], list):
                my_first_dict[key] = [my_first_dict[key]]
            my_first_dict[key] = my_first_dict[key] + second[key] if isinstance(second[key], list)\
                else my_first_dict[key] + [second[key]]
        else:
            my_first_dict[key] = second[key]
    return my_first_dict



# Объединить два словарь и вернуть результат.
# В случае совпадения ключей:
# - объединить значения рекурсивно, если оба значения - словари;
# - объединить значения в один список, если оба значения - списки;
# - объединить значения в одно множество, если оба значения - множества;
# - объединить значения в список в любом другом случае.
def deep_merge_two_dicts(first: Dict, second: Dict) -> Dict:
    my_first_list = copy.copy(first)
    for key in second.keys():
        if key in first.keys():
            if isinstance(first[key], list) and isinstance(second[key], list):
                my_first_list[key].extend(second[key])
            elif isinstance(first[key], set) and isinstance(second[key], set):
                my_first_list[key] = my_first_list[key] | (second[key])
            elif isinstance(first[key], dict) and isinstance(second[key], dict):
                my_first_list[key] = deep_merge_two_dicts(my_first_list[key], second[key])
            else:
                if not isinstance(my_first_list[key], list):
                    my_first_list[key] = [my_first_list[key]]
                my_first_list[key] = my_first_list[key] + second[key] if isinstance(second[key], list) \
                    else my_first_list[key] + [second[key]]
        else:
            my_first_list[key] = second[key]
    return my_first_list



# Вернуть список, состоящий из ключей, принадлежащих словарю.
def get_keys(dictionary: Dict) -> List:
    return list(dictionary.keys())



# Вернуть список, состоящий из значений, принадлежащих словарю.
def get_values(dictionary: Dict) -> List:
    return list(dictionary.values())



# Вернуть список, состоящий из пар ключ-значение, принадлежащих словарю.
def get_key_value_pairs(dictionary: Dict) -> List[Tuple]:
    return list(dictionary.items())



# Реверсировать и вернуть словарь.
def reverse_dict(dictionary: Dict) -> Dict:
    return dict(reversed(dictionary.items()))



# Удалить из словаря элементы, имеющие пустые значения (None, '', [], {}).
def clear_dummy_elements(dictionary: Dict) -> Dict:
    return {key: value for key, value in dictionary.items() if value not in [None, "", [], {}]}



# Удалить из словаря дублирующиеся и пустые элементы.
def clear_dummy_and_duplicate_elements(dictionary: Dict) -> Dict:
    my_dict = {}
    for key, value in dictionary.items():
        if (value not in [None, "", [], {}]) and value not in my_dict.values():
            my_dict[key] = value
    return my_dict



# Обменять в словаре ключи и значения (в качестве значений могут выступать только неизменяемые значения).
def swap_dict_keys_and_values(dictionary: Dict) -> Dict:
    return {value: key for key, value in dictionary.items()}



# Вернуть словарь, отсортированный по ключу. Ключи могут иметь только тип int.
def sort_dict_with_int_keys(dictionary: Dict) -> Dict:
    return dict(sorted(dictionary.items()))



# Вернуть словарь, отсортированный по ключу в обратном порядке. Ключи могут иметь только тип int.
def sort_dict_backward_with_int_keys(dictionary: Dict) -> Dict:
    return dict(sorted(dictionary.items(), reverse=True))



# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
def group_dict_elements_by_key_type(dictionary: Dict) -> Dict:
    my_float_list = [pair for pair in dictionary.items() if isinstance(pair[0], float)]
    my_int_list = [pair for pair in dictionary.items() if isinstance(pair[0], int)]
    my_str_list = [pair for pair in dictionary.items() if isinstance(pair[0], str)]
    return dict(sorted(my_int_list, key=lambda x: int(x[0]))
                + sorted(my_float_list, key=lambda x: float(x[0]))
                + sorted(my_str_list, key=lambda x: ord(x[0])))



# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
# Внутри каждой из групп отсортировать элементы по значениям ключа в обратном порядке.
def group_dict_elements_by_key_type_and_sort(dictionary: Dict) -> Dict:
    my_float_list = [pair for pair in dictionary.items() if isinstance(pair[0], float)]
    my_int_list = [pair for pair in dictionary.items() if isinstance(pair[0], int)]
    my_str_list = [pair for pair in dictionary.items() if isinstance(pair[0], str)]
    return dict(sorted(my_int_list, key=lambda x: int(x[0]), reverse=True)
                + sorted(my_float_list, key=lambda x: float(x[0]), reverse=True)
                + sorted(my_str_list, key=lambda x: ord(x[0]), reverse=True))



# Подсчитать количество элементов словаря, имеющих числовой тип, значение которых находится
# в интервале [-10, 25].
def count_dict_elements(dictionary: Dict) -> int:
    return sum(1 for value in dictionary.values() if type(value) in (int, float) and 25 > value > -10)



# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_lists(keys: List, values: List) -> Dict:
    my_dict = dict(zip(keys, values + [None] * (len(keys) - len(values))))
    return my_dict



# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение, заданное по-умолчанию.
def build_dict_from_two_unaligned_lists_and_default(keys: List, values: List, default: Any) -> Dict:
    return dict(zip(keys, values + list(map(copy.copy, [default] * (len(keys) - len(values))))))



# Построить и возвратить словарь из двух iterable объектов. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_iterables(keys: Iterable, values: Iterable) -> Dict:
    my_dict = dict.fromkeys(keys)
    my_dict_2 = dict(zip(my_dict, values))
    my_dict.update(my_dict_2)
    return my_dict
