def skip_animals(animals, skip)
  arr = []
  animals.each_with_index { |mao, ind| arr << "#{ind}:#{mao}" if ind >= skip }.compact
  arr
  # animals.map.with_index { |mao, ind| "#{ind}:#{mao}" if ind >= skip }.compact
end
