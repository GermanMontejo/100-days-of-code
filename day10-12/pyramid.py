
def create_pyramid(rows):
    for i in range(rows):
        if i == 0:
            print((' ' * int(rows/2) + (i+1) * '*' + (' ' * int(rows/2))))
        elif i == 1:
            print((' ' * (int(rows/2) - 1) + (i+i+1) * '*' + (' ' * int(rows/2))))
        else:
            print(('  ' * (int(rows/2) - (i + i))  + (i+i+1) * '*' + (' ' * int(rows/2))))

if __name__ == '__main__':
    create_pyramid(5)