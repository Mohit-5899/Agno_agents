import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.serper import SerperTools
from agno.tools.yfinance import YFinanceTools
from agno.team import Team

load_dotenv("../.env")

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="moonshotai/kimi-k2-instruct", api_key=os.getenv("GROQ_API_KEY")),
    tools=[DuckDuckGoTools(), SerperTools(api_key=os.getenv("SERPER_API_KEY"))],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="moonshotai/kimi-k2-instruct", api_key=os.getenv("GROQ_API_KEY")),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Act as a financial analyst and provide comprehensive and well-structured answers and also cordinate with {web_agent} to get the latest information",
    show_tool_calls=True,
    markdown=True,
)

agent_team = Team(
    mode="coordinate",
    members=[web_agent, finance_agent],
    model=Groq(id="moonshotai/kimi-k2-instruct", api_key=os.getenv("GROQ_API_KEY")),
    success_criteria="A comprehensive financial news report with clear sections and data-driven insights.",
    instructions=["Always include sources", "Use tables to display data", "Cordinate with {web_agent} to get the latest information"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("What's the market outlook and financial performance of AI semiconductor companies?", stream=True)