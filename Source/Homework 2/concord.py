import sys
from concordance import concordance

	# Remove the filename, sort the files, and load and parse them.
def Process_Arguments(arg):
	Filename = []

	for x in range(1, len(arg)):
		Filename.append([arg[x]])
	
	Filename.sort()

	return Filename


# [["word", []]]	
Data = []
Filename = Process_Arguments(sys.argv)

def CompressLines(collection):
	
	Word = collection[0]
	
	print("WORD {}".format(Word))
	
	return collection
	

	# add the words to the data.
def ProcessWord(word, file, lines):
	
	Found = False
	Count = 0
	
	# search for the word in the list.
	for Record in Data:
		if Record[0] == word:
			Found = True
			break
		Count = Count + 1
		
		# If not found add to data.
	if Found == False:
			#['word', 'file.txt', [1,3,4]]
		Data.append([word, [file, lines]])
	else:
		#print(Count)
		Data[Count][1].append([file, lines])
		

		
	# Loop through all of the files.
for file in Filename:
	Ret_Data = concordance(file[0])
	
	for WordSet in Ret_Data:
		
			# Add a single word and reference to the TOL.
		#print("{} : {} : {}".format(WordSet[0], file[0], WordSet[2]))
		ProcessWord(WordSet[0], file[0], WordSet[2])
		
		
for x in Data:
	print("\n")
	print(CompressLines(x))
	print("\n")
	

 
