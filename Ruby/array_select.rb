def select_arr(arr)
  arr.select(&:odd?)
end

def reject_arr(arr)
  arr.reject { |a| (a % 3).zero? }
end

def delete_arr(arr)
  arr.delete_if(&:negative?)
end

def keep_arr(arr)
  arr.keep_if { |a| a >= 0 }
end
