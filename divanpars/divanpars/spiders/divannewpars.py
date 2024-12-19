import scrapy

class LightSourcesSpider(scrapy.Spider):
    name = 'light_sources'
    allowed_domains = ['divan.ru']
    start_urls = [
        'https://www.divan.ru/category/svetilniki-i-lampy/',  # URL с источниками освещения (пример)
    ]

    def parse(self, response):
        # Проходим по каждому товару на странице
        products = response.css('div.card-item')  # Обновите селектор под реальную структуру сайта

        for product in products:
            yield {
                'name': product.css('div.card-item__title::text').get().strip(),  # Название товара
                'price': product.css('span.card-item__price_value::text').get().strip(),  # Цена
                'url': product.css('a.card-item__link::attr(href)').get(),  # Ссылка на товар
            }

        # Пагинация: Переходим на следующую страницу, если она есть
        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)