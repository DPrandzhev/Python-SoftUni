import re
input_line = input()
colour_pattern = r'(#|@)+([a-z]{3,})(#|@)+'
count_pattern = r'((#|@)+([a-z]{3,})(#|@)+)\W+(\d+)(\/)+'
colour_match = re.findall(colour_pattern, input_line)
count_match = re.findall(count_pattern, input_line)
for entry in colour_match and count_match:
    print(f"You found {entry[4]} {entry[2]} eggs!")