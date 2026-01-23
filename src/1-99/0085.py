def count_rectangles(width, height):
    return (width * (width + 1) // 2) * (height * (height + 1) // 2)


TARGET_RECTANGLES = 2_000_000
best_error = float('+inf')
optimal_area = None
for width in range(1, 100):
    for height in range(1, 100):
        error = abs(count_rectangles(width, height) - TARGET_RECTANGLES)
        if error < best_error:
            best_error = error
            optimal_area = width * height
print(optimal_area)
