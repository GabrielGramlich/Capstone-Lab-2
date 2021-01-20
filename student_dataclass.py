from dataclasses import dataclass

@dataclass
class Student:
	name: str
	school_id: str
	gpa: float


def main():
	students = get_students()
	display_students(students)


def get_students():
	students = []
	count = 0
	while True:
		count = count + 1
		student = get_student(count)
		students.append(Student(student[0], student[1], student[2]))
		response = will_continue()
		if response == 'n':
			break

	return students


def get_student(count):
	name = input(f'What is student {count}\'s name? ').title()
	school_id = input(f'What is student {count}\'s shool id? ')
	gpa = get_valid_gpa(count)
	return(name, school_id, gpa)


def get_valid_gpa(count):
	while True:
		try:
			gpa = float(input(f'What is student {count}\'s gpa? '))
			if is_valid_gpa(gpa):
				break
			else:
				print('Must be between 0.0 and 4.0')
		except ValueError:
			print('Not a number. Please try again.')
	return round(gpa,1)


def is_valid_gpa(gpa):
	return gpa <= 4 and gpa >= 0


def will_continue():
	response = ''
	while validate_response(response):
		response = input(f'Do you have any more students to record? (Y/n) ').lower()
		if validate_response(response):
			refresh(1)

	return response


def validate_response(response):
	return not (response == 'y' or response == 'n')


def display_students(students):
	print()
	for student in students:
		print(student)


if __name__ == '__main__':
	main()


'''
The dataclass version is clean, and as a frequent writer of the hated spaghetti code, I can respect that.
That being said, having the functions in there let's you create conditions in the object like we did with the last one.
That being said, my version 2 of the last program showed you can do that outside of it just as easily, and use that
code for other things within the program.
That being said, keeping code only accessible to the code it's supposed to interact with is smort.
That being said, I don't really know, I'm just gonna try it both way a bunch, and see which I like more, and what
possible issues arise.
That being said, sorry I said 'that being said' so much.
'''
