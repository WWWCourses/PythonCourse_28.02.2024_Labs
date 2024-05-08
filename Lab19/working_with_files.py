# f = open('./Data/example.bin', mode='w')
# f.write('some texts')
# f.close()
# ---------------------------- read from text file --------------------------- #
try:
    with open('./Data/example.txt', 'rb') as f:
        for line in f:
            # Convert each byte of the line to its binary representation
            binary_line = ' '.join(f'{byte:08b}' for byte in line)
            print(binary_line)
except FileNotFoundError as e:
    print(e)


