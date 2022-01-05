hackerrank.store(543_121, 100)
hackerrank.keep_if { |key, _value| key.is_a? Integer }
hackerrank.delete_if { |key, _value| key.even? }
