# The most common array operations encoded here
# Definition:  A collection of values indexed by an index
# Good for: Storing ordered numbers. Fixed quantity of numbers
# Bad for: Storing unordered numbers. Varying quantity of numbers
# Insert complexity: O(1)
# Access complexity: O(1)
# Search complexity: O(log N)-unordered. O(N) ordered
# Delete complexity: O(1)

# Problem 1: order array for integers to appear first
# Time complexity: O(N)
# Space complexity: O(1)
def even_odd(A): 

    next_even, next_odd = 0, len(A)-1

    while next_even < next_odd:

        if A[next_even]%2 != 0:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd-=1
        else:
            next_even+=1

A = [2, 1, 5, 8, 9]
even_odd(A)    
# print(A)

# Syntax

# Instantiating a list
# list = [3, 5, 7, 11], [1]+[0]*10, list(range(100))

# Basic operations
A = [1, 2, 5, 9]
print(len(A))
A.append(42), print(A)
A.remove(2), print(A)
A.insert(3, 28), print(A)

# Instantiate a 2D array
B = [[1, 2, 4], [3, 5, 7, 9]]

# Copy array in python 
# A = B, dont create a copy of B it copies the reference of the list
#  so both A and B refers to the same list

# A = B.copy(), A = B[:], copy the list it changes the list but the elements are references 

# A = B.deepcopy(), copy the list and change the list and the elements 
import copy
from unittest import registerResult

class Foo(object):
    def __init__(self, val):
         self.val = val

    def __repr__(self):
        return f'Foo({self.val!r})'

foo = Foo(1)

a = ['foo', foo]
b = a.copy()
c = a[:]
d = list(a)
e = copy.copy(a)
f = copy.deepcopy(a)

# edit orignal list and instance 
a.append('baz')
foo.val = 5

print(f'original: {a}\nlist.copy(): {b}\nslice: {c}\nlist(): {d}\ncopy: {e}\ndeepcopy: {f}')

# Key methods
# bisect(list, num, beg, end): return the position on sorted list return rightmost
#bisect_left return the position to insert the argument to keep an ordered list, retunr leftmost
import bisect

A = [1, 2, 5, 9]
print(bisect.bisect(A, 5))
print(bisect.bisect_left(A, 5))

A.reverse()
print(A)

# reverse arrya
print(A[::-1])

# Rotate a list 
A = [9,1 ,3, 7, 11, 8, 5, 3]
print(A[2:]+A[:2])

# List comprehension 
print([x**2 for x in range(6) if x%2 == 0]) 
M = [['a', 'b', 'c'], ['d', 'e', 'f']]
print([x for row in M for x in row])
A = [[1, 2, 3], [4, 5, 6]]
print([[x**2 for x in row] for row in A])

# pag 40 - Dutch flag rearrange array using i as pivot

def rearrange_elements_pivot(array, index):

    if index >= len(A) or A is None:
        return None

    left, equal, right = 0, 0, len(array)-1
    pivot = A[index]

    while equal < right:
        
        if A[equal] < pivot:
            A[left], A[equal] = A[equal], A[left]
            left, equal = left+1, equal+1
        elif A[left] == pivot: 
            equal+=1
        else:
            A[equal], A[right] = A[right], A[equal]
            right-=1
        
A = [1, 9 ,5, 5, 2, 11, 3]
rearrange_elements_pivot(A, 2)
print(A)

# pag 43 - 5.2

def plus_one(A):

    A[-1] += 1

    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] +=1

    if A[0] == 10:

        A[0] = 1
        A.append(0)

    return A

print(plus_one([1,2,9]))
# pag 43 - 5.3 Multiply two arbitrary precision integers

def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0]<0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i+j+1] += num1[i] * num2[j]
            result[i+j] += result[i+j+1]//10
            result[i+j+1] %= 10
    
    result = result[next((i for i, x in enumerate(result) 
                            if x!= 0), len(result)):] or [0]
    
    return [sign * result[0]] + result[1:]

print(multiply([5,1], [7,2]))

# pag 44 - 5.4 Advancing through an array
def can_reach_end(A):
    furthest_reach_so_far, last_index = 0, len(A)-1
    i=0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i]+1)
        i+=1
    return furthest_reach_so_far >= last_index

# pag 45 - 5.5 delete duplicates from a sorted array
def delete_duplicates(A):
    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index -1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index

# pag 46 - 5.6 buy and sell a stock once

def buy_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit

# pag 47 - 5.7 buy and sell stock twice

def buy_and_sell_stock_twic(prices):

    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0]*len(prices)

    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    max_price_so_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + first_buy_sell_profits[i-1])
        
    return max_total_profit

# pag 48 - 5.8 computing an alternation

def rearrange(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse = i%2)

# pag 49 - 5.9 Enumarate all primes to n
def generate_primes(n):

    primes=[]
    is_prime = [False, False] + [True]*(n-1)
    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n+1, p):
                is_prime[i] = False
    return primes

# pag 50 - 5.10 Permute the elements of an array
def apply_permutations(perm, A):

    for i in range(len(A)):
        next=i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
    
    perm[:] = [a + len(perm) for a in perm]

# pag 52 - 5.11 Compute the next permutation
def next_permutation(perm):

    inversion_point = len(perm)-2
    while(inversion_point >=0
        and perm[inversion_point] >= perm[inversion_point+1]):
        inversion_point-=1
    
    if inversion_point == -1:
        return []

    for i in reversed(range(inversion_point+1), len(perm)):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    perm[inversion_point+1:] = reversed(perm[inversion_point+1:])
    return perm

# pag 54 - 5.12 Sample offline data
import random
def random_sampling(k, A):

    for i in range(k):
        r = random.randint(i, len(A)-i)
        A[i], A[r] = A[r], A[i]

# pag 55 - 5.13 Sample online data
import itertools
def online_random_sample(it, k):

    sampling_results = list(itertools.islice(it, k))

    num_seen_so_far = k
    for x in it:
        num_seen_so_far+=1
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x
    
    return sampling_results

# pag 56 - 5.14 Compute a random permutation
def compute_random_permutation(n):

    permutation = list(range(n))
    random_sampling(n, permutation)
    return permutation

# pag 57 - 5.15 compute a random subset
def random_subset(n, k):

    changed_elements = {}
    for i in range(k):
        rand_idx = random.randrange(i, n)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped
    
    return [changed_elements[i] for i in range(k)]
    


    


