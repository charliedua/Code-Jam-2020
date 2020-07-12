import datetime
import typing
import re
from typing import List


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field_type = field_type
        # self._attribute : field_type = None
        self.__attribute_dict = {}

    def __get__(self, instance, owner):
        return self.__attribute_dict[instance.__hash__()]

    def __set__(self, instance, value):
        if not issubclass(type(value), self.field_type):
            raise TypeError(f"expected an instance of type '{self.field_type.__name__}' for attribute '{dir(instance)[26]}', got '{type(value).__name__}' instead")

        self.__attribute_dict[instance.__hash__()] = value


class Article:
    """The `Article` class you need to write for the qualifier."""
    id = -1
    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        Article.id += 1
        self.id = Article.id
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self._content = content
        self.last_edited = None

    def __repr__(self):
        return f"<Article title=\"{self.title}\" author='{self.author}' publication_date='{self.publication_date.isoformat()}'>"

    def __len__(self):
        return len(self.content)

    def short_introduction(self, n_characters):
        if len(self._content) > n_characters + 1:
            if self._content[n_characters] == ' ' or self._content[n_characters] == '\n':
                return self._content[:n_characters]
            
            index = n_characters
            while index > 0:
                if self._content[index] == ' '  or self._content[index] == '\n':
                    return self._content[:index]
                else:
                    index -= 1
            
            return self._content[:n_characters]

    def most_common_words(self, n_words):
        final_dict = {}
        words = re.findall(r"[\w]+", self._content.lower())
        for word in words:
            if word in final_dict:
                final_dict[word] += 1
            else:
                final_dict[word] = 1
        final_dict = dict(sorted(final_dict.items(), key=lambda kv: kv[1], reverse=True)[:n_words])
        return final_dict

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, new_content):
        self.last_edited = datetime.datetime.now()
        self._content = new_content

    def __lt__(a,b):
        return a.publication_date < b.publication_date

    def __gt__(a,b):        
        return a.publication_date > b.publication_date