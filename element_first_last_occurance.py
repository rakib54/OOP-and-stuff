arr = [1,3,4,4,4,5,6,7]
target = 4
low = 0
high = len(arr) -1


# find the first index of target target
while low<=high:
  mid = int((low + high) /2)
  if arr[mid] == target:
    first_occurrence = mid
    high = mid -1

  elif arr[mid] > target:
    high = mid - 1

  else:
    low = mid + 1

print(first_occurrence)

# find the last index of target target
while low<=high:
  mid = int((low + high) /2)
  if arr[mid] == target:
    last_occurrence = mid
    low = mid + 1

  elif arr[mid] > target:
    high = mid - 1

  else:
    low = mid + 1

print(last_occurrence)