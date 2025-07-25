# Object-Oriented Programming (OOP) in Python

## Practiced Concepts with Definitions and Details

---

### 1. Class & Object

**Class:**  
A class is a blueprint or design that defines the structure and behavior (attributes and methods) of objects.

**Object:**  
An object is a real instance of a class. It holds actual data and can use the class's methods.

**Practice:**  
- Created custom classes using the `class` keyword.
- Instantiated objects using constructors (`__init__`).

---

### 2. Instance & Class Variables

**Instance Variable:**  
These are object-specific variables, defined using `self.var` inside methods. Each object has its own copy.

**Class Variable:**  
These are shared variables, defined inside the class body (outside methods), and are the same across all instances.

**Practice:**  
- Declared both instance and class variables.
- Understood the difference between object-level and shared data.

---

### 3. Inheritance

**Inheritance:**  
Inheritance allows a child class to use the properties and behaviors (methods/variables) of a parent class. Promotes reusability and modular code.

**Practice:**  
- Created parent and child class structures.
- Reused logic without duplicating code.

---

### 4. Method Types

#### a. Instance Method
- The most common method type.
- Takes `self` as the first argument and works with instance-level data.

#### b. Class Method
- Takes `cls` as the first argument.
- Used to modify or access class-level data.
- Defined using the `@classmethod` decorator.

#### c. Static Method
- Does not take `self` or `cls`.
- Used for general utility tasks that do not modify class or instance state.
- Defined using the `@staticmethod` decorator.

**Practice:**  
- Implemented all three types and observed their behavior.

---

### 5. Dunder (Magic) Methods

**Dunder Methods:**  
Special methods in Python that start and end with double underscores. Python automatically calls these in specific situations.

Examples:
- `__init__()` – constructor, runs when object is created.
- `__str__()` – defines how the object is printed.

**Practice:**  
- Used `__init__()` to initialize object attributes.
- Overrode `__str__()` to return a readable object representation.
- Understood that `__str__()` must always return a string.

---

### 6. Method Overriding

**Overriding:**  
When a child class defines a method with the same name as one in the parent class, it overrides the parent's version.

**Practice:**  
- Overrode a method in the child class.
- Verified that the child method was called when the object was used.

---

### 7. Encapsulation

**Encapsulation:**  
Encapsulation is the concept of restricting direct access to class attributes. It's implemented using:
- `_var` for protected variables (convention-based).
- `__var` for private variables (name mangling in Python).

**Practice:**  
- Created private and protected variables.
- Provided access via public methods (getters/setters).

---

### 8. Polymorphism

**Polymorphism:**  
Polymorphism allows the same method name to behave differently in different classes.

Example: `sound()` method in both `Cat` and `Dog` classes, but with different outputs.

**Practice:**  
- Defined a common method in multiple classes.
- Used the same method call, but observed different behaviors.

---

### 9. Method Overloading

**Overloading:**  
Method overloading means defining multiple methods with the same name but different parameters.

**Note:**  
Python does not support traditional overloading. However, similar behavior can be achieved using default parameters or `*args`/`**kwargs`.

**Practice:**  
- Simulated overloading using default arguments and variable-length parameters.

---

## Pillars of OOP

The four fundamental principles of Object-Oriented Programming:

---

### 1. Encapsulation
Encapsulation is the concept of hiding internal object details and exposing only necessary parts through methods. It protects data from direct modification and keeps the implementation hidden.

For example, using `self.__name = name` makes `name` private, and we expose it via a method like `def get_name(self): return self.__name`.

---

### 2. Polymorphism
Polymorphism means having the same method name behave differently across different classes. It allows flexible and interchangeable use of objects.

For example, `Dog().speak()` returns `"Woof!"`, while `Cat().speak()` returns `"Meow!"` — same method name, different behavior.

---

### 3. Inheritance
Inheritance allows a class to inherit properties and methods from another class. This supports code reusability and avoids duplication.

For example, `class Bird(Animal):` lets `Bird` use all methods defined in `Animal`, such as `move()`.

---

### 4. Abstraction
Abstraction hides complex implementation details and shows only essential features. It’s often done using abstract base classes.

For example, `class Shape(ABC): @abstractmethod def area(self): pass` ensures that any subclass like `Circle` must define its own `area()` method.
