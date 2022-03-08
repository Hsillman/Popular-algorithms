# Popular-algorithms
This repo contains some well known algorithms but also some good variations of their usage.
```bash
├── BinaryTreeAlgos                                      # Folder containing all things Binary Tree related.
│   ├── TreeTraversals                                   # Folder containing Binary Tree Traversals algorithms
│   │         ├── Breadth-First-Traversal-Tree.py        # Python code for level traversal of a binary tree.
│   │         └── Depth-First-Traversal-Tree.py          # Python code for depth traversal of a binary tree.
│   ├── HeightOfBinaryTree.py                            # Python code to find the height of a binary tree.
│   └── HasPathSumFromRootToLeaf.py                      # Python code to check if a binary tree has root to leaft sum given as input.
├── LinkedLists
│   ├── MergeTwoSortedLists.py                           # Python code for merging two sorted linked lists.
│   ├── ReverseLinkedList.py                             # Python code for reversing a linked list.
├── Images                                               # Images used for the README.md file.
├── README.md
├── BinarySearch.py                                      # Python code for binary search.
└── SortingAlgos                                         # Folder with sorting algorithms.
           ├── SelectionSort.py
           ├── BubbleSort.py 
           ├── InsertionSort.py
           ├── mergeSort.py
           ├── QuickSort.py
           └── CountingSort.py 
```
## 1. Sorting Algorithms
### 1.1 Selection Sort
Download the SelectionSort.py file, change the array you want to sort and run it with `python SelectionSort.py`. 

Best scenario: O(n^2)

Worst scenario: O(n^2)

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/SelectionSort.jpg" width="350" height="300">

### 1.2 Bubble Sort
Download the BubbleSort.py file, change the array you want to sort and run it with `python BubbleSort.py`. 

Best scenario: O(n)

Worst scenario: O(n^2)

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/BubbleSort.png" width="400" height="300">

### 1.3 Insertion Sort
Download the InsertionSort.py file, change the array you want to sort and run it with `python InsertionSort.py`. 

Best scenario: O(n)

Worst scenario: O(n^2)

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/InsertionSort.png" width="500" height="300">

### 1.4 Merge Sort
Download the mergeSort.py file, change the array you want to sort and run it with `python mergeSort.py`. 

Best scenario: O(nlogn)

Worst scenario: O(nlogn)

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/mergeSort.png" width="400" height="300">

### 1.5 Counting Sort
Download the CountingSort.py file, change the array you want to sort and run it with `python CountingSort.py`. 

Best scenario: O(n+k)

Worst scenario: O(n+k)

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/CountingSort.png" width="550" height="300">

### 1.5 Quick Sort
Download the file, change the array you want to sort and run it with `python QuickSort.py`. 

Best scenario: O(nlogn)

Worst scenario: O(n^2)

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/QuickSort.png" width="450" height="500">


## 2. Binary Tree Algorithms
### 2.1 Tree Traversals
####  Depth-First-Traversal
In this folder there is a file that contains the iterative and recursive versions of Depth First Traversals. Basically, there are 3 types of Depth First Traversals: <b>Pre-order</b>, <b>Post-order</b> and <b>In-order</b>. Download the file inside the TreeTraversals folder and run it with `python Depth-First-Traversal-Tree.py`. You can modify the Tree structure to your desire. The code will print all of the mentioned traversals.


<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/Preorder-Inorder-and-Postorder-traversals.jpg" width="400" height="300">

#### Breadth-First-Traversal
In the Tree Traversals folder there is a implementation of Breadth-First-Traversal. Download the file inside the TreeTraversals folder and run it with `python Breadth-First-Traversal-Tree.py`. You can modify the Tree structure to your desire.

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/Breadth-First-Traversal-Tree.png" width="450" height="250">

### 2.2 Height of a binary tree
Download the file, change the tree to your desire and run it using `python HeightOfBinaryTree.py`

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/HeightOfBinaryTree.png" width="450" height="250">

### 2.3 Has Path sum from root to leaf
This code returns True if there is any root to leaf path sum equals to the sum provided as input to the function. Download the file, change the tree to your desire and run it using `python HasPathSumFromRootToLeaf.py `

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/HasPathSumFromRootToLeaf.jpg" width="400" height="250">

## 3. Binary Search
Download the file, change the array and pass a target value to the function. Run the code with `python BinarySearch.py`

Best scenario: O(1)

Worst scenario: O(logn)

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/BinarySearch.png" width="450" height="250">

## 3. Linked Lists
### 3.1 Merging two sorted lists
Download the file, change the lists and see the result by executing `python MergeTwoSortedLists.py`

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/MergeTwoSortedLists.jpg" width="550" height="250">

### 3.1 Reverse linked lists
Download the file, change the list and see the result by executing `python ReverseLinkedList.py`

<img src="https://github.com/Hsillman/Popular-algorithms/blob/main/Images/ReverseLinkedList.png" width="550" height="200">
