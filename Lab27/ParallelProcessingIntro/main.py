import time


# sum of numbers 1..10_000_000
START = 1
END = 10_000_000


def sum_of_numbers(start, end):
    total = 0
    for num in range(start, end+1):
        total+=num

    return total


start = time.time()
# Run on Core1:
total_sum = 0
res1 = sum_of_numbers(START,round(END/2) )
# Run on Core2:
res2 = sum_of_numbers(round(END/2), END )

total_sum=res1 + res2


print(f'Sum of {START}..{END} is {total_sum}')
end=time.time()
print(f'time: {end-start}')