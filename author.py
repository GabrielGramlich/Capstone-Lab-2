import sys

class Author:
	def __init__ (self, name):
		self.name = name
		self.books = []

	def publish(self, title):
		self.books.append(title)

	def __str__(self):
		published_works = ', '.join(self.books) or 'Nothing'
		return f'{self.name} has published {published_works}'


def main():
	authors = get_authors()
	authors = get_books(authors)
	display_books(authors)


def get_authors():
	authors = []
	go = False
	while True:
		go, refresh_rate = display_success(go)
		author = Author(input('Which author would you like to make a record of? ').title())
		authors.append(author)
		response = will_continue('authors', '')
		if response == 'n':
			refresh(refresh_rate)
			break
		else:
			refresh(refresh_rate)

	return authors


def display_success(go):
	refresh_rate = 2
	if go:
		print('Successfully added!')
		refresh_rate = 3
	else:
		go = True

	return go, refresh_rate



def will_continue(content_type, extra_message):
	response = ''
	while validate_response(response):
		response = input(f'Do you have any more {content_type} to record{extra_message}? (Y/n) ').lower()
		if validate_response(response):
			refresh(1)

	return response


def validate_response(response):
	return not (response == 'y' or response == 'n')


def get_books(authors):
	for author in authors:
		count = 0
		go = False
		while True:
			go, refresh_rate = display_success(go)
			count = count + 1
			author.publish(input(f'What is the name of book {count} by {author.name}? ').title())
			response = will_continue('books', ' for ' + author.name)
			if response == 'n':
				refresh(refresh_rate)
				break
			else:
				refresh(refresh_rate)
	return authors


def display_books(authors):
	for author in authors:
		print(author)


def refresh(lines):
	for i in range(lines):
		sys.stdout.write("\033[F")
	for i in range(lines):
		print(' '*60)
	for i in range(lines):
		sys.stdout.write("\033[F")
	sys.stdout.flush()


if __name__ == '__main__':
	main()
