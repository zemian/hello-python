import argparse

# see https://docs.python.org/3/howto/argparse.html


def test_argument_fixed_two():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    print(args)

def test_args_boolean():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", action="store_true")
    parser.add_argument("-x", action="store_false")
    args = parser.parse_args()
    print(args)

test_args_boolean()
