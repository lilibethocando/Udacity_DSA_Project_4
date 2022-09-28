from math import sqrt


def get_distance(x1, y1, x2, y2):
    distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    distance = distance * 1000
    return int(distance)


def shortest_path(M, start, goal):

    if start == goal:
        return [start]
    
    h_dict = dict()
    for node, coordinates in M.intersections.items():
        h_dict[node] = get_distance(coordinates[0], coordinates[1], M.intersections[
                                    goal][0], M.intersections[goal][1])
        
    f_dict = dict()
    distance_from_start = {start: 0} #initialize distance from start    
    parent = dict() # initialize parent dict    
    previous = dict() # previous vertex dict
    
    open_ = {start}
    closed = set()
    
    current = start     
    h = h_dict[current] # calculate the heuristic distance of the start vertex to the destination (h)
    
    f_dict[current] = 0 + h
    
    while current != goal:
        for vertex in M.roads[current]:

            if vertex in closed:
                continue
           
            g = distance_from_start[current] + get_distance(M.intersections[current][0], M.intersections[
                                                            current][1], M.intersections[vertex][0], M.intersections[vertex][1])
           
            h = h_dict[vertex]
            f = g + h

            if vertex not in open_ or f < f_dict[vertex]:
                parent[vertex] = current
                f_dict[vertex] = f
                distance_from_start[vertex] = g

                if vertex not in open_:
                    open_.add(vertex)

        closed.add(current)
        open_.remove(current)

        del f_dict[current]
        
        lowest_vertex = min(f_dict.items(), key=lambda x: x[1])[0]
        current = lowest_vertex

    path = [goal]
    come_from = parent[goal]
    path.append(come_from)

    while come_from != start:
        come_from = parent[come_from]
        path.append(come_from)

    return path[::-1]