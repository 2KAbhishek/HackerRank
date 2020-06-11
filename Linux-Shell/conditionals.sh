read char
# echo -e "YES\nNO\n" | grep -i $char
[[ "$char" == [yY] ]] && echo "YES" || echo "NO"