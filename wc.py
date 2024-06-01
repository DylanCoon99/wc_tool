import sys

#  run tool in command line
#  wcount filename.txt     -->  returns wordcount, linecount, charcount, and bytecount
#  wcount -w filename.txt  -->  returns wordcount
#  wcount -l filename.txt  -->  returns linecount
#  wcount -c filename.txt  -->  returns bytecount
#  wcount -m filename.txt  -->  returns charcount


def count_words(file):
	with open(file) as f:
		file = f.read()
	return len(file.split(' '))


def count_lines(file):
	with open(file) as f:
		file = f.read()
	return len(file.split('\n')) - 1


def count_char(file):
	with open(file) as f:
		file = f.read()
	return len(file)


def count_bytes(file):
	with open(file) as f:
		file = f.read()
	return len(file)


def main():

	args = sys.argv[1:]
	len_args = len(args)
	if len_args == 0: return

	flags = {"-w": 0, "-l": 0, "-c": 0, "-m": 0}

	flags["-w"] = 1 if "-w" in args else 0
	flags["-l"] = 1 if "-l" in args else 0
	flags["-c"] = 1 if "-c" in args else 0
	flags["-m"] = 1 if "-b" in args else 0

	# if no flags are present --> count everything

	# file variable
	file = args[-1]
	# going to need to address file not found error as well as file not supplied error
	
	return_values = {"word_count": 0, "line_count": 0, "char_count": 0, "byte_count": 0}


	if flags["-w"]:
		return_values["word_count"] = count_words(file)
	if flags["-l"]:
		return_values["line_count"] = count_lines(file)
	if flags["-m"]:
		return_values["char_count"] = count_char(file)
	if flags["-c"]:
		return_values["byte_count"] = count_bytes(file)


	# going to need to format the output

	return


if __name__ == '__main__':
	main()
