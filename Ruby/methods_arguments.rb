def take(arr, len = 1)
  size = arr.length
  return [] if len >= size

  arr[-(size - len)..-1]
end
