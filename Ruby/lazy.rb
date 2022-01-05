require 'prime'

n = gets.to_i
print Prime.each.lazy.select { |x| x == x.to_s.reverse.to_i }.first(n)
