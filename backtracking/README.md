## Backtracking

### Introduction

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, that incrementally builds candidates to the solutions. As soon as it determines that a candidate cannot possibly lead to a valid complete solution, it abandons this partial candidate and “backtracks’’ (return to the upper level) and reset to the upper level’s state so that the search process can continue to explore the next branch. Backtracking is all about choices and consequences, this is why backtracking is the most common algorithm for solving constraint satisfaction problem

Backtracking is a depth-first search (DFS) algorithm that builds solutions incrementally.

It involves choosing a candidate, exploring further by recursively calling the function, and backtracking if the candidate leads to a dead end.

This technique is often used for problems involving permutations, combinations, and subsets.

The code of backtracking uses a DFS traversal and undoes previous decisions by 
removing a previous choice from the current path.
This is the heart of backtracking, we try all possibilities knowing that some may not lead to a solution. when path no longer can lead to a solution, the decision is reveresed.

Basic Operations in Backtracking
The backtracking algorithm typically follows this pattern:

1. Choose: Select a candidate from the set of possible options.
2. Constraint: Check if the choice satisfies all constraints.
3. Goal: Check if the current state is a valid solution.
4. Recurse: If the constraints are satisfied but the goal isn't reached, make a recursive call.
5. Backtrack: Remove the last chosen candidate if it leads to a dead end and try another candidate.

### How to identify if the problem requires backtracking solution

1. The problem will ask to generate all possible valid answers.
2. Large number of choices should be given. Number of choices is usually variable.
3. We should be able to control the recursion i.e. pruning of undesirable branch. 

### Template of Backtracking code

```template
def solve(nums, start, current_path, result):
    # Base condition
    if is_result_found():
        result.append(list(current_path))
        return
    
    for i in range(start, len(nums)):
        if is_choice_valid():

            # Take the choice. Now, element at first position is fixed 
            current_path.append(nums[i])
            
            # Solve for next position
            solve(nums, start + 1, current_path, result)
            
            # Revert the choice taken earlier
            current_path.pop()
            
def solution(nums):
    result = []
    current_path = []
    start = 0
    solve(nums, start, current_path, result)
    return result
```

### Common problems:

1. Generate all Subsets (powerset)
2. Generate all Subsets (powerset) with duplicate in input
3. Combinations sum equal to target
4. Combinations sum equal to target with duplicated in input
5. Phone letter combinations
6. Word search
7. Permutations
8. Permutations 2
9. N Queen
10. N Queen 2
11. Rat in Maze
12. Generate balanced parenthesis 
13. Generate greatest number using k swaps 
14. Generate all N digit numbers with increasing digits



