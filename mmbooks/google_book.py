from typing import Dict
from mmbooks.book import Book


class GoogleBook(Book):
    def __init__(self, response_json: Dict) -> None:
        volume_info = response_json.get("volumeInfo", "")

        self.title = volume_info.get("title", "")
        # 複数人あり
        # TODO: 無い場合もあるようだ
        try:
            self.author = volume_info.get("authors", "")[0]
        except Exception as e:
            self.author = ""
            print("failed to get author. error={}".format(e))
        # TODO: type==OTHERの場合は、identifierが1つしか無いため対処必要
        try:
            self.isbn = volume_info.get("industryIdentifiers", "")[1].get("identifier", "")
            self.isbn10 = volume_info.get("industryIdentifiers", "")[0].get("identifier", "")
        except Exception as e:
            print("failed to get isbn13. error={}".format(e))
            # それでも無い場合あり
            try:
                self.isbn = volume_info.get("industryIdentifiers", "")[0].get("identifier", "")
            except Exception as inner_error:
                print("failed to get isbn10. error={}".format(inner_error))
                self.isbn = ""
        self.description = volume_info.get("description", "")
        self.page_count = volume_info.get("pageCount", "")
        self.image_url = volume_info.get("imageLinks", {"thumbnail": ""}).get("thumbnail", "")
        self.info_url = volume_info.get("infoLink", "")
        self.published_date = volume_info.get("publishedDate", "")

    def to_list_string(self) -> str:
        string = "{},{},{},{},{},{}".format(
            self.__class__.__name__,
            self.isbn,
            self.title,
            self.author,
            self.published_date,
            self.page_count,
        )
        return string

    def __str__(self) -> str:
        string = """
        CLASS :         {}
        title :         {}
        author :        {}
        isbn10 :        {}
        isbn :          {}
        description :   {}
        page_count :    {}
        image_url :     {}
        info_url :      {}
        published_date: {}
        """.format(
            self.__class__.__name__,
            self.title,
            self.author,
            self.isbn10,
            self.isbn,
            self.description,
            self.page_count,
            self.image_url,
            self.info_url,
            self.published_date,
        )
        return string
