s = input()
end_s = ""
current_char = s[0]
char_count = 1
for char in s[1:]:
    if char == current_char:
        char_count += 1
    else:
        end_s += f"{current_char}{char_count}"
        char_count = 1
        current_char = char
end_s += f"{current_char}{char_count}"
print(end_s)
