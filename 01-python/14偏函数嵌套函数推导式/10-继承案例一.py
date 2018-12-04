# 基类（父类）
class BasePage(object):
    def show_header(self):
        print("我是头部信息")

    def show_footer(self):
        print("我是底部信息")

    def show_body(self):
        print("我是BasePage主体信息")

# 首页类
class HomePage(BasePage):

    def show_body(self):
        print("我是HomePage主体信息")

# 新闻类
class NewsPage(BasePage):

    def show_body(self):
        print("我是NewsPage主体信息")

# 产品类
class Product(BasePage):

    def show_body(self):
        print("我是Product主体信息")


if __name__ == '__main__':
    home_page = HomePage()
    home_page.show_body()

    news_page = NewsPage()
    news_page.show_body()

    product = Product()
    product.show_body()

