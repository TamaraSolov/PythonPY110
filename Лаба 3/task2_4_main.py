import json


def task():
    filename = "input.json"
    with open(filename) as f:
        s_j = json.load(f)

    gen_exr = (x["contains_improvement_appeals"] for x in s_j)
    # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
