def strike(word)
  "<strike>#{word}</strike>"
end

def mask_article(str, arr)
  arr.each do |word|
    str.gsub!(/\b#{word}\b/, strike(word))
  end
  str
end
