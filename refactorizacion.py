def ingresar_evaluation():
    while True:
        print('Please enter your rating from 1 to 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Please enter a number from 1 to 5')
            else:
                print('Please enter your comment')
                comment = input()
                post = f'Point: {point} Comment: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Please enter the evaluation points as numbers')

def ver_resultados():
    print('Results so far')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def procesar_opcion(num):
    if num == 1:
        ingresar_evaluation()
    elif num == 2:
        ver_resultados()
    elif num == 3:
        print('Exit')
        return False
    else:
        print('Please enter from 1 to 3')
    return True

while True:
    print('Please select the process you want to perform')
    print('1: Enter evaluation points and comments')
    print('2: Check the results so far')
    print('3:End')
    num = input()

    if num.isdecimal():
        num = int(num)
        if not procesar_opcion(num):
            break
    else:
        print('Please enter from 1 to 3')