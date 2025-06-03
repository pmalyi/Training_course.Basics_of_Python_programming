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
#### Приклади використання іменовах кортежів
*Задача 1: Книга*
Створіть іменований кортеж Book з полями title, author, year.  
Створіть об’єкт книга. Надрукуйте автора. Змініть рік видання через _replace. 
```python
from collections import namedtuple

Book = namedtuple('Book', ['title', 'author', 'year'])
b = Book("Python 101", "John Doe", 2020)
print(b.author)   # John Doe
new_b = b._replace(year=2021)
print(new_b)  # Book(title='Python 101', author='John Doe', year=2021)
```

*Задача 2: Точка на площині*  
Створіть Point(x, y).  
Обчисліть відстань до початку координат. Надрукуйте Point у вигляді (x=..., y=...).
```python
from collections import namedtuple
import math

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
distance = math.sqrt(p.x ** 2 + p.y ** 2)
print(f"Distance: {distance:.2f}")   # Distance: 5.00
```

*Задача 3: Студенти*   
Є список студентів у вигляді Student(name, grade).  
Надрукувати імена студентів, у яких оцінка ≥ 90. Порахувати середній бал.
```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade'])
students = [
    Student("Alice", 91),
    Student("Bob", 85),
    Student("Clara", 96),
]
print([s.name for s in students if s.grade >= 90])   # ['Alice', 'Clara']
avg = sum(s.grade for s in students) / len(students)
print(f"Average grade: {avg:.2f}")   # Average grade: 90.67
```

