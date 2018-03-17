# Jworsf01 - Joseph Worsfold
# Assignment four
from earth_distance import distance


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples:

      [(state, city, latitude, longitude), ...]

    Use this as your initial `road_map`, that is, the cycle

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    infile = open(file_name, "r")
    road_map = []
    line = infile.readline()
    while line != "":
        road_map.append(tuple(line.split('\t')))
        line = infile.readline()
    return road_map


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations.
    Print only one or two digits after the decimal point.
    """
    for i in range(len(road_map)):
        print("City: %s, %s, Latitude: %.2f, Longitude: %.2f." %
              (road_map[i][1], road_map[i][0], float(road_map[i][2]),
               float(road_map[i][3])))


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all
    the connections in the `road_map`. Remember that it's a cycle, so that
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    total_dist = 0
    for i in range(len(road_map)):
        total_dist += (distance(float(road_map[i][2]),
                                float(road_map[i][3]),
                                float(road_map[(i + 1) % len(road_map)][2]),
                                float(road_map[(i + 1) % len(road_map)][3])))
    return total_dist


def swap_adjacent_cities(road_map, index):
    """
    Take the city at location `index` in the `road_map`, and the city at
    location `index+1` (or at `0`, if `index` refers to the last element
    in the list), swap their positions in the `road_map`, compute the
    new total distance, and return the tuple

        (new_road_map, new_total_distance)
    """
    pass


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the
    city at location `index2`, swap their positions in the `road_map`,
    compute the new total distance, and return the tuple

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    pass


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `swap_adjacent_cities`,
    try `10000` swaps, and each time keep the best cycle found so far.
    After `10000` swaps, return the best cycle found so far.
    """
    pass


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    total_distance = 0.0
    for i in range(len(road_map)):
        d = (distance(float(road_map[i][2]), float(road_map[i][3]),
                      float(road_map[(i + 1) % len(road_map)][2]),
                      float(road_map[(i + 1) % len(road_map)][3])))
        total_distance += d  # replace with total distance function later
        print("%s, %s -> %s, %s = distance %f. :== Total distance = %f."
              % (road_map[i][1], road_map[i][0],
                 road_map[(i + 1) % len(road_map)][1],
                 road_map[(i + 1) % len(road_map)][0],
                 d, total_distance))


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    road_map = read_cities("city-data.txt")
    # print_cities(road_map)
    print_map(road_map)


if __name__ == "__main__":
    main()
