To analyze the time complexity of the given function `example_function(n)`, we'll break it down into its individual components and then determine the overall time complexity.

## Step 1: Analyzing the First Loop

```python
for i in range(n):
    print(i)
```

This is a single `for` loop that iterates `n` times. In each iteration, it performs a single `print(i)` operation, which is O(1). Since the loop runs `n` times and each iteration takes constant time:

**Time complexity of Step 1: O(n)**

## Step 2: Analyzing the Nested Loops

```python
for j in range(n):
    for k in range(n):
        print(j, k)
```

Here we have two nested loops:

- **Outer loop** (`for j in range(n)`): This loop iterates `n` times.
- **Inner loop** (`for k in range(n)`): For each iteration of the outer loop, the inner loop also iterates `n` times.
- **Body of the inner loop** (`print(j, k)`): This is a constant-time O(1) operation.

For each of the `n` iterations of the outer loop, the inner loop performs `n` iterations, each taking O(1) time. Therefore, the total number of operations for the nested loops is:

n * n * O(1) = O(n^2)

**Time complexity of Step 2: O(n^2)**

## Step 3: Combining the Time Complexities

The function `example_function(n)` executes Step 1 and Step 2 sequentially (one after the other, not nested within each other). When combining sequential steps, we add their time complexities:

Total = O(n) + O(n^2) = O(n + n^2)

When expressing the overall time complexity in Big O notation, we keep only the dominant (highest-order) term, since it dictates the growth rate as `n` becomes large. Here, O(n^2) dominates O(n).

## Overall Time Complexity: O(n^2)

In the worst-case scenario, as `n` grows large, the nested loops in Step 2 will overwhelmingly dominate the execution time. The first loop's linear contribution becomes negligible in comparison to the quadratic growth of the nested loops. Therefore, the overall time complexity of `example_function(n)` is **O(n^2)** (quadratic time).
