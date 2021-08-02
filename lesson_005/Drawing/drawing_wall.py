import simple_draw

def drawing_wall(start_x, start_y, height_wall = 800, width_wall = 1200, height_brick = 50, width_brick = 100,
                 color=[216,53,225]):
     for row, y in enumerate(range(start_y, height_wall, height_brick)):
        slide_x = 0 if row % 2 == 0 else int(width_brick / 2)
        for x in range(start_x + slide_x, width_wall, width_brick):
            left_bottom = simple_draw.get_point(x, y)
            right_top = simple_draw.get_point(x + width_brick, y + height_brick)
            simple_draw.rectangle(left_bottom=left_bottom, right_top=right_top, color=color, width=1)



