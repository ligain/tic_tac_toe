X_SYMBOL = 'x'
O_SYMBOL = 'o'
NULL_SYMBOL = '_'
BOARD_TEMPLATE = '''
{1} | {2} | {3}
----------
{4} | {5} | {5}
----------
{6} | {7} | {8}'''
BOARD_MAPPING = {
    X_SYMBOL: X_SYMBOL,
    O_SYMBOL: O_SYMBOL,
    NULL_SYMBOL: ' '
}
WIN_COMBINATIONS = (
    # horizontal row combinations
    (1, 1, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 1, 1),

    # vertical row combinations
    (1, 0, 0, 1, 0, 0, 1, 0, 0),
    (0, 1, 0, 0, 1, 0, 0, 1, 0),
    (0, 0, 1, 0, 0, 1, 0, 0, 1),

    # diagonal combinations
    (1, 0, 0, 0, 1, 0, 0, 0, 1),
    (0, 0, 1, 0, 1, 0, 1, 0, 0),
)
