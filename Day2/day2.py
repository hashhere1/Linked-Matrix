"""List"""
print("List")
sample_list = [1, 2, 3, 4]
# accessing list elements
print(sample_list[0], sample_list[1])
# appending into the list
sample_list.append("Hello")
print(sample_list)

# removing from the list
sample_list.remove(1)
print(sample_list)

#iterating over a list
for items in sample_list:
    print({f"Items": items})


"""Tuple"""
print("\nTuple")
# Creating a tuple
sample_tuple = (10, 20)

# Accessing Elements
print(sample_tuple[0])
# Tuples are immutable – you can't change values


"""Dictionary"""
print("\n Dictionary")

# Creating a dictionary
sample_dictionary = {"Name": "Hassaan", "Semester": "6th"}

# Accessing the values in dictionary
print(sample_dictionary["Name"])

# Adding a value in the dictionary
sample_dictionary["City"] = "Lahore"
print(sample_dictionary)

# Iterating over a dictionary
for key, value in sample_dictionary.items():
    print(key,": ",value)


"""Set"""
print("\n Set")

# Creating a Set
sample_set = {1, 2, 3, 4, 5}

# Accessing a sample set
"""We cannot access the elements from a set directly because they are unordered. Elements can be accessed by
converting a set into a dictionary"""
accessing_set = list(sample_set)
print(accessing_set[0])

# Adding into the set
sample_set.add(5)
print(sample_set)

# Removing an element from the set
sample_set.remove(2)
print(sample_set)

"""Comprehensions"""

# List Comprehension
print("\n List Comprehension")

squares = [x**2 for x in range(5)]
print(squares)

# Dict Comprehension
print("\n Dict Comprehension")

dict_comprehension = {x: x ** 2 for x in range(5)}
print(dict_comprehension)

# Set Comprehension
print("\n Set Comprehension")

set_comprehension = {x ** 2 for x in range(5)}
print(set_comprehension)


"""Student Record Management System (Console-Based)"""
print("\n Student Management System! ")

students = []

def add_student():
    roll = int(input("Enter roll number: "))
    year = int(input("Enter admission year: "))
    name = input("Enter name: ")
    city = input("Enter city: ")
    grade = input("Enter grade: ").upper()

    student = {
        "roll": (roll, year),  # Tuple
        "name": name,
        "city": city,
        "grade": grade
    }
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("\nAll Student Records:")
    for s in students:
        print(f"Roll: {s['roll'][0]} | Year: {s['roll'][1]} | Name: {s['name']} | City: {s['city']} | Grade: {s['grade']}")
    print()

def search_by_name():
    name = input("Enter name to search: ")
    found = [s for s in students if s["name"].lower() == name.lower()]
    if found:
        for s in found:
            print(f"Found: {s}")
    else:
        print("No student found with that name.")
    print()

def filter_by_city():
    city = input("Enter city to filter: ")
    filtered = [s for s in students if s["city"].lower() == city.lower()]
    if filtered:
        print(f"\nStudents from {city.title()}:")
        for s in filtered:
            print(f"{s['name']} (Roll: {s['roll'][0]}, Grade: {s['grade']})")
    else:
        print(f"❌ No students found from {city}.")
    print()

def show_unique_cities():
    unique_cities = {s["city"] for s in students}
    print("\nUnique Cities:")
    for city in unique_cities:
        print(f"- {city}")
    print()

def main():
    while True:
        print("Student Record Management")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search by Name")
        print("4. Filter by City")
        print("5. Show Unique Cities")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_by_name()
        elif choice == "4":
            filter_by_city()
        elif choice == "5":
            show_unique_cities()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
