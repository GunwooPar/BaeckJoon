import sys

def input():
    return sys.stdin.readline().rstrip()




book_list = []

book_total = int(input())

for _ in range(9):
    book = int(input())
    book_list.append(book)


res = book_total - sum(book_list)

print(res)

