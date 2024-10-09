data = [
            [1,2,3],
            [4,5,6]
        ]

row_count = len(data)

print(f'Rows count: {row_count}')
print(f'Columns count: {len(data[0])}')

for row_idx,row in enumerate(data):
    for col_idx, el in enumerate(row):
        print(f'[{row_idx},{col_idx}]:{el}')


