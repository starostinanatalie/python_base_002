import random
import simple_draw

def smiles_draw(x, y, colour):
    point = simple_draw.get_point(x, y)
    other = simple_draw.get_point(x + 65, y + 50)
    eye_point = simple_draw.get_point(x + 20, y + 30)
    eye_second_point = simple_draw.get_point(x + 45, y + 30)
    smile_point_one = simple_draw.get_point(x + 10, y + 20)
    smile_point_two = simple_draw.get_point(x + 25, y + 12)
    smile_point_three = simple_draw.get_point(x + 35, y + 12)
    smile_point_four = simple_draw.get_point(x + 50, y + 20)
    simple_draw.ellipse(point, other, colour, 2)
    simple_draw.circle(eye_point, 5, colour, 2)
    simple_draw.circle(eye_second_point, 5, colour, 2)
    simple_draw.line(smile_point_one, smile_point_two, colour, 2)
    simple_draw.line(smile_point_two, smile_point_three, colour, 2)
    simple_draw.line(smile_point_three, smile_point_four, colour, 2)



    


