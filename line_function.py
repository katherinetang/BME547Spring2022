def find_y(point1, point2, x):
    m, y_int = find_eqn(point1, point2)

def find_eqn(point1, point2):
    m = (point2[1]-point1[1])/(point2[0]-point1[0])
    y_int = point1[1]-m*point1[0]
    return m, y_int