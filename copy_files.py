import shutil
import getopt
import sys

def get_arguments():
	args = None
	start_number = None
	end_number = None

	#Argument stuff
	try:
		opts, args = getopt.getopt(sys.argv[1:], 's:e:', ['start=', 'end='])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)

	for option, arg in opts:
		if option in ('-s', '--start'):
			start_number = int(arg)
		elif option in ('-e', '--end'):
			end_number = int(arg)
		else:
			raise Exception('Unknown option ' + option + ' : ' + arg)

	if start_number is None:
		print('Start number must be provided.')
		usage()
		sys.exit(2)

	if end_number is None:
		print('End number must be provided.')
		usage()
		sys.exit(2)

	if start_number >= end_number:
		print('End number must be larger then start number.')
		sys.exit(2)

	return start_number, end_number

def copy_files(start_number, end_number):

	#Setup stuff needed for later
	file_path = 'dat/'
	number_needed = end_number - start_number
	starting_file_name = file_path + 'map_' + str(start_number) + '.dat'

	#Loop through incrimenting each time
	i = 1
	while i <= number_needed:
		dst = file_path + 'map_' + str(start_number + i) + '.dat'
		#This does the copy
		shutil.copyfile(starting_file_name, dst)
		print('Created: ' + dst)
		i = i + 1

def usage():
	#If you're dumb
	print('')
	print('Usage: python copy_files.py -s # -e #')
	print('-s | --start: The starting number of the file that gets copy. (Must exist already.)')
	print('Format: -s 2342')
	print('-e | --end: The end number that will be the last file that gets created.')
	print('Format: -s 2358')
	print('')

def main():
	try:
		args = get_arguments()
		print('Starting file copy.')
		copy_files(args[0], args[1])
		print('File copy done.')
	except Exception as e:
		print("Something broke: " + str(e))

if __name__ == "__main__":
	main()
