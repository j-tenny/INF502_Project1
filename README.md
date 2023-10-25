# DNA Similarity analysis in Python
## Overview
This project involves writing a Python program to compare two DNA sequences and measure their similarity using two methods - number of matches and maximum contiguous chain. The program lets user to select parameters, read input sequences from console or file, handle exceptions, and neatly print the results.
The program takes as input two DNA sequences, directly via user from files. 
### Algorithm Design
The key algorithms needed are:

- NUMBER OF MATCHES
  - Align sequences
  - Count number of positions where characters are equal
- MAXIMUM CONTIGUOUS CHAIN
  - Align sequences
  - Identify longest subsequence where characters match contiguously
- APPLY SHIFTS
  - Loop through different shift values
  - Shift one sequence left/right and align with other
  - Calculate number of matches and maximum chain for each shift
  - Return best shift, number of matches and maximum chain

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
python INF502Project1Group10.py
```
The user is prompted to enter the file paths for two DNA sequence text files. For example:
```
Please enter the file path to your .txt containing your first DNA sequence: sequence1.txt
Sequence 1 contents:
CTAGTTGACG
Please enter the file path to your .txt containing your second DNA sequence: sequence2.txt
Sequence 2 contents:
TGGATTTGTG
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

## Conclusion
Our program does comparison of two detected DNA sequences and analyzes their similarity.
For similarity we will check the counts of simple metrics – number of matching nucleotides and length of the longest matching subsequence.
The user provides the input DNA sequences via text files and defines a parameter for maximum shift amount. The program then aligns the sequences with different shifts up to the max and calculates the similarity scores. The optimal alignments with maximum matches and longest chain are printed.

The core innovation is in allowing the sequences to be aligned by sliding them relatively to each other. This approaches simulates the matching process that could occur if the sequences had been inserted/deleted at various points. Instead of simply doing a fixed alignment, the program will try out various alignments and choose the best one according to metrics that we will define. This high level functionality required developing lower level functionality such as slicing and shifting strings programmatically.

Additionally, a key technical feature in this program is that the user interface validates user input and handles exceptions. User Input is tightly controlled via FileChooser classes, which only allow appropriate file selection. The file reading technique validates the characters read ( A,C,G,T) and the program acts accordingly on the detected characters. Any errors that may occur are caught and handled allowing the program to operate more smoothly.

The code’s structure is modular and follows sound programming principles. The main functions are clearly separated into logical modules each with clear inputs and outputs. There is a clear function devoted to reading the sequences and one devoted to calculating base scores and something just to shifts and something just to output. An attempt was clearly made to break things up into logical parts and make things readable.

This is a simple project but covers a number of foundational python skills: string manipulation, loops, conditionals, functions, and saving text to a file. It dumps a lot of requirements and details on the student, and requires them to think through the requirements, design logical algorithm, then translate those algorithms to working code. They must go from organizing and receiving input, to performing a large amount of computation in loops, to presenting output/results in a clear and organized fashion, and even saving text to a file.

The goal of this project is to get started with basic DNA similarity. However, it can be thought of as a gentle pedagogical introduction to working with DNA sequences programmatically. There is a lot of scope to build on this foundation, including getting into more advanced molecular biology and machine learning approaches. The skills that are developed in this project are transferable across many technical fields.

**NOTE: THIS PROJECT IS OPEN-SOURCE.**
