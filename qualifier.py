import datetime
import typing
import re
# from django.db import models


# can leave the `ArticleField` class as-is if you do not wish to tackle the advanced requirements
class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    # (title, author, content, and publication_date)
    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content

    def __repr__(self):
        return f"<Article title=\"{self.title}\" author='{self.author}' publication_date='{publication_date.isoformat()}'>"

    def __len__(self):
        return len(content)

    def short_introduction(self, n_characters):
        if len(self.content) > n_characters + 1:
            index = n_characters
            if self.content[n_characters] == ' ':
                return self.content[:n_characters]
            
            while index > 0:
                if self.content[index] == ' ':
                    return self.content[:index]
                else:
                    index -= 1
            
            return self.content[:n_characters]

    def most_common_words(self, n_words):
        final_dict = {}
        words = re.findall(r"[\w]+", self.content.lower())
        for word in words:
            if word in final_dict:
                final_dict[word] += 1
            else:
                final_dict[word] = 1
                if len(final_dict) > n_words:
                    del(final_dict[word])
                    break
        final_dict = dict(sorted(final_dict.items(), key=lambda kv: kv[1], reverse=True))
        return final_dict

fairytale = Article(
    title="The emperor's new clothes",
    author="Hans Christian Andersen",
    content="'But he has nothing at all on!' at last cried out all the people. The Emperor was vexed, for he knew that the people were right.",
    publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0),
)

print()




# article = Article("new", "debug", datetime.datetime.now(), "kjabfk asdj fhgks adjhf")