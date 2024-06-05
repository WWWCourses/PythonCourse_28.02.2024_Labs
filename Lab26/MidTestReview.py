# x = 0
# a = 5
# b = 5
# if a>0:
#     if b < 0:
#         x = x + 5
#     elif a > 5:
#         x= x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2

# print(x)

# def foo(x):
#     print(x**2)
#     return x**2

# res = foo(2)
# print(res)


# def total(initial=5, *args, **kw):
#     print(initial) # 5
#     print(args)     #
#     print(kw)     #


# total(100, 1,2,3, a=1)



def test_scores(total_questions=0, total_correct=0):
    return int(total_correct) / int(total_questions)




test_score = test_scores(0,20)
print(test_score)