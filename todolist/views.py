from datetime import datetime

from django.shortcuts import render


def check_author(function):
    def _function(*args):
        found = True if args[0] == '中村憲剛' else False
        result = function(*args)
        if found:
            print('call: %s' % str(datetime.now()))
            print('length of books: %d' % len(result))
        return result

    return function


books = {
    '中村憲剛': ['サッカー脳を育む', '考える習慣'],
    '夏目漱石': ['坊ちゃん']
}


@check_author
def book_names_by_author(author, books_dict):
    return ['%s by %s' % (book, author) for book in books_dict[author]]


print(book_names_by_author('中村憲剛', books))
