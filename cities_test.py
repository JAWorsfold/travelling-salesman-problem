from cities import *


# road_map1 = [("Essex", "Colchester", "51.8959", "0.8919"),
#              ("Essex", "Chelmsford", "51.7356", "0.4685"),
#              ("Essex", "Frinton-on-sea", "51.8304", "1.2472"),
#              ("Suffolk", "Ipswich", "52.0567", "1.1482")]

def test_compute_total_distance():
    road_map1 = [("Essex", "Colchester", "51.8959", "0.8919"),
                 ("Essex", "Chelmsford", "51.7356", "0.4685"),
                 ("Essex", "Frinton-on-sea", "51.8304", "1.2472"),
                 ("Suffolk", "Ipswich", "52.0567", "1.1482")]
    actual_total_distance1 = 86.83358165735886
    assert compute_total_distance(road_map1) == actual_total_distance1
    road_map2 = [("A", "a", "0", "0"),
                 ("B", "b", "1", "1"),
                 ("C", "c", "2", "2"),
                 ("D", "d", "3", "3")]
    actual_total_distance2 = 585.7342975569294
    assert compute_total_distance(road_map2) == actual_total_distance2
    road_map3 = [("Z", "z", "0", "0"),
                 ("Y", "y", "-10.05", "-10.05"),
                 ("X", "x", "-30.25", "-30.25"),
                 ("W", "w", "-50.75", "-50.75")]
    actual_total_distance3 = 9234.89789867314
    assert compute_total_distance(road_map3) == actual_total_distance3


def test_swap_adjacent_cities():
    pass


def test_swap_cities():
    pass


def test_find_best_cycle():
    pass
