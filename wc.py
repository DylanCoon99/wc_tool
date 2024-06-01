import sys

#  run tool in command line
#  wcount filename.txt     -->  returns wordcount, linecount, charcount, and bytecount
#  wcount -w filename.txt  -->  returns wordcount
#  wcount -l filename.txt  -->  returns linecount
#  wcount -c filename.txt  -->  returns bytecount
#  wcount -m filename.txt  -->  returns charcount


def count_words(file):
	return 19


def count_lines(file):
	return 7


def count_char(file):
	return 102


def count_bytes(file):
	return 102


def main():

	args = sys.argv[1:]
	print(args)
	flags = {"-w": 0, "-l": 0, "-c": 0, "-m": 0}

	flags["-w"] = 1 if "-w" in args else 0
	flags["-l"] = 1 if "-l" in args else 0
	flags["-c"] = 1 if "-c" in args else 0
	flags["-m"] = 1 if "-b" in args else 0

	# if no flags are present --> count everything

	return


if __name__ == '__main__':
	main()
