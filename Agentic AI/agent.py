from agno.agent import Agent
from agno.team import Team

from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

load_dotenv()

eng_agent = Agent(name="English Agent", role="You answer questions in English")
chi_agent = Agent(name="Chinese Agent", role="You answer questions in Chinese")
bangla_agent = Agent(name="Bangla Agent", role="You answer questions in Bangla")

team_leader = Team(
    name="Answer and Translation Team",
    members=[eng_agent, chi_agent, bangla_agent],
    description="A team of agents that can answer questions in multiple languages.",
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    show_members_responses=True,
    instructions="""All Member agents must respond to answer the query int their specific language.
                    Do not route to just one agent.
                    Output the response of all agents.
            """,
)

team_leader.print_response("What is the capital of bangladesh?")

