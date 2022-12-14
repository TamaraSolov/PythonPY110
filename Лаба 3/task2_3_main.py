import json

def task():
    filename = "input.json"
    with open(filename) as f:
        j_s = json.load(f)

    return max(j_s, key=lambda x: x["score"])

        # [lambda x: x.max() for x in j_s["score"]]
         # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
