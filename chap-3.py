my_class = 'paniz zeinab mahnaz mehrarna mohammad amin farokh reza meysam'.split(' ')

for index, name in enumerate(my_class):
    if index %3 != 0 :
        print(f'nafar shomare {index+1} {name} ast')
