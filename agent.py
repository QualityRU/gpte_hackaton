from datetime import datetime, timedelta

from chatgpt import chatgpt_news
from news_analyzer import NewsAnalyzer
from price_checker import PriceChecker


class Agent:
    async def get_analysis(self):
        price_checker = PriceChecker()
        news_analyzer = NewsAnalyzer()

        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

        percent_change = await price_checker.get_percent_change(period='7d')
        news = await news_analyzer.get_news(
            query='bitcoin', from_date=start_date, to_date=end_date
        )
        news = list(filter(lambda x: x is not None, news))
        news_for_ai = '\n'.join(news)
        ai_news = await chatgpt_news(
            f'Обобщи тезисно как эксперт почему на русском:\n{news_for_ai}'
        )

        result = f'Изменение цены за 7 дней: {percent_change}%\nНовостная выжимка:\n{ai_news}'

        return result
