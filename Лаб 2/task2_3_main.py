def pow_gen(base: int):
    stepen = 0
    while True:
        yield base ** stepen
        stepen += 1

    ...  # TODO записать функцию-генератор


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
