from ebooklib import epub

class Book:
    def __init__(self, title="", author=""):
        self.title = title
        self.author = author
        self.chapter = 0
    
    def epub_skeleton(self):
        book = epub.EpubBook()
        book.set_title(self.title)
        book.set_language('en')

    def add_chapter(self, title, content):
        self.chapter += 1

        fname = f"chap_{self.chapter:05d}"
        chapter = epub.EpubHtml(title=title, filename=fname.format(chapter), lang='hr')
        chapter.content = content

        self.book.add_chapter(chapter)
        # add default NCX and Nav file
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        style = 'BODY {color: black;}'
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
        book.add_item(nav_css)
        book.spine = ['nav', c1]