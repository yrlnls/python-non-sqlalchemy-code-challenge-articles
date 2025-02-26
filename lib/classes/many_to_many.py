class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        elif not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 chars inclusive.")
        elif hasattr(self, "_title"):
            raise AttributeError("Cannot change title after instantiation.")
        else:
            self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author.")
        else:
            self._author = author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be of type Magazine.")
        else:
            self._magazine = magazine
class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def name(self):
        return self._name

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError("Cannot modify attribute after instantiation.")
        else:
            super().__setattr__(name, value)

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})

class Magazine:
    
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and (2 <= len(name)) and (len(name) <= 16):
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters long.")

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        contributor_set = set()
        for article in self.articles():
            contributor_set.add(article.author)
        return list(contributor_set)
        
    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        contributing_authors = []
        for author in self.contributors():
            article_count = sum(1 for article in author.articles() if article.magazine is self)
            if article_count > 2:
                contributing_authors.append(author)
            if not contributing_authors:
                return None
            return contributing_authors

  