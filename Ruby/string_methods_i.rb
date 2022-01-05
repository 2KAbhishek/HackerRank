def process_text(str_arr)
  str_arr.each.map(&:strip).join(' ')
end
