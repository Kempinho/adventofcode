#!/usr/bin/env python3

with open("Day3_input.txt", "r") as f:
    w1 = f.readline().rstrip("\n").split(",")
    w2 = f.readline().rstrip("\n").split(",")
    #print(wire1)

def get_path(wire):
    x_coord = 0
    y_coord = 0
    grid = [[x_coord,y_coord]]
    #print(grid)
    #print("o",end="")
    for path in wire:
        if path[0] == "R":
            for _ in range(0,int(path[1:])):
                x_coord += 1
                grid.append([x_coord,y_coord])
        elif path[0] == "L":
            for _ in range(0,int(path[1:])):
                x_coord -= 1
                grid.append([x_coord,y_coord])
        elif path[0] == "U":
            for _ in range(0,int(path[1:])):
                y_coord += 1
                grid.append([x_coord,y_coord])
        elif path[0] == "D": 
            for _ in range(0,int(path[1:])):
                y_coord -= 1
                grid.append([x_coord,y_coord])
        else:
            raise Exception("Unknown instruction")
    #print(grid)
    return grid

def get_crossing(wire1, wire2):
    intersections = []
    m_distances = []
    path1 = get_path(wire1)
    path2 = get_path(wire2)
    #print("path1:",path1)
    #print("path2:",path2)
    for coordinate in path1:
        if coordinate in path2:
            intersections.append(coordinate)
            print(intersections)

    for intersection in intersections[1:]:
        m_distances.append(abs(intersection[0]) + abs(intersection[1]))
    print(min(m_distances))
    return min(m_distances)
    #print(path1 in path2)



if __name__ == "__main__":
    assert get_crossing(["R8","U5","L5","D3"], ["U7","R6","D4","L4"]) == 6
    assert get_crossing(
        ["R75","D30","R83","U83","L12","D49","R71","U7","L72"], 
        ["U62","R66","U55","R34","D71","R55","D58","R83"]) == 159
    print(get_crossing(w1, w2))