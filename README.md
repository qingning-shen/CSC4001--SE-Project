# CSC4001--SE-Project
This is the course project from CSC4001 in CUHKSZ about differential testing, fuzzing and dataflow analysis.

Differential testing is a black-box technique to compare whether two programs have the same behaviors under the specific requirements, and one of the program is correct in the testing function. Before testing, we need some robust samples to express the possible mistakes logic. So if the results return by the two programs are different, the other program must have some bugs.

This task requires us to write a pig language interpreter, which represents the correct program in the testing function, and the generator for the pig language is to generate some testing data. To ensure robust, the testing data should be divided into two parts. The first part are random. Mainly focused on the recursion of the expressions, the basic logic of the pig (the function of branching, declare, assignment, remove and output). The second part are designed deliberately, which need to consider some special cases. Such as the loops caused by branching.

In each data-flow analysis application, we associate with every program point a data-flow value that represents an abstraction of the set of all possible program states that can be observed for that point. And it’s to find a solution to a set of safe-approximation-directed constraints on the IN[s]’s and OUT[s]’s, for all statements. In this project, we have transfer function OUT[B] = gen B union (IN[B] - killB) and control flow IN[B] = ∪ p a predecessor of B OUT[P].
