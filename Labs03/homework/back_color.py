from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text_list = []
    color_list = []

    for item in shapes:
        text_list.append(item['text'])
        color_list.append(item['color'])
    text = choice(text_list)
    color = choice(color_list)
    quiz_type = randint(0,1)
    lists = (text, color, quiz_type)
    return lists

# def is_inside(list1, list2):
#     x = list1[0]
#     y = list1[1]
#     x_box = list2[0]
#     y_box = list2[1]
#     width = list2[2]
#     height = list2[3]
#     if x >= x_box and x <= (x_box + height):
#         if x >= y_box and y <= (y_box + width):
#             is_inside = True
#     else:
#         is_inside = False
##     return is_inside

from is_inside import is_inside
def mouse_press(x, y, text, color, quiz_type):
    check = True
    while check:
        for item in shapes:
            rect = item['rect']
            check = is_inside([x, y], rect)
            if check == True:
                box_color = item['color']
                text_color = item['text']
            else:
                break
    if quiz_type == 0 and text_color == text:
        check = True
    elif quiz_type == 1 and box_color == color:
        check = True
    else:
        check = False
    return check
