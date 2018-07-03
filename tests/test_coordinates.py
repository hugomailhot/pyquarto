# !/usr/bin/env python
# encoding: utf-8

from pyquarto.coordinates import Coordinates


alphanum_pairs = (
    ('a', 1), ('a', 2), ('a', 3), ('a', 4),
    ('b', 1), ('b', 2), ('b', 3), ('b', 4),
    ('c', 1), ('c', 2), ('c', 3), ('c', 4),
    ('d', 1), ('d', 2), ('d', 3), ('d', 4)
)

matrix_coordinates = (
    (0, 0), (0, 1), (0, 2), (0, 3),
    (1, 0), (1, 1), (1, 2), (1, 3),
    (2, 0), (2, 1), (2, 2), (2, 3),
    (3, 0), (3, 1), (3, 2), (3, 3)
)


def test_from_alphanumeric():
    for alphanum, mat_coords in zip(alphanum_pairs, matrix_coordinates):
        alpha, num = alphanum
        assert Coordinates.from_alphanumeric(alpha, num) == mat_coords


def test_to_alphanumeric():
    for alpha, num in alphanum_pairs:
        c = Coordinates(alpha, num)
        assert c.to_alphanumeric() == (alpha, num)


def test_to_matrix_coordinates():
    for alphanum, mat_coords in zip(alphanum_pairs, matrix_coordinates):
        alpha, num = alphanum
        c = Coordinates(alpha, num)
        assert c.to_matrix_coordinates() == mat_coords

