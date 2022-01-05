def count_multibyte_char(str)
  str.each_char.count { |x| x.bytesize > 1 }
  # str.each_char.select{|x| x.bytesize > 1}.count
end
