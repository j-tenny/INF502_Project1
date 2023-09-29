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

# define seqMatch() function that calculates and print back the count of matches without
    # any shifts done as well as if there is any chained sequences present
    # (display them seperatly)

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

# test seqMatch() function
if __name__ == "__main__":
    seq1 = "ACGTTACCCGTC"
    seq2 = "GCTTCACTGTTA"
    seqMatch(seq1, seq2)    

# define shiftMatch() function to calculate and print back the chain after shifts done with
    # maximum score from sequence provided as input through console

# define contChain() function to calculate and print back the maximum contiguous chain
    # (after shifts done ) from sequence provided as input through console

# define shiftChain() function to calculate and print back the chain after shifts done with maximum score
    # from sequence provided as input through file (filename still will be provided
    # through input)

# define shiftContChain() function to calculate and print back the maximum contiguous chain (after shifts done ) from
    # sequence provided  as input through file (filename still will be provided through
    # input)

# Exception handling: Your code must handle all exception types raised, and do so by
    # accounting for specific exception types. So "no except:" or "except Exception:
    # clauses". Use exact error messaging and communicate back appropriately.
