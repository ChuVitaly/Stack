
from main import Stack

def find1(a):
    brackets_str1 = Stack()
    brackets_str2 = Stack()
    for k in a:
        if k == "(":
            brackets_str1.push(k)
    for i in a:
        if i == ")":
            brackets_str2.push(i)

    if brackets_str1.size() == 0 and brackets_str2.size() == 0:
        print("Таких скобок: '(' нет в этой строке")
    elif brackets_str1.size() == 0 or brackets_str2.size() == 0:
        print("В Этой строке скобки: '(' - не сбалансированы")
    elif brackets_str1.size() / brackets_str2.size() == 1:
        print("В Этой строке скобки: '(' - сбалансированы")
    elif brackets_str1.size() / brackets_str2.size() != 1:
        print("В Этой строке скобки: '(' - не сбалансированы")


def find2(a):
    brackets_str1 = Stack()
    brackets_str2 = Stack()
    for k in a:
        if k == "[":
            brackets_str1.push(k)
    for i in a:
        if i == "]":
            brackets_str2.push(i)

    if brackets_str1.size() == 0 and brackets_str2.size() == 0:
        print("Таких скобок: '[' нет в этой строке")
    elif brackets_str1.size() == 0 or brackets_str2.size() == 0:
        print("В Этой строке скобки: '[' - не сбалансированы")
    elif brackets_str1.size() / brackets_str2.size() == 1:
        print("В Этой строке скобки: '[' - сбалансированы")
    elif brackets_str1.size() / brackets_str2.size() != 1:
        print("В Этой строке скобки: '[' - не сбалансированы")


def find3(a):
    brackets_str1 = Stack()
    brackets_str2 = Stack()
    for k in a:
        if k == "{":
            brackets_str1.push(k)
    for i in a:
        if i == "}":
            brackets_str2.push(i)

    if brackets_str1.size() == 0 and brackets_str2.size() == 0:
        print("Таких скобок: '{' нет в этой строке")
    elif brackets_str1.size() == 0 or brackets_str2.size() == 0:
        print("В Этой строке скобки: '{' - не сбалансированы")
    elif brackets_str1.size() / brackets_str2.size() == 1:
        print("В Этой строке скобки: '{' - сбалансированы")
    elif brackets_str1.size() / brackets_str2.size() != 1:
        print("В Этой строке скобки: '{' - не сбалансированы")


def main():
    find1(a)
    find2(a)
    find3(a)


if __name__ == '__main__':
    # a = '(((([{}]))))'
    a = '[([])((([[[]]])))]{()}'
    # a = '{{[(])]}}'
    main()
