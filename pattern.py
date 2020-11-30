class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]
class Package:
    def __init__(self, price): 
        self._price = price 

    def get_price(self): 
        return self._price
class LanguageAdaptor():
    def __init__(self, object, **method_want_adopted):
        self._object = object
        self.__dict__ = method_want_adopted

    def __getattr__(self, attr):
        return getattr(self._object, attr)
class User:
    def __init__(self, name:str, packege:Package, lang:LanguageAdaptor):
        self.name = name
        self.package = packege
        self.lang = lang

    def update(self, notif, company):
        print('Dear {}, {} have notification for you--> notif is {}'.format(self.name, company.name, notif))


class Company(metaclass=Singleton):
    # constructor method
    def __init__(self):
        self.name = 'insta'
        self.__subscribers = []
        self.__notification = []
    
    def __str__(self):
        return self.name

    def add_notif(self, notif):
        self.__notification.append(notif)
        self.notify_subscribers(notif)

    def get_notifs(self):
        return self.__notification

    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)

    def subscribers(self):
        return self.__subscribers

    def notify_subscribers(self, notif):
        for sub in self.__subscribers:
            sub.update(notif, self)
    def show_user_information(self):
        print('# show info')
        for user in self.__subscribers:
            print('user is {} and package price is {} and {}'.format(user.name, user.package.get_price(), user.lang.write))

class FeaturePackage1(Package):
    
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price.get_price() + 2000
class FeaturePackage2(Package):
    
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price.get_price() + 5000
class Language():
    def __init__(self):
        self.language = ''

class PersianLang(Language):
    def __init__(self):
        self.language = 'Perisan'
    def write_farsi(self):
        return 'write Farsi'
class BritishLang():
    def __init__(self):
        self.language = 'British'
    def write_british(self):
        return 'write British'
class AmericaLang():
    def __init__(self):
        self.language = 'American'
    def write_american(self):
        return 'write American'

def make_adopted_method():
    obj = []
    british = BritishLang()
    persian = PersianLang()
    american = AmericaLang()
    obj.append(LanguageAdaptor(british, write=british.write_british()))
    obj.append(LanguageAdaptor(persian, write=persian.write_farsi()))
    obj.append(LanguageAdaptor(american, write=american.write_american()))
    return obj

def test_observer(insta_1, users):

    print('# test observer')
    for user in users:
        insta_1.subscribe(user)
    insta_1.add_notif('New version is available')

def test_decorator():
    print('# test decorator')
    p = Package(1000)
    p1 = FeaturePackage1(p)
    p2 = FeaturePackage2(FeaturePackage1(p))
    print("base package price is {}".format(p.get_price()))
    print("base package and package 1 price is {}".format(p1.get_price()))
    print("base package and package 1 and package 2 price is {}".format(p2.get_price()))
    return [p, p1, p2]
 
def test_singleton():
    print('# test singleton')
    insta_1 = Company()
    insta_2 = Company()
    insta_1.name = 'telegram'
    insta_2.name = 'insta'
    print(insta_1)
    print(insta_2)
    return insta_1

def test_adaptor():
    lang_obj = make_adopted_method()
    return lang_obj

def make_user(lang_obj, packages):
    users = []
    users_name = ['Narges Aasdi', 'Freshte Hadian','Amir Sartipi']
    for (name, package, lang) in zip(users_name, packages, lang_obj):
        users.append(User(name, package, lang))
    return users

if __name__ == "__main__":
    insta_1 = test_singleton()
    lang_obj = test_adaptor()
    packages = test_decorator()
    users = make_user(lang_obj, packages)
    test_observer(insta_1 ,users)
    insta_1.show_user_information()