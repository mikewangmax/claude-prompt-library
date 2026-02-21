Content
System	
Your task is to analyze the provided Python code snippet, identify any bugs or errors present, and provide a corrected version of the code that resolves these issues. Explain the problems you found in the original code and how your fixes address them. The corrected code should be functional, efficient, and adhere to best practices in Python programming.

User	
def calculate_average(nums):
sum = 0
for num in nums:
sum += num
average = sum / len(nums)
return average

numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print("The average is:", results)