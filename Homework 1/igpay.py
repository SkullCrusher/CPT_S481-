
	# convert the word into pig latin.
def igpay_convert(word):
	# Where the first vowel is.
	Count = 0;
	
	# Loop through each character in the string.
	for c in word:
		if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
			break;
		Count += 1
		
	# If there are no vowels, return the word.
	if Count == len(word):
		return word
	
	# If the vowel is the first add way.
	if Count == 0:
		return word + "way"
	else:
		# If the vowel does not come first.
		end = ""
		start = ""
		i = 0
		
		for c in word:
			if i < Count:
				end = end + c
			else:
				start = start + c
			i += 1
				
		return start + end + 'ay'
	

# Turn a word into pig latin then check it to make sure the caps are correct.
def igpay(word):
	Result = igpay_convert(word.lower())
	
	# three cases, no starting cap so all lower, first cap, all cap.
	HasUpper = False
	LastUpper = 0
	
	# Search for uppers
	for c in word:
		if c.isupper():
			HasUpper = True
			LastUpper += 1
		else:
			break
			
	# Case 1: no caps.
	if HasUpper == False:
		return Result
	
	# Case 2: First cap
	if HasUpper == True and LastUpper == 1:
		return Result.capitalize()
		
	# Case 3: More than one cap so just assume all caps.
	return Result.upper()
	

def _selftest(word, pig):
	if igpay(word) == pig:
		print("Successful: '" + word + "' -> '" + igpay(word) + "' : Expected '" + pig + "'" )
	else:
		print("Failure: '" + word + "' -> '" + igpay(word) + "' : Expected '" + pig + "'")

def _extended_selftest():
	_selftest("message", "essagemay")
	_selftest("ENGLISH", "ENGLISHWAY") 
	_selftest("translate", "anslatetray") 
	_selftest("HAMMER", "AMMERHAY")
	_selftest("Violently", "Iolentlyvay") 
	_selftest("literature", "iteraturelay") 
	_selftest("Chair", "Airchay") 
	_selftest("window", "indowway") 
	_selftest("musical", "usicalmay") 
	_selftest("zebra", "ebrazay")
	_selftest("penguin", "enguinpay")
	_selftest("home", "omehay")
	_selftest("dog", "ogday")
	_selftest("final", "inalfay")
	_selftest("ink", "inkway")
	_selftest("teacher", "eachertay")
	_selftest("fun", "unfay")
	_selftest("eager", "eagerway")
	_selftest("entomb", "entombway")
	_selftest("entombment", "entombmentway")

# The self check trigger.
if __name__ == "__main__":
	print("\nDavid Harkins: Self test (From pdf)\n")
	
	_selftest("yes", "esyay") #1 (a)
	_selftest("parrot", "arrotpay") #1 (b)
	_selftest("knights", "ightsknay") #1 (b)
	_selftest("add", "addway") #1 (c)
	_selftest("office", "officeway") #1 (c)
	_selftest("why", "why") #1 (d)
	
	print("\nDavid Harkins: Self test (extended)")
	_extended_selftest()



