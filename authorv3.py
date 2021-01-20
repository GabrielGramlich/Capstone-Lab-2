import sys

class Author:
	def __init__ (self, name):
		self.name = name
		self.books = []
		print('Successfully added!')

	def publish(self, title):
		if title not in self.books:
			self.books.append(title)
			print('Successfully added!')
		else:
			print('You already added that, you silly goose.')


	def __str__(self):
		published_works = ', '.join(self.books) or 'Nothing'
		return f'{self.name} has published {published_works}'


def main():
	authors = get_authors()
	authors = get_books(authors)
	display_books(authors)


def get_authors():
	authors = []
	while True:
		author = Author(input('Which author would you like to make a record of? ').title())
		authors.append(author)
		response = will_continue('authors', '')
		if response == 'n':
			break

	return authors



def will_continue(content_type, extra_message):
	response = ''
	while validate_response(response):
		response = input(f'Do you have any more {content_type} to record{extra_message}? (Y/n) ').lower()

	return response


def validate_response(response):
	return not (response == 'y' or response == 'n')


def get_books(authors):
	for author in authors:
		count = 0
		while True:
			count = count + 1
			author.publish(input(f'What is the name of book {count} by {author.name}? ').title())
			response = will_continue('books', ' for ' + author.name)
			if response == 'n':
				break
	return authors


def display_books(authors):
	for author in authors:
		print(author)


if __name__ == '__main__':
	main()
