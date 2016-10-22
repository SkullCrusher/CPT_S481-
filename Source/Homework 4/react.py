from particle import Particle

class Nucleus(Particle):

    def __str__(self):
        return "({}){}".format(self.massNumber, self.sym)


class UnbalancedCharge(Exception):
    def __init__(self, diff):
        super(UnbalancedCharge, self).__init__(diff)

class UnbalancedNummber(Exception):
    def __init__(self, diff):
        super(UnbalancedNummber, self).__init__(diff)


em = Particle("e-", -1, 0)       # an electron
ep = Particle("e+", 1, 0)        # a positron
p = Particle("p", 1, 1)          # a proton
n = Particle("n", 0, 1)          # a neutron
nu_e = Particle("nu_e", 0, 0)    # a neutrino
gamma = Particle("gamma", 0, 0)  # a gamma particle

d = Nucleus("H", 1, 2)    # hydrogen
li6 = Nucleus("Li", 3, 6) # lithium
he4 = Nucleus("He", 2, 4) # helium

    # a single reaction.
class Reaction():

        # Return the [total_charge, total_mass]
    def _calculateTotalCharge(self, arg):
        tot_chg = 0
        tot_massNumber = 0

        for x in arg:
            tot_chg += x.chg
            tot_massNumber += x.massNumber

        return [tot_chg, tot_massNumber]

        # constructor.
    def __init__(self, left, right):

            # Calculate the total charge and total mass.
        LeftTotal = self._calculateTotalCharge(left)
        RightTotal = self._calculateTotalCharge(right)

            # Does the total charge match?
        if LeftTotal[0] != RightTotal[0]:
            raise UnbalancedCharge(abs(LeftTotal[0] - RightTotal[0]))

            # Does the total mass match?
        if LeftTotal[1] != RightTotal[1]:
            raise UnbalancedNummber(abs(LeftTotal[1] - RightTotal[1]))

            # set the values in place.
        self.left = left
        self.right = right

        # takes a tuple and turns it into a string.
    def _GenerateSide(self, arg):
        SideResult = ""

        # Build the left side.
        for x in arg:
            if SideResult == "":
                SideResult += str(x)
            else:
                SideResult += " + " + str(x)

        return SideResult

        # Generate the output like the following: (6)Li + (2)H -> (4)He + (4)He
    def __str__(self):
        return self._GenerateSide(self.left) + " -> " + self._GenerateSide(self.right)


     # The class to handle chain reactions.

class ChainReaction():


    def __init__(self, Name):
            # Create a empty place to store the reactions.
        self.StoredReactions = []
        self.ReactionName = Name
        pass

    def addReaction(self, ReactionToAdd):
        self.StoredReactions.append([ReactionToAdd])
        #print(self.StoredReactions)

    def CalculateNet(self):

        Result = "\nnet:\n"

            # Temp storage of the net reaction for both sides.
        lhsNet_Unclean = []
        rhsNet_Unclean = []

            # for each reaction split it apart.
        for x in self.StoredReactions:

            # print("X: {}".format(x[0]))
            #print(lhsNet_Unclean)

            lhsNet_Unclean.append(x[0].left[0])
            lhsNet_Unclean.append(x[0].left[1])

            rhsNet_Unclean.append(x[0].right[0])
            rhsNet_Unclean.append(x[0].right[1])

        print("{}\n{}".format(lhsNet_Unclean, rhsNet_Unclean))


        dupe = True
            # Remove the duplicates.
        while dupe:
            #print("CC:\n{}\n{}\n".format(lhsNet_Unclean, rhsNet_Unclean))

            dupe = False
            for i in range(0, len(lhsNet_Unclean)):
                for g in range(0, len(rhsNet_Unclean)):
                    if lhsNet_Unclean[i] == rhsNet_Unclean[g]:

                        print(lhsNet_Unclean[i],rhsNet_Unclean[g])

                        del lhsNet_Unclean[i]
                        del rhsNet_Unclean[g]
                        dupe = True
                        break

                if dupe == True:
                    break

        lhs_result = ""
        rhs_result = ""
        #print(lhsNet_Unclean[0].GenerateSide(lhsNet_Unclean[0]))

        #print(lhsNet_Unclean)

        for x in lhsNet_Unclean:
            if lhs_result == "":
                lhs_result += str(x)
            else:
                lhs_result += " + " + str(x)

        for x in rhsNet_Unclean:
            if rhs_result == "":
                rhs_result += str(x)
            else:
                rhs_result += " + " + str(x)


        return Result + lhs_result + " -> " + rhs_result



        # print out.
    def __str__(self):
        Result = self.ReactionName + " chain:"

        for x in self.StoredReactions:
            Result += "\n" + str(x[0]);

        Result += self.CalculateNet();

        return Result


# Part 1 [40]
# print(Reaction((li6, d), (he4, he4)))
# (6)Li + (2)H -> (4)He + (4)He
print(Reaction((li6, d), (he4, he4)))

# Part 2 [10]
# Extend particle class to have + operator acting on two particles
# which will result in a tuple containing them so that:
# print(Reaction(li6 + d, he4 + he4))
# print(Reaction((li6, d), (he4, he4)))
print(li6 + d)

# Part 3 [50]

# one of the principal reactions powering the Sun
he3 = Nucleus ( "He" , 2 , 3) # not defined above

chnPP = ChainReaction ( " proton - proton ( branch I ) " )
for rctn in ( Reaction (( p , p ) , (d , ep , nu_e )) ,
        Reaction (( p , p ) , (d , ep , nu_e )) ,
        Reaction (( d , p ) , ( he3 , gamma )) ,
        Reaction (( d , p ) , ( he3 , gamma )) ,
        Reaction (( he3 , he3 ) , ( he4 , p , p ))):
    chnPP . addReaction ( rctn )

#debugging.
print("\n")

print(chnPP)