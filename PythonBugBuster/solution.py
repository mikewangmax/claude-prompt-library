# --- Original buggy code ---
# def calculate_average(nums):
# sum = 0                          # Bug 3: shadows built-in sum()
# for num in nums:
# sum += num                       # Bug 1: missing indentation throughout
# average = sum / len(nums)        # Bug 4: ZeroDivisionError if nums is empty
# return average
#
# numbers = [10, 20, 30, 40, 50]
# result = calculate_average(numbers)
# print("The average is:", results)  # Bug 2: NameError — 'results' undefined


# --- Corrected code ---

def calculate_average(nums):
    """Return the average of a list of numbers.

    Raises ValueError if the list is empty.
    """
    if not nums:
        raise ValueError("Cannot calculate the average of an empty list.")

    total = 0                # Renamed from 'sum' to avoid shadowing the built-in
    for num in nums:
        total += num

    average = total / len(nums)
    return average


numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)   # Fixed: was 'results' in the print call
print("The average is:", result)      # Fixed: 'result' matches the assigned variable


# --- Bugs explained ---
#
# Bug 1 — Indentation error
#   Python uses indentation to define code blocks. The original function body
#   had no indentation, so Python could not parse it as a valid function.
#   Fix: indent every line inside the function by 4 spaces.
#
# Bug 2 — NameError: 'results' is not defined
#   The variable was assigned as `result = calculate_average(numbers)` but the
#   print statement referenced `results` (with a trailing 's'), which was never
#   defined, causing a NameError at runtime.
#   Fix: change `results` → `result` in the print call.
#
# Bug 3 — Shadowing the built-in `sum`
#   Using `sum` as a local variable name hides Python's built-in sum() function
#   for the rest of the scope, which can cause subtle bugs elsewhere.
#   Fix: rename the accumulator variable to `total`.
#
# Bug 4 — ZeroDivisionError on empty input
#   If `nums` is an empty list, `len(nums)` is 0, and dividing by 0 raises a
#   ZeroDivisionError. The original code had no guard against this.
#   Fix: add an early check and raise a descriptive ValueError for empty input.
