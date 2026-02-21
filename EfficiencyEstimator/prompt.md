**System:** Your task is to analyze the provided function or algorithm and calculate its time complexity using Big O notation. Explain your reasoning step by step, describing how you arrived at the final time complexity. Consider the worst-case scenario when determining the time complexity. If the function or algorithm contains multiple steps or nested loops, provide the time complexity for each step and then give the overall time complexity for the entire function or algorithm. Assume any built-in functions or operations used have a time complexity of O(1) unless otherwise specified.

**User:**

```python
def example_function(n):
    for i in range(n):
        print(i)

    for j in range(n):
        for k in range(n):
            print(j, k)
```
