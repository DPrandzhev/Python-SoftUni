import re
input_line = input()
pairs_found = 0
mirror_words = []
pattern = r'([@#])+([A-z]{3,})\1\1([A-z]{3,})\1'



match = re.findall(pattern, input_line)
for tpl in match:
    pairs_found += 1
    if tpl[1] == tpl[2][::-1]:
        mirror_words.append(f'{tpl[1]} <=> {tpl[2]}')

if pairs_found == 0:
    print ('No word pairs found!')
else:
    print(f'{pairs_found} word pairs found!')

if len(mirror_words) >= 1:
    print('The mirror words are:')
    print(', '.join(mirror_words))
else:
    print('No mirror words!')