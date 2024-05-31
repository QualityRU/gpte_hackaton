from asyncio import run

from agent import Agent


async def main():
    agent = Agent()
    response = await agent.get_analysis()
    print(response)


if __name__ == '__main__':
    run(main())
