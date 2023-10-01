# =============================================================================
# INF 502 - Group project 1 Basic Python Program
# Due: Wed Oct 25, 2023 11:59
# 
# Group members:
#     Varun Kumar Chilukuri
#     Skye Salganek
#     Johnathan Tenny
#
# =============================================================================

# define the main() function
def main():
    # prompt user to provide sequence 1
        # error if characters other than ACGT 
    # prompt user to provide sequence 2
        # error if characters other than ACGT 
    # prompt user to define the 'maximum shift'
        # error if greater than size of smallest chain
        # do chains need to be same size?
    # prompt user to choose between longest contiguous chain or most matches total

    #

# define seqMatch() function that calculates and print back the count of matches without
    # any shifts done as well as if there is any chained sequences present
    # (display them seperatly)

    return None

def seqMatch(seq1, seq2):

    # calculates and prints the number of matches in original sequences 
    matchCount = 0
    seqLength = min(len(seq1), len(seq2))
    for position in range(seqLength):
        if seq1[position] == seq2[position]:
            matchCount += 1
    print(f"The original un-shifted sequences contain {matchCount} positional nucleotide matches.")

    # calculates the longest consecutive matching chain and prints the length as well as the chain
    maxLength = 0
    maxStart = None
    maxEnd = None
    currentLength = 0
    currentStart = None
    for position in range(seqLength):
        if seq1[position] == seq2[position]:
            if currentLength == 0:
                currentStart = position
            currentLength += 1
            if currentLength > maxLength:
                maxLength =currentLength
                maxStart = currentStart
                maxEnd = position
        else:
            currentLength = 0

    maxChain = seq1[maxStart:maxEnd + 1]
    print(f"Longest consecutive matching chain: {maxChain} (Length: {maxLength})")
    return matchCount, maxLength, maxChain 



# define shiftMatch() function to calculate and print back the chain after shifts done with
    # maximum score from sequence provided as input through console

# define contChain() function to calculate and print back the maximum contiguous chain
    # (after shifts done ) from sequence provided as input through console

# define shiftChain() function to calculate and print back the chain after shifts done with maximum score

def shiftAndMatch(seq1,seq2,shiftAmount,verbose=False):
    # Compare two strings of characters for matches after shifting by a specified amount
    # Returns the total number of matches, a string containing matches only, and the two strings after matching
    matchCount = 0
    index = 0
    matchString = ''

    # Remove shiftAmount from end of seq1
    seq1_slice = seq1[:len(seq1)-shiftAmount]

    # Remove shiftAmount from start of seq2
    seq2_slice = seq2[shiftAmount:]

    # For each char in seq 1...
    for seq1_char in seq1_slice:

        # Get current char from seq2
        seq2_char = seq2_slice[index]

        # If the pair matches, add to total count of matches
        if seq1_char == seq2_char:
            matchCount += 1
            # Add the character to a string containing only the matching characters
            matchString += seq1_char

        # If the pair does not match, add a blank character
        else:
            matchString += ' '

        # Increment index
        index += 1

    # Return results as a list
    return [matchCount, matchString, seq1_slice, seq2_slice]

def getLongestChain(matchString):

    # Split on the blank spaces creating a list of lists containing each contiguous chain
    consecutiveMatches = matchString.split(' ')

    lenLongestChain = 0
    longestChainStr = ''

    # Search through the list of chains to find the longest
    for chain in consecutiveMatches:
        lenChain = len(chain)
        if lenChain > lenLongestChain:
            lenLongestChain = lenChain
            longestChainStr = chain

    return [lenLongestChain, longestChainStr]

def mostMatchesShiftAll(seq1,seq2,maxShift,verbose=False):
    # Test for most matches across all possible shift amounts in both directions
    mostMatches = 0


    # Search most matches while shifting seq2
    mostMatchesShiftSeq1 = False
    for shiftAmount in range(maxShift):
        matchCount, matchString, seq1_slice, seq2_slice = shiftAndMatch(seq1,seq2,shiftAmount,verbose=True)

        if matchCount > mostMatches:
            mostMatches = matchCount
            mostMatchesShiftAmt = shiftAmount
            mostMatchesSeq1 = seq1_slice
            mostMatchesSeq2 = seq2_slice
            mostMatchesMatching = matchString

        if verbose:
            print(f'Testing {shiftAmount} shift of seq2:')
            print('Matches:', matchString)
            print('   Seq1:', seq1_slice)
            print('   Seq2:', seq2_slice)
            print()

    # Test for most matches while shifting seq1
    for shiftAmount in range(maxShift):
        matchCount, matchString, seq1_slice, seq2_slice = shiftAndMatch(seq2, seq1, shiftAmount, verbose=True)

        if matchCount > mostMatches:
            mostMatches = matchCount
            mostMatchesShiftAmt = shiftAmount
            mostMatchesShiftSeq1 = True
            mostMatchesSeq1 = seq1_slice
            mostMatchesSeq2 = seq2_slice
            mostMatchesMatching = matchString

        if verbose:
            print(f'Testing {shiftAmount} shift of seq1:')
            print('Matches:', matchString)
            print('   Seq1:', seq1_slice)
            print('   Seq2:', seq2_slice)
            print()

    if mostMatches == 0:
        print('No matches were found')

    else:
        if mostMatchesShiftSeq1:
            print(f'The most total matches were found by shifting sequence 1 by {mostMatchesShiftAmt}')
        else:
            print(f'The most total matches were found by shifting sequence 2 by {mostMatchesShiftAmt}')

        print('Matches:', mostMatchesMatching)
        print('   Seq1:', mostMatchesSeq1)
        print('   Seq2:', mostMatchesSeq2)



def longestChainShiftAll(seq1,seq2,maxShift,verbose=False):
    # Test for longest chain across all possible shift amounts
    # Test for most matches across all possible shift amounts in both directions
    lenLongestChainAll = 0

    # Search longestChain while shifting seq2
    longestChainShiftSeq1 = False
    for shiftAmount in range(maxShift):
        matchCount, matchString, seq1_slice, seq2_slice = shiftAndMatch(seq1, seq2, shiftAmount)
        lenLongestChain, longestChainStr = getLongestChain(matchString)

        if lenLongestChain > lenLongestChainAll:
            lenLongestChainAll = lenLongestChain
            longestChainShiftAmt = shiftAmount
            longestChainMatching = matchString
            longestChainSeq1 = seq1_slice
            longestChainSeq2 = seq2_slice

        if verbose:
            print(f'Testing {shiftAmount} shift of seq2:')
            print('Matches:', matchString)
            print('   Seq1:', seq1_slice)
            print('   Seq2:', seq2_slice)
            print()

    # Test for longest chain while shifting seq1
    for shiftAmount in range(maxShift):
        matchCount, matchString, seq1_slice, seq2_slice = shiftAndMatch(seq2, seq1, shiftAmount)
        lenLongestChain, longestChainStr = getLongestChain(matchString)

        if lenLongestChain > lenLongestChainAll:
            lenLongestChainAll = lenLongestChain
            longestChainShiftSeq1 = True
            longestChainShiftAmt = shiftAmount
            longestChainMatching = matchString
            longestChainSeq1 = seq1_slice
            longestChainSeq2 = seq2_slice

        if verbose:
            print(f'Testing {shiftAmount} shift of seq1:')
            print('Matches:', matchString)
            print('   Seq1:', seq1_slice)
            print('   Seq2:', seq2_slice)
            print()

    if lenLongestChainAll == 0:
        print('No matches were found')

    else:
        
        if longestChainShiftSeq1:
            print(f'The longest chain was found by shifting sequence 1 by {longestChainShiftAmt}')
        else:
            print(f'The longest chain was found by shifting sequence 2 by {longestChainShiftAmt}')

        print('Matches:', longestChainMatching)
        print('   Seq1:', longestChainSeq1)
        print('   Seq2:', longestChainSeq2)

# Exception handling: Your code must handle all exception types raised, and do so by
    # accounting for specific exception types. So "no except:" or "except Exception:
    # clauses". Use exact error messaging and communicate back appropriately.

# test seqMatch() function
if __name__ == "__main__":
    seq1 = "ACGTTACCCGTC"
    seq2 = "GCTTCACTGTTA"
    maxShift = 10
    #seqMatch(seq1, seq2)
    #mostMatchesShiftAll(seq1,seq2,maxShift,verbose=True)
    longestChainShiftAll(seq1,seq2,maxShift,verbose=True)
