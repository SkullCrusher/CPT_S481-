
    # The thing.
def concordance(f, unique = True):
    
        # The results.
    database = []
    
        # load the file into InputFile.
    f = open(f, 'r')
    InputFile = f.read()
    f.close()

        # Clean up the file.
    InputFile = InputFile.lower() # change to lower case.
    InputFile = InputFile.splitlines() # Change it into lines.
    
    #InputFile = InputFile.strip() # remove white space.
    
    LineCount = 0

        # For each line
    for line in InputFile:
        LineCount += 1

            # Split it into words.
        for word in line.split():

                # Used to remove trash characters from the words.            
            newword = ""
            last_alpha = 0
            buffer = ""
            
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
                    buffer = ""

                    continue
                
                    # Is it part of a word? add to buffer any maybe accept.
                if word[c] == '-' or word[c] == '\'':
                    buffer = buffer + word[c]
                   
                # Replace the old word with the cleaned one.
            word = newword
                    
            
            # Remove all 
            MatchIndex = -1
            
                # Check if the word already exists in the database.
            for x in range(0, len(database)):
                if(database[x][0] == word):
                    MatchIndex = x
            
                # If the word is already in the db, increase count.
            if MatchIndex != -1: 
                    # Add the line number to it.
                temp = database[x][2]
                temp.extend([LineCount])
                database[x] = [word, database[x][1] + 1, temp]
            else:
                database.append([word, 1, [LineCount]])
           
        # Post processing - sort the database based on the alphabet 
    database.sort(key=lambda x: x[0])
    
        # Post processing - If unique remove the same lines from the list.
    if unique:
        for pair in database:            
            pair[2] = list(set(pair[2]))
    
    return database


    
    # Self test. (TO DO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)
if __name__ == '__main__':
    database = concordance("file.txt")

    print(database)
     