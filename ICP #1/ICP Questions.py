if __name__ == '__main__':

    # Question 1: Initialize array, show results of array
    print("\nQUESTION 1:")

    # Initial printing of initial array
    array_1 = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    print("Initial array: ", array_1)

    # Sort array_1
    array_1.sort()
    print("Sorted array: ", array_1)

    # Find max
    print("Max age: ", max(array_1))

    # Find min
    print("Min age: ", min(array_1))

    # Add the max and the min to the list again
    array_1.append(max(array_1))
    array_1.append(min(array_1))
    array_1.sort()
    print("Max and Min added again to array (sorted): ", array_1)

    # Find the median age
    if (len(array_1)%2 == 0):
        medianAge = [array_1[(int)(len(array_1) / 2)], array_1[(int)(len(array_1) / 2 - 1)]]
    else:
        medianAge = array_1[(int)(len(array_1) / 2)]
    print("Median age: ", medianAge)

    # Find the average age
    totalIndex = 0.0
    for i in range(len(array_1)):
        totalIndex = totalIndex + array_1[i]
    print("Average age: ", totalIndex/len(array_1))

    # Find the range of ages
    print("Range of ages: ", max(array_1) - min(array_1))


    # Question 2: Dealing with dictionaries
    print("\nQUESTION 2:")

    # Create an empty dictionary named "dog"
    dog = {}
    print("Dictionary \"dog\": ", dog)

    # Add name, color, breed, legs, age to the dog dictionary
    dog['name'] = ''
    dog['color'] = ''
    dog['breed'] = ''
    dog['legs'] = ''
    dog['age'] = ''
    print("Dictionary \"dog\", updated: ", dog)

    # Create a student dictionary and add first_name, last_name,
    # gender, age, marital_status, skills, country, city, and
    # address as keys for the dictionary
    student = {'first_name': '',
               'last_name': '',
               'gender': '',
               'age': '',
               'marital_status': '',
               'skills': ['skill 1', 'skill 2', 'skill 3'],
               'country': '',
               'city': '',
               'address': ''}
    print("Dictionary \"student\": ", student)

    # Get the length of the student dictionary
    print("Length of student dictionary: ", len(student))

    # Get the value of skills and check the data type, it should be a list
    print("Data type of skills: ", type(student['skills']))
    print("Value of skills: ", student['skills'])

    # Modify the skills values by adding one or two skills
    student.update({'skills': student['skills'] + ['skill 4', 'skill 5']})
    print("Value of skills (updated): ", student['skills'])

    # Get the dictionary keys as a list
    print("student keys: ", student.keys())

    # Get the dictionary values as a list
    print("student values: ", student.values())


    # Question 3: Dealing with Tuples
    print("\n\nQUESTION 3:")

    # Create a tuple containing names of your sisters and your brothers
    # (imaginary siblings are fine)
    sisters = ('Greta', 'Rhianin', 'Lindsay')
    brothers = ('Garth', 'Dylan', 'Chase')
    print("Sisters tuple: ", sisters)
    print("Brothers tuple: ", brothers)

    # Join brothers and sisters tuples and assign it to siblings
    siblings = sisters + brothers
    print("Siblings tuple: ", siblings)

    # How many siblings do you have?
    print("I have", len(siblings), "siblings.")

    # Modify the siblings tuple and add the name of your father and mother
    # and assign it to family_members
    family_members = siblings + ('Kyle', 'Leslie')
    print("\"family_members\":", family_members)


    # Question 4: Dealing with Sets
    print("\n\nQUESTION 4:")

    # Initialize values for question;
    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    age = [22, 19, 24, 25, 26, 24, 25, 24]

    # Find the length of the set it_companies
    print("length of it_companies:", len(it_companies))

    # Add 'Twitter' to it_companies
    it_companies.add('Twitter')
    print("it_companies with Twitter added:", it_companies)

    # Insert multiple IT companies at once to the set it_companies
    it_companies = it_companies.union(it_companies, ('Meta', 'X', 'Amazon_Prime'))
    print("it_companies with others added at once:", it_companies)

    # Remove one of the companies from the set it_companies
    it_companies.remove('Twitter')
    print("it_companies with Twitter removed:", it_companies)

    # What is the difference between remove and discard
    print("The \"remove\" function raises a KeyError exception. The \"discard\" function does not.")

    # Join A and B
    print("Join of A and B:", A | B)

    # Find A intersection B
    print("Intersection of A and B:", A & B)

    # Is A subset of B
    print("A is a subset of B")

    # Are A and B disjoint sets
    print("A and B aren't disjoint sets")

    # Join A with B and B with A
    print("A joined with B:", A|B)
    print("B joined with A:", B|A)

    # What is the symmetric difference between A and B
    print("Symmetric difference of A and B:", A^B)

    # Delete the sets completely
    A.clear()
    B.clear()
    print("Sets A and B, cleared:", A, B)

    # Convert the ages to a set and compare the length of the list and the set
    print("\"age\" list as is:", age)
    age_list_length = len(age)
    age = set(age)
    age_set_length = len(age)
    print("\"age\" list converted to set:", age)
    print("Length of \"age\" list:", age_list_length)
    print("Length of \"age\" set:", age_set_length)


    # Question 5: Circle calculations
    print("\n\nQUESTION 5:")
    # The radius of a circle is 30 meters
    circle_radius = 30

    # Calculate the area of a circle and assign the value to
    # a variable name of _area_of_circle_
    _area_of_circle_ = 3.14 * (circle_radius ** 2)
    print("Area of circle with radius 30:", _area_of_circle_,"meters")

    # Calculate the circumference of a circle and assign the
    # value to a variable name of _circum_of_circle_
    _circum_of_circle_ = 2 * 3.14 * circle_radius
    print("Circumference of circle with radius 30:", _circum_of_circle_,"meters")

    # Take radius as user input and calculate the area
    print("The area of your circle is:", 3.14 * ((int)(input("Enter a radius for a circle, will calculate area:")) ** 2))


    # Question 6: Fun with Strings
    print("\n\nQUESTION 6:")
    # "I am a teacher and I love to inspire and teach people"
    question_6_string = "I am a teacher and I love to inspire and teach people"
    print("Given this sentence:", question_6_string)

    # How many unique words have been used in the sentence? Use
    # the split methods and set to get the unique words
    print("There are",len(set(question_6_string.split())), "unique words in this sentence.")


    # Question 7: Tab Escape
    print("\n\nQUESTION 7:")

    # Use a tab escape sequence to get the following lines:
    #  Name     Age     Country City
    #  Asabeneh  250     Finland Helsinki

    print("Name\t\tAge\t\tCountry City\nAsabeneh\t 250\t Finland Helsinki")


    # Question 8: String Formatting
    print("\n\nQUESTION 8:")

    # Use the string formatting method to display the following:

    radius = 10
    area = 3.14 * radius ** 2
    print(f"The area of a circle with radius {radius} is {area} meters square.")


    # Question 9: Conversion
    print("\n\nQUESTION 9:")

    # Write a program, which reads weights (lbs.) of N students into a list and
    # convert these weight to kilograms in a separate list using Loop. N: Number
    # of students (read input from user)

    n = (int)(input("Please enter the number of students you wish to put weights in for: "))
    student_lbs = []
    student_kil = []

    for i in range(n):
        student_lbs.append(input(f"Please input weight for student {i + 1}: "))
        student_kil.append((float)(student_lbs[i]) * 0.453)

    for i in range(n):
        print(f"The weight of student {i + 1} is {student_lbs[i]:.2f} in lbs, or {student_kil[i]:.2f} in kg.")