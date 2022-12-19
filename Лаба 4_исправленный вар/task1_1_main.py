import json
import re

BOOKS_FILE = "books.md"
# BOOK_REGEX = r"####\s+(?P<position>\d+)\.\s+" \
#              r"\[(?P<book>.+?)\]" \
#              r"\((?P<book_url>(https)(://)(amzn.to)+/[a-zA-Z0-9]+)\)\s+" \
#              r"\s+by\s+(?P<author>.+?)\s+\((?P<recommended>)" \
#              r"\((?P<recommended>\d{1,}\.\d+%)\s+[recommended]+\)\s+" \
#              r"!\[\]\((?P<cover_url>.+?)\)\s+" \
#              r"\"(?P<description>.+?)\"\s+"
# TODO записать ругулярное выражения для поиска книги
BOOK_REGEX = r"####\s+(?P<position>\d+)\.\s+" \
             r"\[(?P<book>.+?)\]" \
             r"\((?P<book_url>(https)(://)(amzn.to)+/[a-zA-Z0-9]+)\)\s+[by]+\s+" \
             r"(?P<author>.+?)\s+\((?P<recommended>\d{1,}\.\d+%)\s+[recommended]+\)\s+" \
             r"!\[\]\((?P<cover_url>.+?)\)\s+" \
             r"\"(?P<description>.+?)\"\s+"
def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
