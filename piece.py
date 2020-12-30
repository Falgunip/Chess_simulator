# Taking Input from the user

min_x = 65  # A
max_x = 72  # H
min_y = 1
max_y = 8

def king(x_position,y_position):
    if x_position > min_x and x_position < max_x and y_position > min_y and y_position < max_y:
        values = chr(x_position - 1) + str(y_position), chr(x_position + 1) + str(y_position), chr(x_position) + str(y_position - 1) \
            , chr(x_position) + str(y_position + 1), chr(x_position - 1) + str(y_position - 1), chr(x_position - 1) + str(y_position + 1) \
            , chr(x_position + 1) + str(y_position - 1), chr(x_position + 1) + str(y_position + 1)
    elif x_position == min_x and y_position > min_y and y_position < max_y:
        values = chr(x_position) + str(y_position + 1), chr(x_position) + str(y_position - 1), chr(
            x_position + 1) + str(y_position), chr(x_position + 1) + str(y_position + 1), chr(x_position + 1) + str(
            y_position - 1)
    elif x_position == min_x and y_position == min_y:
        values = chr(x_position) + str(y_position + 1), chr(x_position + 1) + str(y_position), chr(
            x_position + 1) + str(y_position + 1)
    elif y_position == min_y and x_position > min_x and x_position < max_x:
        values = chr(x_position - 1) + str(y_position), chr(x_position - 1) + str(y_position + 1), chr(
            x_position) + str(y_position + 1), chr(x_position + 1) + str(y_position), chr(x_position + 1) + str(
            y_position + 1)
    elif x_position == min_x and y_position == max_y:
        values = chr(x_position) + str(y_position - 1), chr(x_position + 1) + str(y_position), chr(
            x_position + 1) + str(y_position - 1)
    elif x_position == max_x and y_position > min_y and y_position < max_y:
        values = chr(x_position) + str(y_position - 1), chr(x_position - 1) + str(y_position - 1), chr(
            x_position - 1) + str(y_position), chr(x_position - 1) + str(y_position + 1), chr(x_position) + str(
            y_position + 1)
    elif x_position == max_x and y_position == min_y:
        values = chr(x_position - 1) + str(y_position), chr(x_position - 1) + str(y_position + 1), chr(
            x_position) + str(y_position + 1)
    elif y_position == max_y and x_position > min_x and x_position < max_x:
        values = chr(x_position - 1) + str(y_position), chr(x_position - 1) + str(y_position - 1), chr(
            x_position) + str(y_position - 1), chr(x_position + 1) + str(y_position - 1), chr(x_position + 1) + str(
            y_position)
    elif x_position == max_x and y_position == max_y:
        values = chr(x_position - 1) + str(y_position), chr(x_position - 1) + str(y_position - 1), chr(
            x_position) + str(y_position - 1)
    values = list(values)
    return values


def queen(x_position,y_position):
    values = bishop(x_position,y_position) + rook(x_position,y_position)
    return values

def bishop(x_position,y_position):
    values = []
    x_copy = x_position
    y_copy = y_position
    while x_copy > min_x and y_copy < max_y:
        values1 = chr(x_copy - 1) + str(y_copy + 1)
        x_copy = x_copy - 1
        y_copy = y_copy + 1
        values.append(values1)
    x_copy = x_position
    y_copy = y_position
    while x_copy < max_x and y_copy < max_y:
        values2 = chr(x_copy + 1) + str(y_copy + 1)
        x_copy = x_copy + 1
        y_copy = y_copy + 1
        values.append(values2)
    x_copy = x_position
    y_copy = y_position
    while x_copy > min_x and y_copy > min_y:
        values2 = chr(x_copy - 1) + str(y_copy - 1)
        x_copy = x_copy - 1
        y_copy = y_copy - 1
        values.append(values2)
    x_copy = x_position
    y_copy = y_position
    while x_copy < max_x and y_copy > min_y:
        values2 = chr(x_copy + 1) + str(y_copy - 1)
        x_copy = x_copy + 1
        y_copy = y_copy - 1
        values.append(values2)
    return values

def hourse(x_position,y_position):
    # if x_position > min_x and x_position < max_x and y_position > min_y and y_position < max_y:
    if x_position in range(min_x,max_x+1) and y_position in range(min_y,max_y+1):
        values = chr(x_position - 2) + str(y_position +1), chr(x_position - 1) + str(y_position +2),chr(x_position +1) + str(y_position +2),\
                 chr(x_position +2) + str(y_position +1),chr(x_position -2) + str(y_position -1),chr(x_position -1) + str(y_position -2),\
                 chr(x_position +1) + str(y_position -2),chr(x_position +2) + str(y_position -1),
        #print(values)
        values = list(values)
        for i in values[:]:
            if i.startswith('@') or i.startswith('?') or i.endswith('0') or i.endswith('-1') or i.startswith('I') or i.startswith('J') or i.endswith('9'):
                values.remove(i)
            else:
                continue
    return values

def rook(x_position,y_position):
    if x_position >= min_x and x_position <= max_x and y_position >= min_y and y_position <= max_y:
        values = []
        for i in range(min_x,max_x+1):
            values1 = chr(i) + str(y_position)
            if i == x_position:
                continue
            values.append(values1)
        for j in range(min_y,max_y+1):
            values2 = chr(x_position) + str(j)
            if j == y_position:
                continue
            values.append(values2)
    return values

def pawn(x_position,y_position):
    if x_position in range(min_x,max_x+1) and y_position < max_y :
        values = chr(x_position) + str(y_position +1)
    else:
        return "Enter Proper Value"
    return values


def main():
    piece = input("Enter for which you piece you want to search: King, Queen, Bishop, Horse, Rook, Pawn : ")
    position = input("Enter on which position your piece is present: A1 to A8, B1 to B8,...H1 to H8 : ")

    x_posi, y_posi = tuple(list(position))
    # print(x_posi, y_posi)

    x_posi = ord(x_posi)
    y_posi = int(y_posi)

    if piece == 'King' or piece == 'Bishop' or piece == 'Rook' or piece == 'Queen' or piece == 'Hourse':
        piece_option = {'King': king, 'Bishop': bishop, 'Rook': rook, 'Queen': queen, 'Hourse': hourse}
        result = ", ".join(piece_option[piece](x_posi, y_posi))
    elif piece == 'Pawn':
        piece_option = {'Pawn': pawn}
        result = piece_option[piece](x_posi, y_posi)
    print(result)

if __name__ == '__main__':
    main()