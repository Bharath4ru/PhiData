from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.firecrawl import FirecrawlTools
from dotenv import load_dotenv
load_dotenv()


agent = Agent(
    tools=[FirecrawlTools(scrape=False, crawl=True)],
    model = Gemini(id="gemini-2.0-flash-exp"), 
    show_tool_calls=True, 
    markdown=True)


agent.print_response("list only test stats https://www.cricbuzz.com/profiles/8733/kl-rahul/")
