import sys
from tqdm import tqdm
import time
import wikipedia

def progress_bar(url, output_file):
	# Writing the urk to the argument file
	with open(output_file, 'a') as file:
		file.write(url + "\n")

	for _ in tqdm( range(100), desc="Extracting Url..."):
		time.sleep(0.01)

def main():

	term = sys.argv[1]
	url = wikipedia.page(term).url

	output_file = sys.argv[2]

	# Dummy progress bar
	progress_bar(url, output_file)

	# Brief Summary on the search term
	with open(term+".txt", 'a') as file:
		file.write(wikipedia.summary(term) + "\n")	

if __name__ == "__main__":
	main()