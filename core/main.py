from core import author
from core import interface

def main(args):
    print(args)

print(interface.args.output)
book = author.Book(interface.args.title)
print(book.title)