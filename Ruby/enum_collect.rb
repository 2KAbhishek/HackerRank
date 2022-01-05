def rot13(secret_messages)
  secret_messages.collect { |c| c.tr('a-z', 'n-za-m') }
end
