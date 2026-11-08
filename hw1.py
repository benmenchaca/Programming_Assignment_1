"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data

# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose:  Counts how many vowels in a string.
    # TODO: Input(s): One parameter: the string that we are trying to count the number of vowels in.
    # TODO: Output: The function returns the number of vowels counted
   result = 0
   for t in text.lower():
        if t == 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u':
            result += 1
   
   return result


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose:  Computes the lengths of lists within a list
    # TODO: Input(s):  One parameter: list of number lists.
    # TODO: Output: The function returns a new list containing only lists that have a length of 2.
    
    return [i for i in items if len(i) == 2]
    


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: Computes a new list of lists where each inner list is sorted in ascending order if it has exactly two elements.
    # TODO: Input(s): One parameter: a list of lists of integers.
    # TODO: Output: The function returns a new list of lists where each inner list is sorted in ascending order if it has exactly two elements; otherwise, the inner list remains unchanged.
    result = []
    for i in range(len(items)):
        if len(items[i]) == 2 and items[i][0] > items[i][1]:
            result.append([items[i][1], items[i][0]])
        else:
            result.append(items[i])

    return result



# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: Computes the sum of two Price objects, taking into account the conversion of cents to dollars if necessary.
    # TODO: Input(s): Two parameters: first and second, both of which are instances of the data.Price class representing monetary values in dollars and cents.
    # TODO: Output: The function returns a new instance of the data.Price class representing the total sum of the two input Price objects, with cents properly converted to dollars if they exceed 100.
   cents=first.cents + second.cents 
   dollars=first.dollars + second.dollars

   dollars += cents // 100
   cents = cents % 100

   return data.Price(dollars, cents)


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: Computes the area of a rectangle given its dimensions.
    # TODO: Input(s): One parameter: rectangle, which is an instance of the data.Rectangle class representing the dimensions of the rectangle.
    # TODO: Output: The function returns a float representing the area of the rectangle, calculated as the product of its width and height.
     width = rectangle.bottom_right.x - rectangle.top_left.x
     height = rectangle.bottom_right.y - rectangle.top_left.y
     area = width * height
     return area
   


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: Filters a list of Book objects to return only those written by a specific author.
    # TODO: Input(s): Two parameters: author (a string) and books (a list of Book objects).
    # TODO: Output: The function returns a new list containing only the Book objects written by the specified author.
  
    return [book for book in books if author in book.authors]


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: Computes the smallest circle that can contain the given rectangle.
    # TODO: Input(s): One parameter: rectangle, which is an instance of the data.Rectangle class representing the dimensions of the rectangle.
    # TODO: Output: The function returns a new instance of the data.Circle class representing the bounding circle.
    
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    radius = ((rectangle.bottom_right.x - rectangle.top_left.x) ** 2 + (rectangle.bottom_right.y - rectangle.top_left.y) ** 2) ** 0.5 / 2
    return data.Circle(data.Point(center_x, center_y), radius)


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: Computes a list of employee names whose pay is below the average pay of all employees.
    # TODO: Input(s): One parameter: employees, which is a list of Employee objects.
    # TODO: Output: The function returns a list of strings representing the names of employees whose pay is below the average.
    result = []


    if len(employees) == 0:
        return result

    average_pay = sum(employee.pay_rate for employee in employees) / len(employees)

    for employee in employees:
        if employee.pay_rate < average_pay:
            result.append(employee.name)

    return result