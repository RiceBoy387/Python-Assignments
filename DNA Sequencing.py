"""CSCA08 Assignment 0, Fall 2017
 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus
 Name: Justin Lyn
 UtorID: lynjust2
 Student Number: 1004178301
 Date: October 6/2017
"""


def split_input(sequence):
    '''(str) -> list
    This function is designed to take in a dna sequence and then seperate
    it into the upstream data, gene, and downstream data. It will return these
    values in a single list.
    REQ: sequence (In all caps and containing only letters 'C' 'T' 'G' 'A')
    >>> split_input("CGTAATGCGTATGCGAT")
    ['CGTA', 'ATGCGT', 'ATGCGAT']
    >>> split_input("AGTCGACAGT")
    ['AGTCGACAGT', '', '']
    '''
    # Use the find method to figure out at what index val the gene starts
    gene = sequence.find("ATG")
    # Obtain the up stream part of sequence
    up_stream = sequence[0:gene]
    # Check to see at what index next gene starts
    next_gene = sequence.find("ATG", (gene+2))
    # Obtain the down stream part of the sequence
    # Use if statement incase no down stream
    if next_gene == -1:
        down_stream = ''
        # If no down stream make sure dna_gene goes to the end of the sequence
        dna_gene = sequence[gene:len(sequence)]
    else:
        down_stream = sequence[(next_gene):len(sequence)]
        # If there is down stream dna_gene only goes up until the down_stream
        dna_gene = sequence[gene:next_gene]
    # If there is no gene everything goes to up stream
    if gene == -1:
        dna_gene = ''
        up_stream = sequence[0:len(sequence)]
    # Store the up stream, dna gene, and donwstream in a list to return
    split_sequence = [up_stream, dna_gene, down_stream]
    # return the list
    return split_sequence


def get_gene(sequence):
    '''(str) -> str
    This function is designed to find a gene in a given sequence and return
    that gene. If no gene is found then it will return ERROR
    REQ: sequence (In all caps and containing only letters 'C' 'T' 'G' 'A')
    >>> get_gene("GTACCATGCGGTGATGATC")
    'ATGCGGTG'
    >>> get_gene("AGTCAGTAGCTA")
    'ERROR'
    '''
    # Call the split_input function to get the gene
    s_input = split_input(sequence)
    # Set the variable to the gene
    dna_gene = s_input[1]
    # Use if statement to determine whether to return the gene or an Error
    if dna_gene == '':
        is_gene = "ERROR"
    else:
        is_gene = dna_gene
    # Return whether gene or Error
    return is_gene


def validate_gene(gene):
    '''(str) -> bool
    This function is designed to return whether or not the given gene is
    valid. Based on the paramaters it starts with 'ATG' contains a following
    codon, the codons are full, and there are no 4 consecutive nucleotides
    REQ: gene (In all caps and containing only letters 'C' 'T' 'G' 'A')
    >>> validate_gene("ATGGCATATACT")
    True
    >>> validate_gene("ATGAAAATC")
    False
    '''
    # Create a variable to store whether or not the gene is valid
    valid_gene = True
    # Check to see if the gene starts with ATG and set valid_gene to it
    valid_gene = valid_gene*(gene.startswith("ATG"))
    # Check to see if the gene has 6 or more nucleotides
    if len(gene) >= 6:
        valid_gene = valid_gene*1
    else:
        valid_gene = valid_gene*0
    # Check to see that the codons are complete
    if len(gene) % 3 == 0:
        valid_gene = valid_gene*1
    else:
        valid_gene = valid_gene*0
    # Check to make sure there isnt 4 consecutive nucleotides
    a = gene.find("AAAA")
    g = gene.find("GGGG")
    c = gene.find("CCCC")
    t = gene.find("TTTT")
    # Use if statement to determine whether or not the gene is valid
    # Since .find() return -1 when false that means it didn't find
    # 4 consecutive nucleotides and gene is valid
    if (a == -1 and g == -1 and c == -1 and t == -1):
        valid_gene = valid_gene*1
    else:
        valid_gene = valid_gene*0
    # Return whether or not the gene is valid
    return (valid_gene == 1)


def is_palindromic(gene):
    '''(str) -> bool
    This function is designed to figure out whether or not a gene
    is palindromic (the same in reverse) and if it is it will return True
    REQ: gene (In all caps and containing only letters 'C' 'T' 'G' 'A')
    >>> is_palindromic("ATGAGAGTA")
    True
    >>> is_palindromic("ATGAGAGTAAGT")
    False
    '''
    # Cast the gene into two different lists
    genelist = list(gene)
    backwards = list(gene)
    # Reverse the list so we can compare and see if palindromic
    backwards.reverse()
    # Return bool value of whether or not the gene is palindromic
    return(genelist == backwards)


def evaluate_sequence(sequence):
    '''(str) -> str
    This function is designed to output whether or not a gene is found,
    is valid, is invalid, or is palindromic and valid. All the criteria
    is based on previous functions: get_gene, validate_gene, and
    is_palindromic
    REQ: sequence (In all caps and containing only letters 'C' 'T' 'G' 'A')
    >>> evaluate_sequence("ATGGTA")
    'Valid Palindromic Gene Found'
    >>> evaluate_sequence("ATGGGGTAT")
    'Invalid Gene'
    '''
    # Check to see if theres even a gene
    if_gene = get_gene(sequence)
    # Use if statement to determine what to output
    # If there is no gene found
    if if_gene == 'ERROR':
        evaluate = "No Gene Found"
    else:
        # Check if the gene is valid
        # Send it over to the validate_gene function to see
        val_gene = validate_gene(if_gene)
        # Cast val_gene since its a bool
        valid_gene = str(val_gene)
        # Determine what to output when the gene is found
        if valid_gene == "True":
            # Check to see if the valid gene is also palindromic
            # Send valid gene to the palindromic function
            pal_gene = is_palindromic(if_gene)
            # Cast palin_gene to a string
            palin_gene = str(pal_gene)
            # If the gene is valid and palindromic
            if palin_gene == "True":
                evaluate = "Valid Palindromic Gene Found"
            # If the gene is valid but not palindromic
            else:
                evaluate = "Valid Gene Found"
        # If the gene is invalid
        else:
            evaluate = "Invalid Gene"
    # Return the gene evaluation
    return evaluate
