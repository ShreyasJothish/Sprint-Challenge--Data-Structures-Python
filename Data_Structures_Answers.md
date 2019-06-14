Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

**Answer**: The item is inserted based on the current position attribute of the ring buffer class.
So the runtime complexity is O(1).

2. What is the space complexity of your ring buffer's `append` function?

**Answer**: The item is inserted without any addition memory needed.
So the space complexity is O(1).

3. What is the runtime complexity of your ring buffer's `get` method?

**Answer**: All ring buffer is iterated over to determine the item's value at each position starting at 0 till capacity limit.
So the runtime complexity is O(n).

4. What is the space complexity of your ring buffer's `get` method?

**Answer**: There is no additional memory allocated for get method and memory of existing ring buffer is used.
So the space complexity is O(1).

5. What is the runtime complexity of the provided code in `names.py`?

**Answer**: The given solution iterates over two list sequentially in two loops.
So the runtime complexity is O(m x n).
where 
    m - number of items in names1_list
    n - number of items in names2_list

If we assume the lists to be of same size, then we can generalize the runtime complexity as O(n^2).

6. What is the space complexity of the provided code in `names.py`?

**Answer**: There is no additional memory allocated for comparing the list.
So the space complexity is O(1).

7. What is the runtime complexity of your optimized code in `names.py`?

**Answer**: I am using Binary Search Tree (BST) implementation for getting faster search.
So the runtime complexity of creating the BST tree is O(mlogm).
Also the searching for duplicates in BST is O(nlogm).

So overall complexity is O(mlogm) + O(nlogm).

where 
    m - number of items in names1_list
    n - number of items in names2_list
    
**Stretch goal**
Based on solution in stretch goal to use only arrays, the solution is optimized to sort both the name arrays before comparison.
With this overall runtime compexity for finding duplicates is reduced to O(n).

8. What is the space complexity of your optimized code in `names.py`?

**Answer**: To create the Binary Search Tree, we need additional m nodes.
So the space complexity for new solution is O(m).

where 
    m - number of items in names1_list
    
**Stretch goal**

With stretch goal overall space complexity is reduced to O(1).
