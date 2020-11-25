
'''
Obeserver Design pattern
'''

class User:
    '''
    User class will act role of observer to subject
    '''
    def __init__(self, name):
        self.name = name

    def update(self, article, blog_writer):
        print(f'For {self.name}, new article by {blog_writer.name} is added')

class BlogWriter:
    '''
    BlogWriter class is useful to blog writer to add new article
    and manage subscribers as well
    '''
    def __init__(self, name):
        self.name = name
        self.__subscribers = []
        self.__articles = []

    def add_article(self, article):
        '''
        Add new article and notify subscribers
        '''
        self.__articles.append(article)
        self.notify_subscribers(article)

    def get_articles(self):
        '''
        Get articles written by {self}
        '''
        return self.__articles

    def subscribe(self, subscriber):
        '''
        Add new subscriber to notify on adding article
        '''
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        '''
        User can unsubscribe from further notifications
        '''
        return self.__subscribers.remove(subscriber)

    def subscribers(self):
        '''
        Get subsribers
        '''
        return self.__subscribers

    def notify_subscribers(self, article):
        '''
        Notifying all the subsribers about new addition of an article
        '''
        for sub in self.__subscribers:
            sub.update(article, self)
    
    def print_article(self):
        '''
        Printing all article that blog writer published
        '''
        for article in self.__articles:
            print(f'article subject is {article}')

if __name__ == '__main__':
    blog_writer = BlogWriter('Amir Sartipi')
    narges_asadi = User('Narges Aasdi')
    fereshte_hadian = User('Freshte Hadian')
    blog_writer.subscribe(narges_asadi)
    blog_writer.subscribe(fereshte_hadian)
    blog_writer.add_article('Programming')
    blog_writer.add_article('Sport')
    blog_writer.print_article()