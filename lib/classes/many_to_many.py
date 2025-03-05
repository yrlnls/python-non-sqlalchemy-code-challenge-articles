class Article:
    all = []
    
    def __init__(self, author, magazine, title):  
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("author must be an instance of Author")
        self._author = new_author
    
            
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        self._magazine = new_magazine
                
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "title"):
            AttributeError("title cannot be changed")
        else:
            if isinstance(new_title, str):
                if 5 <= len(new_title) <= 50:
                    self._title = new_title
                else:
                    ValueError("Title must be between 5 and 50 characters")
            else:
                TypeError("Title must be a string")
            
                    
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if hasattr(self, "name"):
            AttributeError("name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name) > 0:
                    self._name = new_name
                else:
                    ValueError("name mbst be longer than 0 characters")
            else:
                TypeError("name must be a string")

    def articles(self):
            return [article for article in Article.all if isinstance(article, Article) and self == article.author]
    
    def magazines(self):
            return list({article.magazine for article in self.articles() if isinstance(article.magazine, Magazine)})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    

    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None
        

class Magazine:
    
    all = []    
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self.all.append(self)
        
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else:
                ValueError("name must be between 2 and 16 characters")
        else:
            ValueError("name must be a string")
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category) > 0:
                self._category = new_category
            else:
                ValueError("category must be longer than 0 characters")
        else:
            ValueError("category must be a string")
    
 
    def articles(self):
            return [article for article in Article.all if isinstance(article, Article) and self == article.magazine]
    
    def contributors(self):
        if type(Author):
            return list({article.author for article in self.articles()})
    
    def article_titles(self):
        article_titles = [magazine.title for magazine in self.articles()]
        if article_titles:
            return article_titles
        else:
            return None

    def contributing_authors(self):
        authors= {}
        list_of_authors = []
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else: 
                authors[article.author] = 1  
        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author)
        if (list_of_authors):
            return list_of_authors
        else:
            return None
    @classmethod
    def top_publisher(cls):
        try:
            return max(cls.all, key=lambda magazine:len(magazine.articles()) if magazine.articles() else None)
        except:
            return None