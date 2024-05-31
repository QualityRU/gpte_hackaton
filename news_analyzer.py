from aiohttp import ClientSession


class NewsAnalyzer:
    def __init__(self):
        self.news_api_url = 'https://newsapi.org/v2/everything'
        self.news_api_key = '2a009d59e361430b97a1305cc997e68f'

    async def get_news(self, query, from_date, to_date):
        self.params = {
            'q': query,
            'from': from_date,
            'to': to_date,
            'sortBy': 'publishedAt',
            'apiKey': self.news_api_key,
        }

        async with ClientSession() as session:
            async with session.get(
                url=self.news_api_url, params=self.params
            ) as response:
                data = await response.json()
                news = list()

                for article in data.get('articles'):
                    news.append(article.get('description'))

                return news
