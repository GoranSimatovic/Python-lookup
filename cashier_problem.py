import numpy as np

def define_coins_back(x):
    if x == 0:
        return 0

    coin_shapes = np.array([50, 10, 5, 2, 1])
    count = np.zeros(len(coin_shapes), dtype=int)

    for i in range(len(coin_shapes)):
        count[i] = x // coin_shapes[i]
        x = x % coin_shapes[i]

    return np.array([count, coin_shapes])


class cashier:
    def __init__(self, name):
        self.name = name
        print('Hi! My name is ', self.name, '! \n Welcome to our Mom and Pop shop!')

    def money_matters(self):
        print('If your shopping costs are?  (provide cost)')
        cost = float(input())
        print('And you gave me ?')
        money_in = float(input())
        print('Then your cash back in coins is\n')
        calculation = define_coins_back((money_in - cost) * 100)
        list(map(lambda x, y: print(x,' times ', y,'cents'), calculation[0], calculation[1]))

molly = cashier('Molly')
molly.money_matters()