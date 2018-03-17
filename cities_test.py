from cities import *


road_map1 = [("Essex", "Colchester", "51.8959", "0.8919"),
             ("Essex", "Chelmsford", "51.7356", "0.4685"),
             ("Essex", "Frinton-on-sea", "51.8304", "1.2472"),
             ("Suffolk", "Ipswich", "52.0567", "1.1482")]

road_map2 = [("A", "a", "0", "0"),
             ("B", "b", "1", "1"),
             ("C", "c", "2", "2"),
             ("D", "d", "3", "3")]

road_map3 = [("Z", "z", "0", "0"),
             ("Y", "y", "-10.05", "-10.05"),
             ("X", "x", "-30.25", "-30.25"),
             ("W", "w", "-50.75", "-50.75")]


def test_compute_total_distance():
    actual_total_distance1 = 86.83358165735886
    assert compute_total_distance(road_map1) == actual_total_distance1
    actual_total_distance2 = 585.7342975569294
    assert compute_total_distance(road_map2) == actual_total_distance2
    actual_total_distance3 = 9234.89789867314
    assert compute_total_distance(road_map3) == actual_total_distance3


def test_swap_adjacent_cities_one():
    map, distance = swap_adjacent_cities(road_map1, 0)
    assert distance == 89.65681007275302
    map, distance = swap_adjacent_cities(road_map1, 1)
    assert distance == 101.74032316468367
    map, distance = swap_adjacent_cities(road_map1, 2)
    assert distance == 89.65681007275302
    map, distance = swap_adjacent_cities(road_map1, 3)
    assert distance == 101.74032316468366


def test_swap_adjacent_cities_two():
    map, distance = swap_adjacent_cities(road_map2, 0)
    assert distance == 585.7343196545323
    map, distance = swap_adjacent_cities(road_map2, 1)
    assert distance == 780.9889602375081
    map, distance = swap_adjacent_cities(road_map2, 2)
    assert distance == 585.7343196545323
    map, distance = swap_adjacent_cities(road_map2, 3)
    assert distance == 780.9889602375081


def test_swap_adjacent_cities_three():
    map, distance = swap_adjacent_cities(road_map3, 0)
    assert distance == 9257.388533012429
    map, distance = swap_adjacent_cities(road_map3, 1)
    assert distance == 13003.742428600068
    map, distance = swap_adjacent_cities(road_map3, 2)
    assert distance == 9257.388533012429
    map, distance = swap_adjacent_cities(road_map3, 3)
    assert distance == 13003.742428600068


def test_swap_cities():
    pass


def test_find_best_cycle():
    pass
