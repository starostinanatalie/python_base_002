import simple_draw as sd

def draw_branches_advanced(initial_point, angle, branch_length):
    if branch_length < 10:
        return
    delta_angle = sd.random_number(30 - 30 * 0.4, 30 + 30 * 0.4)
    angle_left = angle - delta_angle
    angle_right = angle + delta_angle
    left_branch = sd.get_vector(start_point=initial_point, angle=angle_left, length=branch_length)
    left_branch.draw(color=sd.COLOR_GREEN)
    right_branch = sd.get_vector(start_point=initial_point, angle=angle_right, length=branch_length)
    right_branch.draw(color=sd.COLOR_GREEN)
    delta_length = sd.random_number(-20, 20) * 0.01
    branch_length = branch_length * (0.75 + delta_length)
    draw_branches_advanced(left_branch.end_point, angle_left, branch_length)
    draw_branches_advanced(right_branch.end_point, angle_right, branch_length)

def draw_tree(x, y):
    root_point = sd.get_point(x, y)
    root = sd.get_vector(root_point, 90, 30)
    root.draw(color=sd.COLOR_DARK_ORANGE)
    draw_branches_advanced(root.end_point, 90, 100)
