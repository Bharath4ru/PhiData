from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv


load_dotenv()

web_agent = Agent(
    name ="Web Agent",
    model = Gemini(id="gemini-2.0-flash-exp"),
    tools =[DuckDuckGo(search=True)],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
    )

finance_agent = Agent(
    name = "Finance Agent",
    role="Get financial data",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data."],
    debug_mode=True,
    
    )

agent_team = Agent(
    model = Gemini(id="gemini-1.5-flash"),
    team = [web_agent, finance_agent],
    instructions = ["Always include sources","Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
    )

agent_team.print_response("Sumarrize analyst recommendation and share the latest news for NVDA", stream=True)
