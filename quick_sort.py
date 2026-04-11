def partition(thelist, low, high):
  pivot = thelist[high]
  i = low -1
  for j in range(low, high):
  if thelist[j] <= pivot:
    i = i + 1
    (thelist[i], thelist[j]) = (thelist[j], thelist[i])
  (thelist[i + 1], thelist[high]) = (thelist[high], thelist[i + 1])
  return i + 1
