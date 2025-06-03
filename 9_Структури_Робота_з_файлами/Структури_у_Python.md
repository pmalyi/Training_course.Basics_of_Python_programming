## "Структури" у Python
Для зберігання складних записів у багатьох мовах є спеціальні типи даних, такі як struct C++ або record в 
Паскалі.
Змінна типу структура містить у собі кілька іменованих полів. Наприклад, повертаючись до завдання сортування
людей за спаданням росту, нам було б зручно зберігати опис кожної людини у вигляді структури з двома полями:
зріст та ім'я.
У чистому вигляді типу даних "структура" у стандарті мови Python немає. Існує кілька способів реалізації 
аналогів структур: 
1. namedtuple з бібліотеки collections
2. Класи як структури.  
### Іменований кортеж
namedtuple — це спеціальний тип кортежу, де кожен елемент має ім’я. Це зручно для структурування даних, коли
ви хочете мати кортеж, але звертатись до його елементів за іменами, а не індексами.
Імпортується з модуля collections:
```python
from collections import namedtuple
```
#### Створення namedtuple:
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
# Тепер у вас є об'єкт p типу Point з доступом до x та y:
print(p.x)  # 3
print(p.y)  # 4
```
#### Методи namedtuple
```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
bob = Person('Bob', 25)

# index() - повертає індекс елемента у кортежі
print(bob.index(25)) # 1

# count() - повертає кількість елементів у кортежі
print(bob.count('Bob')) # 1

# _asdict() — перетворити на словник
print(bob._asdict())  # {'name': 'Bob', 'age': 25}

# _replace() — створити новий об’єкт з деякими зміненими полями
bob2 = bob._replace(age=30)
print(bob2)  # Person(name='Bob', age=30)

# _fields — повертає список полів
print(Person._fields)  # ('name', 'age')
```


