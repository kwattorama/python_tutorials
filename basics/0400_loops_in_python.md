# Loops in Python

**[Loops](https://en.wikipedia.org/wiki/LOOP_(programming_language))** are yet another fundamental concepts in **computer science**. In simple terms it means to **iterate** or **repeat** something.

**Note:** To understand loops properly, it is presumed that you know little bit about **[Containers](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#container-type)**.

In programming, usually all statements are executed **sequentially** i.e. line by line. But many times we come across instances wherein we need to repeat the execution multiple times. Loops come in handy during those situations. Most of the programming languages have the concept of **loops**. They help the developer to reduce the efforts for doing repetitive work. Essentially, loops are a **[control flow](https://en.wikipedia.org/wiki/Control_flow)** structure which deals with **iterations**.

By definition, *Repetitive execution of the same block of code is called as **looping** or **iterations**.*

These are usually called as **[Compound](https://docs.python.org/3/reference/compound_stmts.html)** statements as the statements or the code spans multiple lines. While (no pun intended) there are various types of loops in Python but, according to me loops could be classified into **two** simple types: **[Iterative](https://en.wikipedia.org/wiki/Iteration#Computing)** loop and **[Conditional](https://en.wikipedia.org/wiki/Conditional_loop)** loop.

## Iterative Loop

Iterative loops are the structures (**[syntax](https://en.wikipedia.org/wiki/Python_syntax_and_semantics)**) that repeats till it gets exhausted. Means **iterative** loops run till all the elements from the **[containers](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#container-type)** are processed.

In Python, we classify iterative loops into **two** types: **[for](https://docs.python.org/3/reference/compound_stmts.html#for)** loop and **[while](https://docs.python.org/3/reference/compound_stmts.html#while)** loop.

### For loop

**For loop** is the most basic and common type of loop in programming. They are used for iterating over a **[container](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#container-type)** or **[sequence](https://github.com/xames3/python_tutorials/blob/master/basics/0301_types_of_data_in_python.md#mutable-objects)**. They are usually used to iterate upto a **definite** range or **fixed** range (some limit). Hence these are also considered as **Definite Loops**.

```python
# This is basic and general format of for loops in Python
for new_variable in container_object:
	# do something with the new variable
	new_variable...
```

From the above format, **new_variable** is some random variable that has never been created. This variable will be representing each member or element of the **[container_object](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#container-type)** till all the elements of the container are exhausted.

```python
>>> # Actual usage in Python using list object
>>> some_list = [1, "xa", 2.0, (), {"name": "kaamiki"}]
>>> 
>>> for idx in some_list:
... 	print(idx)
>>> 
1
"xa"
2.0
()
{"name": "kaamiki"}
```

In the above example, we first defne our **container_object** which is a **[list](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#lists-list)** in our case.
Here, **idx** represents **new_variable** from the above format. What **for loop** essentially does is, it makes the **idx** variable to **[access each member](https://github.com/xames3/python_tutorials/blob/master/basics/0301_types_of_data_in_python.md#mutability-of-a-list)** or element of the **some_list** (**[list](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#lists-list)**) object.

The above format of the **for loop** can be used for writing any basic **for loop** with the basic types of containers like **[list](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#lists-list)**, **[tuple](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#tuple-tuple)**, **[set](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#set-set)** and **[dict](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#dictionary-dict)**.

**Note:** Using the above format while iterating through a dictionary object, only the keys would be accessed. Not the values.

#### For loop for Tuple object

```python
random_tuple = (69, 420.0, "xa")

for idx in random_tuple:
    # Doing something using idx, in this case printing values
    print(idx)
```

#### For loop for Set object

```python
set_object = {21, "nirvana"}

for idx in set_object:
    print(idx)
```

#### For loop for Dictionary object

Here, **idx** would represent the "key" of the the **lame_dict** dictionary object.

```python
lame_dict = {"key_1": "value_1", "key_2": "value_2"}

for idx in lame_dict:
    print(idx)
```

Besides the traditional containers (lists/dicts/tuples/set) there are other **two** basic built-in Python containers: **[range()](https://docs.python.org/3/library/stdtypes.html#ranges)** and **[enumerate()](https://docs.python.org/3/library/functions.html#enumerate)**.

### Range in Python

Range is an **iterable** (something which contains more than one element) just like **Containers**.
