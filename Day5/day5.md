# Python Expressions – Conceptual Guide

---

## 1. Lambda Functions

### What Are They?

Lambda functions are small, anonymous functions that don’t have a name. They are mainly used for short, simple tasks
where defining a full function would be unnecessary.

### When to Use:

You typically use lambda functions when you need a quick function for operations like sorting, filtering, or mapping
over data — especially when passing functions as arguments.

### Real-Life Use:

Used when you need a quick one-line function — such as sorting a list of items by a specific key or applying a
transformation.
---
## 2. Decorators

### What Are They?

Decorators are a special kind of function in Python that lets you "wrap" another function to add new behavior to it —
without changing its actual code.

### When to Use:

You use decorators to add reusable logic like logging, authentication checks, performance timing, or input validation
around your functions.

### Real-Life Use:

For example, a decorator could automatically log every time a function is run — saving you from writing the same logging
code over and over.
---

## 3. Iterators

### What Are They?

Iterators are objects that let you go through a collection (like a list or string) one item at a time. They follow a
specific protocol with methods to get the next item in a sequence.

### When to Use:

When you want to loop through data manually or build a custom data structure that can be looped through.

### Real-Life Use:

Iterators are used behind the scenes in `for` loops. You’re using them even if you don’t notice — anytime you loop over
a list, dictionary, or set.

---

## 4. Comprehensions

### What Are They?

Comprehensions are a concise way to create new collections (like lists, sets, or dictionaries) based on existing ones,
while possibly filtering or modifying elements.

### When to Use:

When you want to quickly generate or transform data in a clean and readable way.

### Real-Life Use:

Great for tasks like filtering data, generating sequences, or creating a dictionary from two related lists — all in a
single line of code.
---