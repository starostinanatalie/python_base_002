import simple_draw as sd
from Drawing import drawing_wall

def draw_rural_house(start_x, start_y, height_wall, width_wall, width_brick, window_width, window_height, colour):
    house_right_top = sd.get_point(start_x + width_wall + int(width_brick / 2), start_y + height_wall)
    sd.rectangle(left_bottom=sd.get_point(start_x, start_y),
                 right_top=house_right_top, color=colour, width=5)
    drawing_wall.drawing_wall(start_x=start_x, start_y=start_y, height_wall=start_y + height_wall,
                              width_wall=start_x + width_wall, height_brick=int(width_brick / 2),
                              width_brick=width_brick, color=sd.COLOR_DARK_ORANGE)
    window_left_bottom = sd.get_point(start_x + (int((width_wall - window_width) / 2)), start_y + 100)
    window_right_top = sd.get_point(start_x + (int((width_wall - window_width) / 2)) + window_width,
                                    start_y + 100 + window_height)
    sd.rectangle(left_bottom=window_left_bottom, right_top=window_right_top, color=sd.background_color)
    sd.rectangle(left_bottom=window_left_bottom, right_top=window_right_top, color=colour, width=3)
    roof_list = [sd.get_point(start_x - 15, start_y + height_wall),
                 sd.get_point(start_x + int(width_wall / 2), start_y + height_wall + 200),
                 sd.get_point(start_x + width_wall + int(width_brick / 2) + 15, start_y + height_wall)]
    sd.polygon(point_list=roof_list, color=sd.COLOR_DARK_RED, width=0)

