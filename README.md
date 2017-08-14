# Abstract_Algebra_Finite_Group_Generator

This is brute force program that enumerates all possible
permutations of [binary operations](http://mathworld.wolfram.com/BinaryOperation.html)
on a given set. It further investigate which permutation, along
with the given set, defines a valid group.

> A group < G, * > is a set G, closed under a binary operation *, such 
that the following axioms are satisfied:
* For all $a,b,c \in G$, we have
	* $(a * b) * c = a * (b * c)
* There is an element $e$ in $G$ such that for all $x \in G$,
	* $e * x = x * e = x$
	* $e$ is the identity element for *
* Corresponding to each $a \in G$, there is an element $a'$ in
$G$ such that
	* $a * a' = a' * a = e$
	* $a'$ is called the inverse of $a$  

you may use

```python
check_group([0,1,2])
#check_group([0,1,2,3]) # this will take a long time to run
```

to enumerate all the order 3 finite groups
and return only the valid ones. 

Check [Abstract Algebra/Group tables](https://en.wikibooks.org/wiki/Abstract_Algebra/Group_tables)
if you want more information.

