'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list_):
  # Prints max, min, mean, and sum of list of numbers
  list_.sort()
  print(f"The max is {list_[-1]}.")
  print(f"The min is {list_[0]}.")
  print(f"The mean is {sum(list_) / len(list_)}.")
  print(f"The sum is {sum(list_)}.")

# call the function below here
stats(example_list)
