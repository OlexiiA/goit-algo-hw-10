COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    if not isinstance(amount, int) or amount < 0:
        raise ValueError("Сума має бути цілим невід’ємним числом.")

    result = {}
    for coin in COINS:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount):
    if not isinstance(amount, int) or amount < 0:
        raise ValueError("Сума має бути цілим невід’ємним числом.")

    # Навіть якщо використати лише монети по 1, потрібно не більше amount монет.
    min_count = [amount + 1] * (amount + 1)
    last_coin = [0] * (amount + 1)
    min_count[0] = 0

    for current_sum in range(1, amount + 1):
        for coin in COINS:
            if coin <= current_sum:
                count = min_count[current_sum - coin] + 1
                if count < min_count[current_sum]:
                    min_count[current_sum] = count
                    last_coin[current_sum] = coin

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


if __name__ == "__main__":
    amount = 113
    print(f"Сума: {amount}")
    print(f"Жадібний алгоритм: {find_coins_greedy(amount)}")
    print(f"Динамічне програмування: {find_min_coins(amount)}")
