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

import sys
# define the main() function
def main():
    seq1, seq2, maxShift, verbose = userInputs()
    seqMatch(seq1, seq2, verbose=verbose)
    if maxShift > 0:
        mostMatchesShiftAll(seq1, seq2, maxShift, verbose=verbose)
        longestChainShiftAll(seq1, seq2, maxShift, verbose=verbose)

    return None

def userInputs():



    print('How would you like to input sequences?')
    print('[1] Input manually through console')
    print('[2] Input file names and read sequence from file')
    print()
    input_type = input('Type 1 or 2: ').strip()
    print()
    while input_type != '1' and input_type != '2':
        print('Input not recognized. Select option 1 or 2.')
        print()
        input_type = input('Type 1 or 2: ').strip()
        print()


    print('Would you like to see detailed outputs? (Not recommended for large files)')
    print('[1] Print detailed outputs')
    print('[2] Suppress detailed outputs')
    print()
    verbose_selection = input('Type 1 or 2: ').strip()
    print()
    while verbose_selection != '1' and verbose_selection != '2':
        print('Input not recognized. Select option 1 or 2.')
        print()
        verbose_selection = input('Type 1 or 2: ').strip()
        print()

    if verbose_selection=='1':
        verbose = True
    else:
        verbose = False


    def isValidSequence(sequence):
        validChars = {'A', 'C', 'G', 'T'}
        return all(char in validChars for char in sequence)


    # prompt user to provide sequence 1
    seq1 = ""
    seq2 = ""


    if input_type=='1':

    # Console input option
        print()
        seq1 = input("Input sequence containing characters ACTG:")
        print()

        while True:
            if isValidSequence(seq1):
                if len(seq1)>0:
                    if verbose:
                        print("Sequence 1 contents:")
                        print(seq1)
                        print('')
                    else:
                        print('Sequence 1 accepted')
                    break
                else:
                    print('Error: Sequence should not be empty.')
                    print()
                    seq1 = input("Input sequence containing characters ACTG:")
                    print()

            # error if characters other than ACGT
            else:
                print("Error: Invalid characters found in sequence 1.")
                print("Nucleotide sequences should only contain characters 'A', 'C', 'G', 'T'. ")
                print()
                seq1 = input("Input sequence containing characters ACTG:")
                print()


        # prompt user to provide sequence 2
        print()
        seq2 = input("Input sequence containing characters ACTG:")
        print()
        while True:
            if isValidSequence(seq2):
                if len(seq2)>0:
                    if verbose:

                        print("Sequence 2 contents:")
                        print(seq2)
                        print('')
                    else:
                        print('Sequence 2 accepted')
                    break
                else:
                    print('Error: Sequence should not be empty.')
                    print()
                    seq2 = input("Input sequence containing characters ACTG:")
                    print()
            # error if characters other than ACGT
            else:
                print("Error: Invalid characters found in sequence 2.")
                print("Nucleotide sequences should only contain characters 'A', 'C', 'G', 'T'. ")
                print()
                seq2 = input("Input sequence containing characters ACTG:")
                print()


    else:
    # File Input Option
        while not seq1:
            try:
              print()
              filePath1 = input("Please enter the file path to your .txt containing your first DNA sequence: ")
              print()
              try:
                  with open(filePath1, 'r') as file:
                      seq1 = file.read()
              except FileNotFoundError:
                print(f"The file '{filePath1}' was not found. Try again!")
              except Exception as e:
                print(f"An error occurred: {e}")
            except KeyboardInterrupt:
              print("User interrupted the input. Program exited.")
              sys.exit() # Exit the program
        while True:
            if isValidSequence(seq1):
                if verbose:
                    print("Sequence 1 contents:")
                    print(seq1)
                    print('')
                else:
                    print('Sequence 1 accepted')

                break
            # error if characters other than ACGT
            else:
              print("Error: Invalid characters found in sequence 1.")
              print("Nucleotide sequences should only contain characters 'A', 'C', 'G', 'T'. ")
              print()
              filePath1 = input("Please try again. Enter the file path to your first DNA sequence: ")
              print()
              try:
                with open(filePath1, 'r') as file:
                  seq1 = file.read()
              except FileNotFoundError:
                print(f"The file '{filePath1}' was not found. Try again!")
              except Exception as e:
                print(f"An error occurred: {e}")
              except KeyboardInterrupt:
                print("User interrupted the input. Exiting.")
                sys.exit() # Exit the program


        # prompt user to provide sequence 2
        seq2 = ""
        while not seq2:
            try:
              print()
              filePath2 = input("Please enter the file path to your .txt containing your second DNA sequence: ")
              print()
              try:
                  with open(filePath2, 'r') as file:
                      seq2 = file.read()
              except FileNotFoundError:
                print(f"The file '{filePath2}' was not found. Try again!")
              except Exception as e:
                print(f"An error occurred: {e}")
            except KeyboardInterrupt:
              print("User interrupted the input. Program exited.")
              sys.exit() # Exit the program
        while True:
            if isValidSequence(seq2):
                if verbose:

                    print("Sequence 2 contents:")
                    print(seq2)
                    print('')
                else:
                    print('Sequence 2 accepted')
                break
            # error if characters other than ACGT
            else:
              print("Error: Invalid characters found in sequence 2.")
              print("Nucleotide sequences should only contain characters 'A', 'C', 'G', 'T'. ")
              print()
              filePath2 = input("Please try again. Enter the file path to your second DNA sequence: ")
              print()
              try:
                with open(filePath2, 'r') as file:
                  seq2 = file.read()
              except FileNotFoundError:
                print(f"The file '{filePath2}' was not found. Try again!")
              except Exception as e:
                print(f"An error occurred: {e}")
              except KeyboardInterrupt:
                print("User interrupted the input. Exiting.")
                sys.exit() # Exit the program

# prompt user to define the 'maximum shift'
    while True:
        try:
            print()
            shiftAmount = input('Maximum shift to evaluate when matching nucleotides between sequences: ')
            print()
            maxShift = int(shiftAmount)
            if maxShift < 0:
                raise ValueError("Maximum shift value must be a positive integer.")

            # error if greater than size of smallest chain
            if maxShift > min(len(seq1), len(seq2)):
                raise ValueError("Maximum shift exceeds length of sequences. Try a smaller shift: ")

            break

        except ValueError as e:
            print(e)
            print("Try again with a valid maximum shift value.")

        except Exception as e:
            print(f"An unknown error occurred: {e}")
            sys.exit()  # Exit the program

    return seq1, seq2, maxShift, verbose

# define seqMatch() function that calculates and print back the count of matches without
    # any shifts done as well as if there is any chained sequences present
    # (display them seperatly)
def seqMatch(seq1, seq2, verbose=False):

    # calculates and prints the number of matches in original sequences
    matchCount = 0
    matches=''
    seqLength = min(len(seq1), len(seq2))
    for position in range(seqLength):
        if seq1[position] == seq2[position]:
            matchCount += 1
            matches+=seq1[position]
        else:
            matches+=' '
    print('')
    print('')
    print('----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----')
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
    print(f"Longest chain: {maxChain} (Length: {maxLength})")
    print("")
    if verbose:
        print('Matches:', matches)
        print('   Seq1:', seq1)
        print('   Seq2:', seq2)
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

        if index == len(seq2_slice):
            break

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

    # initialization message
    print('')
    print('')
    print('----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----')
    print('Testing for the most matches across all possible shift amounts in both directions...')
    print('')

    mostMatches = 0


    # Search most matches while shifting seq2
    mostMatchesShiftSeq1 = False
    for shiftAmount in range(1, maxShift+1):
        matchCount, matchString, seq1_slice, seq2_slice = shiftAndMatch(seq1,seq2,shiftAmount,verbose=True)

        if matchCount > mostMatches:
            mostMatches = matchCount
            mostMatchesShiftAmt = shiftAmount
            mostMatchesSeq1 = seq1_slice
            mostMatchesSeq2 = seq2_slice
            mostMatchesMatching = matchString

        if verbose:
            print(f'Testing {shiftAmount} shift of seq2:')
            print(f"{shiftAmount} shift of seq2 results in {matchCount} nucleotide matches.")
            print('Matches:', matchString)
            print('   Seq1:', seq1_slice)
            print('   Seq2:', seq2_slice)
            print()

    # Test for most matches while shifting seq1
    for shiftAmount in range(1,maxShift+1):
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
            print(f"{shiftAmount} shift of seq1 results in {matchCount} nucleotide matches.")
            print('Matches:', matchString)
            print('   Seq1:', seq1_slice)
            print('   Seq2:', seq2_slice)
            print()

    if mostMatches == 0:
        print('No matches were found')

    else:
        if mostMatchesShiftSeq1:
            print(f'The most matches were found by shifting sequence 1 by {mostMatchesShiftAmt}')
            print(f"The result is {mostMatches} nucleotide matches.")
        else:
            print(f'The most matches were found by shifting sequence 2 by {mostMatchesShiftAmt}')
            print(f"The result is {mostMatches} nucleotide matches.")



        if verbose:
            print('Matches:', mostMatchesMatching)
            print('   Seq1:', mostMatchesSeq1)
            print('   Seq2:', mostMatchesSeq2)
        print('')



def longestChainShiftAll(seq1,seq2,maxShift,verbose=False):
    # Test for longest chain across all possible shift amounts
    # Test for most matches across all possible shift amounts in both directions

    # initialization message
    print('')
    print('')
    print('----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----')
    print('Testing for longest matching nucleotide chain...')
    print('')

    lenLongestChainAll = 0
    ChainSeq2 = ''
    ChainSeq1 = ''

    # Search longestChain while shifting seq2
    longestChainShiftSeq1 = False
    for shiftAmount in range(1,maxShift+1):
        matchCount, matchString, seq1_slice, seq2_slice = shiftAndMatch(seq1, seq2, shiftAmount)
        lenLongestChain, longestChainStr = getLongestChain(matchString)


        if lenLongestChain > lenLongestChainAll:
            lenLongestChainAll = lenLongestChain
            ChainSeq2 = longestChainStr
            longestChainShiftAmt = shiftAmount
            longestChainMatching = matchString
            longestChainSeq1 = seq1_slice
            longestChainSeq2 = seq2_slice

        if verbose:
            print(f'Testing {shiftAmount} shift of seq2:')
            print(f"Longest chain: {longestChainStr} (Length: {lenLongestChain})")
            print('Matches:', matchString)
            print('   Seq1:', seq1_slice)
            print('   Seq2:', seq2_slice)
            print()

    # Test for longest chain while shifting seq1
    for shiftAmount in range(1, maxShift+1):
        matchCount, matchString, seq1_slice, seq2_slice = shiftAndMatch(seq2, seq1, shiftAmount)
        lenLongestChain, longestChainStr = getLongestChain(matchString)

        if lenLongestChain > lenLongestChainAll:
            lenLongestChainAll = lenLongestChain
            ChainSeq2 = longestChainStr
            longestChainShiftSeq1 = True
            longestChainShiftAmt = shiftAmount
            longestChainMatching = matchString
            longestChainSeq1 = seq1_slice
            longestChainSeq2 = seq2_slice

        if verbose:
            print(f'Testing {shiftAmount} shift of seq1:')
            print(f"Longest chain: {longestChainStr} (Length: {lenLongestChain})")
            print('Matches:', matchString)
            print('   Seq1:', seq1_slice)
            print('   Seq2:', seq2_slice)
            print()

    if lenLongestChainAll == 0:
        print('No matches were found')

    else:

        if longestChainShiftSeq1:
            print(f'The longest matching chain was found by shifting sequence 1 by {longestChainShiftAmt}')
            print(f"Longest chain: {ChainSeq1} (Length: {lenLongestChainAll})")
        else:
            print(f'The longest matching chain was found by shifting sequence 2 by {longestChainShiftAmt}')
            print(f"Longest chain: {ChainSeq2} (Length: {lenLongestChainAll})")

        if verbose:
            print('Matches:', longestChainMatching)
            print('   Seq1:', longestChainSeq1)
            print('   Seq2:', longestChainSeq2)

# Exception handling: Your code must handle all exception types raised, and do so by
    # accounting for specific exception types. So "no except:" or "except Exception:
    # clauses". Use exact error messaging and communicate back appropriately.

# test seqMatch() function
if __name__ == "__main__":
    main()
    #seq1 = "ACGTTACCCGTC"
    #seq2 = "GCTTCACTGTTA"
    #maxShift = 10
    #seq1, seq2, maxShift = userInputs()
    #seqMatch(seq1, seq2)
    #mostMatchesShiftAll(seq1,seq2,maxShift,verbose=True)
    #longestChainShiftAll(seq1,seq2,maxShift,verbose=True)
