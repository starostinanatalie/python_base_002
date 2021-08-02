import simple_draw as sd

def drawing_rainbow_straight(x,y):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    slide_point = 0
    for colour in rainbow_colors:
        slide_point += 5
        beginning_point = sd.get_point(x + slide_point,y + 50)
        end_point = sd.get_point(x + 345 + slide_point, y + 450)
        sd.line(start_point=beginning_point, end_point=end_point, color=colour, width=4)
        center = sd.get_point(200, -100)
        radius += 7
        sd.circle(center_position = center, radius=radius, color=colour, width=7)

def drawing_rainbow(x, y, radius):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    for colour in rainbow_colors:
        center = sd.get_point(x, y)
        radius += 7
        sd.circle(center_position=center, radius=radius, color=colour, width=10)