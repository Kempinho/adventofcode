#!/usr/bin/env python3

with open("Day3_input.txt", "r") as f:
    w1 = f.readline().rstrip("\n").split(",")
    w2 = f.readline().rstrip("\n").split(",")

def get_path(wire):
    x_coord = 0
    y_coord = 0
    grid = [(x_coord,y_coord)]
    for path in wire:
        if path[0] == "R":
            for _ in range(0,int(path[1:])):
                x_coord += 1
                grid.append((x_coord,y_coord))
        elif path[0] == "L":
            for _ in range(0,int(path[1:])):
                x_coord -= 1
                grid.append((x_coord,y_coord))
        elif path[0] == "U":
            for _ in range(0,int(path[1:])):
                y_coord += 1
                grid.append((x_coord,y_coord))
        elif path[0] == "D": 
            for _ in range(0,int(path[1:])):
                y_coord -= 1
                grid.append((x_coord,y_coord))
        else:
            raise Exception("Unknown instruction")
        
    return grid

def get_all_intersections(wire1, wire2):
    path1 = set(get_path(wire1))
    path2 = set(get_path(wire2))
    intersections = path1.intersection(path2)
    intersections.discard((0,0))

    return intersections

def get_manhattan_distance(wire1, wire2):
    m_distances = []
    intersections = get_all_intersections(wire1, wire2)
    for value in intersections:
        m_distances.append(abs(value[0]) + abs(value[1]))
    return min(m_distances)

def get_fewest_steps(wire1, wire2):
    steplist = []
    path1 = get_path(wire1)
    path2 = get_path(wire2)
    intersections = get_all_intersections(wire1, wire2)

    for value in intersections:
        steplist.append(path1.index(value) + path2.index(value))

    return min(steplist)


if __name__ == "__main__":
    assert get_manhattan_distance(["R8","U5","L5","D3"], ["U7","R6","D4","L4"]) == 6
    assert get_manhattan_distance(
        ["R75","D30","R83","U83","L12","D49","R71","U7","L72"], 
        ["U62","R66","U55","R34","D71","R55","D58","R83"]) == 159
    assert get_fewest_steps(["R8","U5","L5","D3"], ["U7","R6","D4","L4"]) == 30
    assert get_fewest_steps(
        ["R75","D30","R83","U83","L12","D49","R71","U7","L72"], 
        ["U62","R66","U55","R34","D71","R55","D58","R83"]) == 610
    print("Manhattan Distance:", get_manhattan_distance(w1, w2))
    print ("fewest steps to intersection:", get_fewest_steps(w1, w2))