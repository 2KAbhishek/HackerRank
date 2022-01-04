# Write a lambda which takes an integer and square it
square      = ->(n) { n * n }

# Write a lambda which takes an integer and increment it by 1
plus_one    = ->(n) { n + 1 }

# Write a lambda which takes an integer and multiply it by 2
into_two      = ->(n) { n * 2 }

# Write a lambda which takes two integers and adds them
adder       = ->(m, n) { m + n }

# Write a lambda which takes a hash and returns an array of hash values
values_only = ->(n) { n.values }

input_number_one = gets.to_i
input_number_two = gets.to_i
input_hash = eval(gets)

a = square.call(input_number_one)
b = plus_one.call(input_number_two)
c = into_two.call(input_number_one)
d = adder.call(input_number_one, input_number_two)
e = values_only.call(input_hash)

p a
p b
p c
p d
p e
