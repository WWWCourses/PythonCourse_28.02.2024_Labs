# def foo(*args):
#     print(args)


# foo(1,2,3)
# foo(1,2)


def bar(x,y):
    print(f'x={x}')
    print(f'y={y}')


# data = (1,2)
# bar(data[0], data[1])
# bar(*data)

new_data = {
    'x':1,
    'z':2
}

# bar(y=3,x=1)
bar(**new_data)




