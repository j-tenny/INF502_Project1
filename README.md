# DNA Similarity analysis in Python
## Overview
This project implements a DNA sequence similarity analysis algorithm in Python. It allows the user to calculate two similarity metrics - number of matches and maximum contiguous chain between two DNA sequences, either provided interactively or from files.
Here is a sample README.md for your Python DNA similarity project repository:

## Description

The program takes as input two DNA sequences, directly via user from files. 
There are two straightforward measures:

- NUMBER OF MATCHES
- MAXIMUM CONTIGUOUS CHAIN

### Number of Matches:

Number of matches between the two sequences after shifting them to find the maximum matches. The user need to input the maximum shift value to makesure to not shift more than set shift value.

### Maximum Contiguos Chain:

Maximum contiguous matching chain between the two sequences after shifting.

The results are printed out for the user.

## Usage

The program provides a simple interactive menu:

1. Set maximum shift value
2. Load sequences from files
4. Quit

Once the maximum shift is set, the user can choose to load them from files. 

The similarity metrics are calculated and printed out.

## Approach

Approach was to break the problem down into smaller logical pieces:

- Read input sequences from files 
- Functions to shift sequences by a given amount
- Function to count exact matches after shifts
- Function to find maximum contiguous chain after shifts
- Interactive menu
- Handling file input and exceptions
