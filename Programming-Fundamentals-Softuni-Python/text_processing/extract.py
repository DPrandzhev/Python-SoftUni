input_line = input().split("\\")
filename, ext = input_line[-1].split(".")

print(f'File name: {filename}')
print(f'File extension: {ext}')