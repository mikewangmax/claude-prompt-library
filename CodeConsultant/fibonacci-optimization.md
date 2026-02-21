# Fibonacci Function — Performance Analysis and Optimization

## Original Code

```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
```

## Analysis

The original implementation is already reasonably efficient for generating a list of Fibonacci numbers, running in **O(n)** time and **O(n)** space. However, there are several opportunities to improve performance, reduce memory overhead, and make the code more Pythonic. Below are four optimization strategies, ordered from simple refinements to more significant architectural changes.

---

## Optimization 1: Pre-allocate the List

**Problem:** `list.append()` occasionally triggers a reallocation when the internal array runs out of capacity. While amortized O(1), these reallocations copy the entire list to a new memory block, causing intermittent slowdowns for large `n`.

**Solution:** Pre-allocate the list to the exact required size.

```python
def fibonacci_preallocated(n):
    if n <= 0:
        return []
    fib = [0] * n
    if n >= 2:
        fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib
```

**Benefits:**
- Eliminates all dynamic resizing. The list is allocated once at exactly `n` elements.
- Assignment by index (`fib[i] = ...`) is marginally faster than `append()` since it bypasses the length check and potential resize logic.
- Also simplifies the edge-case handling: a single `[0] * n` covers `n == 1` and `n == 2` without separate branches.

---

## Optimization 2: Use a Generator for Lazy Evaluation

**Problem:** If the caller does not need the entire sequence at once (e.g., they only want to iterate through values or find a specific one), building the full list wastes memory.

**Solution:** Use a generator that yields values on demand, using only **O(1)** memory for the running state.

```python
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

**Benefits:**
- **O(1) memory** — only two integers are kept in memory at any time, regardless of `n`.
- Produces values lazily. If the consumer stops early, the remaining values are never computed.
- Tuple unpacking (`a, b = b, a + b`) avoids the need for a temporary variable and is a well-optimized operation in CPython.

**Usage:**
```python
# Iterate lazily
for num in fibonacci_generator(10):
    print(num)

# Materialize into a list if needed
fib_list = list(fibonacci_generator(10))
```

---

## Optimization 3: Use `functools.lru_cache` for Repeated Lookups

**Problem:** If you need to call the function multiple times with overlapping or repeated arguments, each call recomputes the entire sequence from scratch.

**Solution:** Add memoization so that previously computed results are cached and returned instantly on subsequent calls.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 0:
        return ()
    elif n == 1:
        return (0,)
    elif n == 2:
        return (0, 1)
    else:
        prev = fibonacci_cached(n - 1)
        return prev + (prev[-1] + prev[-2],)
```

**Benefits:**
- Repeated calls like `fibonacci_cached(100)` followed by `fibonacci_cached(50)` return instantly from cache.
- Useful in applications where Fibonacci values are queried multiple times at various lengths.

**Trade-off:** Uses tuples instead of lists (since `lru_cache` requires hashable return values), and the cache consumes memory proportional to the number of distinct calls.

---

## Optimization 4: NumPy for Very Large Sequences

**Problem:** For very large `n` (e.g., millions), pure Python loops become a bottleneck due to interpreter overhead and Python integer object creation.

**Solution:** Use NumPy to leverage C-level loop execution.

```python
import numpy as np

def fibonacci_numpy(n):
    if n <= 0:
        return []
    fib = np.zeros(n, dtype=object)  # dtype=object for arbitrary-precision integers
    if n >= 2:
        fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib.tolist()
```

> **Note:** For Fibonacci numbers that exceed 64-bit integer range, `dtype=object` is necessary to preserve Python's arbitrary-precision integers. If you know your values will stay within bounds, `dtype=np.int64` gives even better performance.

**Benefits:**
- Pre-allocated contiguous memory block.
- Slightly faster element access due to NumPy's internal optimizations.
- If combined with matrix exponentiation, can compute the nth Fibonacci number in **O(log n)** time.

---

## Bonus: O(log n) Single-Value Computation via Matrix Exponentiation

If you only need the nth Fibonacci number (not the entire sequence), matrix exponentiation computes it in **O(log n)** time:

```python
def fibonacci_matrix(n):
    """Return the nth Fibonacci number in O(log n) time."""
    if n <= 0:
        return 0

    def matrix_mult(A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]],
        ]

    def matrix_pow(M, p):
        if p == 1:
            return M
        if p % 2 == 0:
            half = matrix_pow(M, p // 2)
            return matrix_mult(half, half)
        else:
            return matrix_mult(M, matrix_pow(M, p - 1))

    base = [[1, 1], [1, 0]]
    result = matrix_pow(base, n)
    return result[0][1]
```

---

## Summary Table

| Approach | Time Complexity | Space Complexity | Best For |
|---|---|---|---|
| Original (list + append) | O(n) | O(n) | Simple use cases |
| Pre-allocated list | O(n) | O(n) | Known-size list output |
| Generator | O(n) | O(1) | Iterating without storing |
| LRU Cache | O(n) first call, O(1) repeat | O(n) cached | Repeated lookups |
| Matrix exponentiation | O(log n) | O(1) | Single nth value |

## Recommended Default

For most use cases, the **generator approach** (Optimization 2) is the best general-purpose improvement. It reduces memory from O(n) to O(1), simplifies the code, and can be materialized into a list with `list(fibonacci_generator(n))` whenever the full sequence is actually needed. If you always need the full list, use the **pre-allocated approach** (Optimization 1) to avoid resize overhead.
