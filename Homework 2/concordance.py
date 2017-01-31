import os, errno

# Used to remove trash characters from the words.
def cleanword(word):

    newword = ''
    last_alpha = 0
    buffer = ''

    # Remove trash from the words.

    for c in range(0, len(word)):

        # Is it a letter ? accept.

        if word[c].isalpha():

            # Add the leading terms if special case.

            if last_alpha != 0:
                newword = newword + buffer + word[c]
            else:
                newword = newword + word[c]

            # Reset trailing.

            last_alpha = c
            buffer = ''

            continue

        # Is it part of a word? add to buffer any maybe accept.

        if word[c] == '-' or word[c] == '\'':
            buffer = buffer + word[c]

    # Replace the old word with the cleaned one.

    return newword


# The thing.

def concordance(f, unique=True):

    # The results.

    dictionary = {}

    # load the file into InputFile.

    f = open(f, 'r')
    InputFile = f.read()
    f.close()

    # Clean up the file.

    InputFile = InputFile.lower()  # change to lower case.
    InputFile = InputFile.splitlines()  # Change it into lines.

    LineCount = 0

    # For each line

    for line in InputFile:
        LineCount += 1

        # Split it into words.

        for word in line.split():

            # clean the word.

            CleanWord = cleanword(word)

            # check if the word is already in the list.

            if CleanWord in dictionary:

                # Should prevent duplicates?

                if unique:

                    # add if not already in list.

                    if LineCount not in dictionary[CleanWord]:
                        dictionary[CleanWord].append(LineCount)
                else:
                    dictionary[CleanWord].append(LineCount)
            else:
                dictionary[CleanWord] = [LineCount]

    return dictionary


# Self test.

if __name__ == '__main__':
	#write a self test file out.
	TestFile = "worda wordb\nwordc wordd worde\nwordd wordd worde\nworda"
	
	f = open('selftest.txt','w')
	f.write(TestFile)
	f.close()
	
	#process the test file.
	database = concordance('selftest.txt')
	
	# remove the test file.
	os.remove('selftest.txt')
	
	#display the results.
	print("Concordance: Self Test - David Harkins\n\nThe file tested is:")
	print("{}\n{}\n{}\n{}\n".format("worda wordb", "wordc wordd worde", "wordd wordd worde", "worda"))
	
	print("Expected results:")
	print("'worda' == [1, 4]: {}".format(database['worda'] == [1,4]))
	print("'wordb' == [1]: {}".format(database['wordb'] == [1]))
	print("'wordc' == [2]: {}".format(database['wordc'] == [2]))
	print("'wordd' == [2, 3]: {}".format(database['wordd'] == [2,3]))
	print("'worde' == [2, 3]: {}".format(database['worde'] == [2,3]))
	
	#print(database)