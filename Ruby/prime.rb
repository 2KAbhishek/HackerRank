def prime?(num)
  false if num <= 1
  true if num == 2
  i = 2
  while i <= Math.sqrt(num)
    return false if (num % i).zero?

    i += 1
  end
  true
end

# def prime?(num)
#   num.prime?
# end
