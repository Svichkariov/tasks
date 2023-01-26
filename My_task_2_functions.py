# Реализовать функцию, которая принимает форму и возвращает ее в обратном порядке.
def rev (value):
    return value[::-1]

# Реализовать функцию, которая принимает два параметра: число и степень - и возвращает это число,
# сложное в степени.
# В случае, если степень не задана пользователем, используется значение 2.0.
def square (number, degree=2):
    return number ** degree

# Реализовать функцию, которая принимает стандартный набор значений и возвращает кортеж,
# Типы передаваемых параметров.

def tpl(*args):
    a = []
    for i in args:
        a.append(type(i))
    result = tuple(a)
    return result

# Реализовать функцию, которая принимает произвольный набор именных параметров и возвращает их
# группировка параметров в видео словаря.
# Например, если заданы входные параметры как `a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0`,
# то необходимо вернуть словарь такого вида:
# {
# int: [['a', 34], ['c', 2]],
# str: [['b', 'какой-то текст']],
# float: [['d', 1.3], ['f', -3.0]],
# дикт: [['е', {1: 2}]]
# }
def sort_type(**dict_):
    lst={}
    for i in dict_.values():
        lst.setdefault(type(i),[])

    for k in lst:
        for j in dict_.keys():
            if k == type(dict_[j]):
                lst[k].append([j,dict_[j]])
    return lst

print(sort_type(a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0))


# Реализовать функцию, которая принимает строку и произвольный набор неименованных и именованных параметров.
# Строка может содержать произвольный набор подстрок вида **, *index* или *name*.
# Вместо ** в строку должен быть подставлен символ *.
# Вместо *index* должен быть подставлен неименованный параметр с индексом index. Должна поддерживаться
# отрицательная индексация.
# Вместо *name* должен быть подставлен именованный параметр с именем name.

def replacement(str_, *args, **kwargs):
    st = str_.replace('**', '*')
    li = list(kwargs)
    ansver_lst = []
    for i in st.split():
        if i[0] == i[-1]:
            if li[0] == i[1:-1]:
                i = kwargs[f'{li[0]}']
            elif li[1] == i[1:-1]:
                i = kwargs[f'{li[1]}']

        if type(i) == str and len(i) != 1 and i[0] == '*':
            index = int(i[1])
            i = args[index]

        ansver_lst.append(i)

    ansver = ' '.join(str(x) for x in ansver_lst)
    return ansver


print(replacement('Some *first* string ** to be formatted *1* *first* *second* *0* *2*', 111, 'string', '!!!', first=5,
                  second=7, ))
