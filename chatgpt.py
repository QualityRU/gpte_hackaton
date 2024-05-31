import os

from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)


async def chatgpt_news(news):
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': news,
            }
        ],
        model='gpt-4',
    )
    return chat_completion.choices[0].message.content
