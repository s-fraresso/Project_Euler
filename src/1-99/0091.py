def is_right_triangle(x1, y1, x2, y2):
    side_squared = [x1**2 + y1**2, x2**2 + y2**2, (x1 - x2)**2 + (y1 - y2)**2]
    side_squared.sort()
    return side_squared[0] + side_squared[1] == side_squared[2]


nb_right_triangles = 0
for x1 in range(1, 51): # start at 1 for x1 and y2 to avoid a point being (0,0)
    for x2 in range(51):
        for y1 in range(51):
            for y2 in range(1, 51):
                if x1 - y1 <= x2 - y2 or (x1, y1) == (x2, y2):
                    continue
                if is_right_triangle(x1, y1, x2, y2):
                    nb_right_triangles += 1
print(nb_right_triangles)