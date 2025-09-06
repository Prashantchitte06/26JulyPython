# Creating a tuple
tp = (6, 5, 0, "abc", 11.5)


# Get size of tuple
print(len(tp))  # Output: 5

# Get specific data
print(tp[3])  # Output: abc


# —--Adding elements—-
# Tuples are immutable, so you cannot use `.append()`, `.insert()`, or `.extend()`.
# Instead, create a new tuple:
tp = tp + (4,)
print(tp)  # Output: (6, 5, 0, 'abc', 11.5, 4)


# —-Removing elements—----
# Tuples are immutable; you cannot use `.pop()` or `.remove()`.
# Instead, create a new tuple excluding the element:
tp = tuple(x for x in tp if x != 11.5)
print(tp)  # Output: (6, 5, 0, 'abc', 4)


#----Copy tuple—
tp1 = tp  # Copy by assignment (no `.copy()` method needed for tuples)
print(tp1)  # Output: (6, 5, 0, 'abc', 4)


# —--Sorting (Tuples cannot be sorted directly)---
tup = (3, 1, 4, 2)
tup1 = tuple(sorted(tup))  # Creates a new sorted tuple
print(tup1)  # Output: (1, 2, 3, 4)


# Reversing (Create a new reversed tuple)
print(tup)
tup2 = tup[::-1]
print(tup2)  # Output: (2, 4, 1, 3)


# # Searching & Counting
tp = (1, 4, 8, 6, 4, 6, 2, 8)
print(tp.index(6))  # Output: 2 (1st occurrence)
print(tp.count(4))  # Output: 2




