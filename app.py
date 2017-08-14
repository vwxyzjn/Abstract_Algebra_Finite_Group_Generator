# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 12:21:04 2017

@author: shuang
"""
from typing import List
import numpy as np
import itertools
import time


def get_permutations_of_list(set_symbols: List):
    """
    This function generates all the permutations of
    a list.
    
    Note:
        This function uses the concept of cartesian product.
        For more information, check out
        https://stackoverflow.com/questions/31630971/permutations-on-2d-lists-python

    Args:
        set_symbols(List): a list of integers

    Return:
        List: a list of all permutations of ``input_list``
    """
    set_range  = [set_symbols] * len(set_symbols)
    all_permutations = []

    for element in itertools.product(*set_range):
        all_permutations += [element]
        
    return all_permutations

def check_associativity(matrix: List, set_symbols: List):
    """
    This function checks the associativity of the
    given matrix(a representation of binary operations).
    
    For example, given a 3x3 matrix ::
    
        matrix = (
            (0, 0, 2), 
            (0, 0, 1), 
            (1, 2, 0)
        )
        array = np.array(matrix)
    
    and a particular permutation of set symbols::
        
        (1, 0, 2)
        
    we check whether array[array[1][0], 2] == array[1, array[0][2]],
    that is, whether f(f(a, b), c) == f(a, f(b, c))
    
    And then we check every possible permutation of ``set_symbols``
    
    Args:
        matrix(List or Tuple): a list of matrix rows. For example::
            
            matrix = ((0, 0, 2), (0, 0, 1), (1, 2, 0))
            
        set_symbols(List): all symbols in the set
    """
    array = np.array(matrix)
    all_permutations = get_permutations_of_list(set_symbols)
    for permutation in all_permutations:
        a = permutation[0]
        b = permutation[1]
        c = permutation[2]
        if not array[array[a][b], c] == array[a, array[b][c]]:
            return {
                "result": False,
                "a,b,c": [a, b, c]
            }
        
    return {
        "result": True
    }

def check_identity_element(matrix: List, set_symbols: List):
    """
    This function checks if there exists an $e$ such that
    
    $$e * x == x * e == x $$
    
    for all x in ``set_symbols``
    
    """
    array = np.array(matrix)
    for e in set_symbols:
        for x in set_symbols:
           if not array[e][x] == array[x][e] == x:
                return {
                    "result": False
                }
        
        # if this ``e`` passes all the test, return it.
        return {
            "result": True,
            "identity_number": e
        }

def check_inverse(matrix: List, set_symbols: List, identity_element: int):
    """
    This function checks if for each $a$ in ``set_symbols``,
    there is an $a'$ in ``set_symbols`` such that
    
    $$a * a' == a' * a == e$$
    
    
    """
    array = np.array(matrix)
    for a in set_symbols:
        found = False
        for a_prime in set_symbols:
            if array[a][a_prime] == array[a_prime][a] == identity_element:
                found = True
        
        # if a couldn't find a corresponding a_prime, then return false.
        if not found:
            return {
                "result": False,
                "a": [a]
            }
        
    # if this ``e`` passes all the test, return it.
    return {
        "result": True
    }


def check_group(set_symbols: List):
    
    # get all matrix permutations
    row_permutations = get_permutations_of_list(set_symbols)
    my_set_rows =[row_permutations] * len(set_symbols)
    group_count = 0
    for permutation in itertools.product(*my_set_rows):
    
        return_result = check_associativity(permutation, set_symbols)
        if return_result['result'] == False:
            continue
        
        return_result = check_identity_element(permutation, set_symbols)
        if return_result['result'] == False:
            continue
        
        return_result = check_inverse(permutation, set_symbols, return_result['identity_number'])
        if return_result['result'] == False:
            continue
        
        print('valid group', permutation)
        group_count += 1
        
    return group_count



set_symbols = [0,1,2]
check_group(set_symbols)

start_time = time.time()
check_group([0,1,2,3])
print("--- %s seconds ---" % (time.time() - start_time))


"""
The following are test cases, some examples are retrieved from
https://en.wikibooks.org/wiki/Abstract_Algebra/Group_tables
"""


def test_check_associativity():
    matrix1 = (
        (1, 2, 3, 0),
        (2, 3, 0, 1),
        (3, 0, 1, 2),
        (0, 1, 2, 3)
    )
    assert check_associativity(matrix1, [0, 1, 2, 3])['result'] == True
    
    matrix2 = (
        (1, 2, 3, 0),
        (2, 4, 0, 1),
        (3, 0, 1, 2),
        (0, 1, 2, 3)
    )
    assert check_associativity(matrix2, [0, 1, 2, 3])['result'] == False
    
    matrix3 = (
        (0, 1, 2),
        (1, 2, 0),
        (2, 0, 1)
    )
    assert check_associativity(matrix3, [0, 1, 2])['result'] == True
    
def test_check_identity_element():
    matrix3 = (
        (0, 1, 2),
        (1, 2, 0),
        (2, 0, 1)
    )

    assert check_identity_element(matrix3, [0,1,2])['result'] == True
    assert check_identity_element(matrix3, [0,1,2])['identity_number'] == 0
    
    matrix4 = (
        (0, 1, 2, 3),
        (1, 2, 3, 0),
        (2, 3, 0, 1),
        (3, 0, 1, 2)
    )
    assert check_identity_element(matrix4, [0,1,2,3])['result'] == True
    assert check_identity_element(matrix4, [0,1,2,3])['identity_number'] == 0
    
    matrix5 = (
        (0, 1, 2, 3),
        (1, 3, 0, 2),
        (2, 0, 3, 1),
        (3, 2, 1, 0)
    )
    assert check_identity_element(matrix5, [0,1,2,3])['result'] == True
    assert check_identity_element(matrix5, [0,1,2,3])['identity_number'] == 0
    
def test_check_inverse():
    matrix3 = (
        (0, 1, 2),
        (1, 2, 0),
        (2, 0, 1)
    )
    assert check_inverse(matrix3, [0,1,2], 0)['result'] == True
    
    matrix4 = (
        (0, 1, 2, 3),
        (1, 2, 3, 0),
        (2, 3, 0, 1),
        (3, 0, 1, 2)
    )
    assert check_inverse(matrix4, [0,1,2,3], 0)['result'] == True
    
test_check_associativity()
test_check_identity_element()
test_check_inverse()
print('all tests passed')
