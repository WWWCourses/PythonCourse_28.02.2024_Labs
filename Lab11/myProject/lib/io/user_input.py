def input_number():
    while True:
        try:
            x = int( input('Enter a number: ') )
            break;
        except:
            print('PLease, enter a number!!!')

def input_float():
    print('input float...')


if __name__=="__main__":
    input_float()

# # when executed as standalone script (python user_input.pu)
# print(__name__) #__main__

# # when imported as module
# 'lib.io.user_input'


