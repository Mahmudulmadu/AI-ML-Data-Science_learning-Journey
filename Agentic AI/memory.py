from agno.agent import Agent
from agno.db.sqlite import SqliteDb

from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    add_history_to_context=True,
)


groq_agent = build_agent()

groq_agent.print_response("what is the capital of bangladesh?")
groq_agent.print_response("what is best place here for visit?")