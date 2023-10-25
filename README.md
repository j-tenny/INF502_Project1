# DNA Similarity analysis in Python
## Overview
This project involves writing a Python program to compare two DNA sequences and measure their similarity using two methods - number of matches and maximum contiguous chain. The program lets user to select parameters, read input sequences from console or file, handle exceptions, and neatly print the results.
The program takes as input two DNA sequences, directly via user from files. 
There are two straightforward measures:

- NUMBER OF MATCHES
- MAXIMUM CONTIGUOUS CHAIN

## Implementation
The program is structured into the following key functions:


#### `userInputs()`
Prompts the user to input the sequences from files and define the maximum shift amount.

- Requests file path for Sequence 1, opens file, and reads contents into a string variable seq1
- Validates sequence characters are A, C, G or T, prints error if not
- Repeats file input until valid sequence entered
- Requests file path for Sequence 2, reads into seq2
- Validates sequence 2 characters
- Requests user input for maximum shift as an integer maxShift
- Validates maxShift is positive and less than sequence lengths
  
#### `seqMatch()`
Calculates basic similarity scores before shifts:

- Counts number of positions where seq1 and seq2 match
- Finds longest contiguous matching substring
- Prints number of total matches and longest contiguous chain details
  
#### `shiftAndMatch()`
Compares two sequences after shifting one by specified amount:

- Slices seq1 and seq2 to shift one by given amount
- Iterates through aligned sequences counting matches
- Returns number of matches and concatenated string of just matches
  
#### `getLongestChain()`
Finds longest contiguous matching chain from a string of matches/non-matches.

- Splits string on spaces into list of chains
- Finds longest chain in list
- Returns length of longest chain and the chain string
  
#### `mostMatchesShiftAll()`
Finds most total matches across all possible shifts up to max:

- Loops shiftAndMatch() up to maxShift trying shifts of seq1
- Tracks highest number of matches and associated shift amount
- Repeats for shifts of seq2
- Prints best alignment with most matches
  
#### `longestChainShiftAll()`
Finds longest contiguous chain across all possible shifts:

- Calls shiftAndMatch() up to maxShift to get matches string
- Uses getLongestChain() to find longest chain from matches
- Tracks longest chain and associated shift amount
- Repeats for shifts of both sequences
- Prints best alignment with longest contiguous chain
  
#### Exception handling
Uses specific except blocks for common errors like TypeError, FileNotFoundError, ValueError, and IndexError
Prints descriptive error messages for user

- TypeError - invalid sequence characters
- IndexError - sequences not of equal length
- FileNotFoundError - file not found
- ValueError - invalid shift size

## Usage

The program can be run as:
```python
python dna_similarity.py
```
The user is prompted to enter the file paths for two DNA sequence text files. For example:
```
Please enter the file path to your .txt containing your first DNA sequence: sequence1.txt
Please enter the file path to your .txt containing your second DNA sequence: sequence2.txt
```
The contents of file should contain only the characters A, C, G and T representing a DNA sequence with correct file path. Otherwise, exceptions are raised.

After the sequences are entered, the user is asked for a maximum shift amount:
```
Maximum shift to evaluate when matching nucleotides between sequences: 1
```
The maximum shift should be only positve integer.
The program then prints the basic similarity scores before any shifts. For example:
```
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
The original un-shifted sequences contain 3 positional nucleotide matches.
Longest chain: TT (Length: 2)
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
Testing for the most matches across all possible shift amounts in both directions...

Testing 1 shift of seq2:
1 shift of seq2 results in 3 nucleotide matches.
Matches:     TT   G
   Seq1: CTAGTTGACG
   Seq2: TGGATTTGTG

Testing 1 shift of seq1:
1 shift of seq1 results in 3 nucleotide matches.
Matches:     TT   G
   Seq1: TGGATTTGTG
   Seq2: CTAGTTGACG

The most matches were found by shifting sequence 2 by 1
The result is 3 nucleotide matches.
Matches:     TT   G
   Seq1: CTAGTTGACG
   Seq2: TGGATTTGTG
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
Testing for longest matching nucleotide chain...

Testing 1 shift of seq2:
Longest chain: TT (Length: 2)
Matches:     TT   G
   Seq1: CTAGTTGACG
   Seq2: TGGATTTGTG

Testing 1 shift of seq1:
Longest chain: TT (Length: 2)
Matches:     TT   G
   Seq1: TGGATTTGTG
   Seq2: CTAGTTGACG

The longest matching chain was found by shifting sequence 2 by 1
Longest chain: TT (Length: 2)
Matches:     TT   G
   Seq1: CTAGTTGACG
   Seq2: TGGATTTGTG
```


