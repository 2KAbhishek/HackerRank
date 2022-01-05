def sum_terms(num)
  (1..num).reduce(0) { |sum, val| sum + ((val * val) + 1) }
end
