def is_inside(list1, list2):
    x = list1[0]
    y = list1[1]
    x_box = list2[0]
    y_box = list2[1]
    width = list2[2]
    height = list2[3]
    if x >= x_box and x <= (x_box + height):
        if x >= y_box and y <= (y_box + width):
            is_inside = True
    else:
        is_inside = False
    return is_inside
