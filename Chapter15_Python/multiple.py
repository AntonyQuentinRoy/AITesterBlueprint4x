point = (10,20)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Point at y-axis at ({point[0]}, {point[1]})")
    case (x, 0):
        print(f"Point at x-axis at ({point[0]}, {point[1]})")
    case (x, y):
        print(f"Point at ({point[0]}, {point[1]})")