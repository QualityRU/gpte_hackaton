import asyncio

import aiohttp


class PriceChecker:
    def __init__(self):
        self.coin_api_url = (
            'https://api.coinpaprika.com/v1/tickers/btc-bitcoin'
        )

    async def get_percent_change(self, period):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.coin_api_url) as response:
                data = await response.json()
                percent_change = f'percent_change_{period}'
                price_change = data['quotes']['USD'][percent_change]
                return price_change

    # async def get_price_change(self, start_date):
    #     self.coin_api_url += '/historical'
    #     self.params = {'start': start_date, 'interval': '1d'}
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get(
    #             url=self.coin_api_url, params=self.params
    #         ) as response:
    #             data = await response.json()
    #             return data
