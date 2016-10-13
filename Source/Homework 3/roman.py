# 0 - n
# 1 - I
# 2 - II
# 3 - III
# 4 - IV
# 5 - V
# 6 - VI
# 7 - VII
# 8 - VIII
# 9 - IX
# 10 - X
# 11 - XI
# 12 - XII
# 13 - XIII
# 14 - XIV
# 15 - XVI
# 16 - XVII
# 17 - XVII
# 18 - XVIII
# 19 - XIX
# 20 - XX



# To correctly view this file please use 'Times new roman' font.
class Roman:

    # instead of if statements fill a dictionary with keys to reference.
    def _GenerateConvertTable(self):
        self.Table = {
            1:          "I",
            4:          "IV",
            5:          "V",
            9:          "IX",
            10:         "X",
            40:         "XL",
            50:         "L",
            90:         "XC",
            100:        "C",
            400:        "CD",
            500:        "D",
            900:        "CM",
            1000:       "M",
            4000:       "M(V)",
            5000:       "(V)",
            9000:       "M(X)",
            10000:      "(X)",
            40000:      "(X)(L)",
            50000:      "(L)",
            90000:      "(X)(C)",
            100000:     "(C)",
            400000:     "(C)(D)",
            500000:     "(D)",
            900000:     "(C)(M)",
            1000000:    "(M)"
        }

        self.Keys = []

        # Reverse them so they are in biggest to smallest.
        for key, value in self.Table.items():
            self.Keys.append(key)

        self.Keys.sort(reverse=True)

    # Convert the roman string to int.
    def _tointfromstring(self, arg):
        print("TO DO TO DO TO DO TO DO TO DO TO DO TO DO")

        return ""

    # Process the argument provided and set it to the local int.
    def _set_roman(self, arg):

        result = 0

        # Decide if the user passed a 'int' (number) or a 'string' (roman).
        try:
            result = int(arg)
        except ValueError:
                # It was a string so process that as a roman.
            result = self._tointfromstring(arg)

        return result

    # Init and have the user pass roman string or int.
    def __init__(self, arg):

        # Build a table to reference when converting to roman.
        self._GenerateConvertTable();

            # What stores the roman value.
        self.RomanValue = self._set_roman(arg)

    # Turns the self.RomanValue into a string.
    def _ConvertToRomainString(self, arg=None):
        #print("self {} arg {}".format(self.RomanValue, arg))

        # first?
        if arg == None:
            # special case, arg is 0.
            if self.RomanValue == 0:
                return "N"
            else:
                arg = self.RomanValue

        # if it is negative
        Special = ""
        if arg < 0:
            Special = "-"
            arg *= -1

        # edge case
        if arg == 0:
            return ""

        # loop through and look for a key that fits into the number.
        for key in self.Keys:
            if (arg - key) >= 0:
                #arg -= key
                #print("{} {}".format(arg, key))
                return "{}{}{}".format(Special, self.Table[key], self._ConvertToRomainString(arg - key))

        # If there is no key assume empty?
        return ""


    def __str__(self):
        return self._ConvertToRomainString()

        # Test equality.

    def __eq__(self, other):  # ==
        if self.RomanValue == other.RomanValue:
            return True
        else:
            return False

    def __ne__(self, other):  # !=
        if self.RomanValue != other.RomanValue:
            return True
        else:
            return False

    def __lt__(self, other):  # <
        if self.RomanValue < other.RomanValue:
            return True
        else:
            return False

    def __gt__(self, other):  # >
        if self.RomanValue > other.RomanValue:
            return True
        else:
            return False

    def __le__(self, other):  # <=
        if self.RomanValue <= other.RomanValue:
            return True
        else:
            return False

    def __ge__(self, other):  # >=
        if self.RomanValue >= other.RomanValue:
            return True
        else:
            return False

    def __neg__(self):  # -some_object
        return Roman(self.RomanValue * -1)

    def __add__(self, other):
        return Roman(self.RomanValue + other.RomanValue)

    def __sub__(self, other):
        return Roman(self.RomanValue - other.RomanValue)

    def __mul__(self, other):
        return Roman(self.RomanValue * other.RomanValue)

    def __floordiv__(self, other):  # //
        return Roman(self.RomanValue // other.RomanValue)

    def __truediv__(self, other): # /
        return Roman(self.RomanValue / other.RomanValue), Roman(self.RomanValue % other.RomanValue)

    def __pow__(self, other): # **
        return Roman(self.RomanValue ** other.RomanValue)


if __name__ == '__main__':
    print("Roman self test: Written by David Harkins.")

    III = Roman(3)
    VII = Roman(7)

    # Pure Roman operations.

    # X + Y
    print("III + VII (X): {}".format((III + VII)))
    # X - Y
    print("III - VII (-IV): {}".format((III - VII)))
    # X * Y
    print("III * VII (XXI): {}".format((III * VII)))
    # X / Y
    TrueDivision = (III / VII)
    print("III / VII ((N, III)): ({}, {})".format(TrueDivision[0], TrueDivision[1]))
    # X // Y
    print("III // VII (N): {}".format((III // VII)))
    # X ** Y
    print("III ** VII (MMCLXXXVII): {}".format((III ** VII)))
    # X == Y
    print("III == VII (False): {}".format((III == VII)))
    # X != Y
    print("III != VII (True): {}".format((III != VII)))
    # X < Y
    print("III < VII (True): {}".format((III < VII)))
    # X > Y
    print("III > VII (False): {}".format((III > VII)))
    # X <= Y
    print("III <= VII (True): {}".format((III <= VII)))
    # X >= Y
    print("III >= VII (False): {}".format((III >= VII)))
    # -X
    print("!(III) (-III): {}".format((-III)))


    # Roman plus int

    # X + 5
    print("III + 5 (X): {}".format((III + 5)))
    # X - 5
    print("III - 5 (-IV): {}".format((III - 5)))
    # X * 5
    print("III * 5 (XXI): {}".format((III * 5)))
    # X / 5
    TrueDivision = (III / 5)
    print("III / 5 ((N, III)): ({}, {})".format(TrueDivision[0], TrueDivision[1]))
    # X // 5
    print("III // 5 (N): {}".format((III // 5)))
    # X ** 5
    print("III ** 5 (MMCLXXXVII): {}".format((III ** 5)))
    # X == 5
    print("III == 5 (False): {}".format((III == 5)))
    # X != 5
    print("III != 5 (True): {}".format((III != 5)))
    # X < 5
    print("III < 5 (True): {}".format((III < 5)))
    # X > 5
    print("III > 5 (False): {}".format((III > 5)))
    # X <= 5
    print("III <= 5 (True): {}".format((III <= 5)))
    # X >= 5
    print("III >= 5 (False): {}".format((III >= 5)))






    SS = Roman(0)
    print(SS)