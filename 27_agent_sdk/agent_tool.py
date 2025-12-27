from dotenv import load_dotenv
import requests
from agents import Agent, Runner
from agents import WebSearchTool, function_tool

load_dotenv()

@function_tool
def get_weather(city: str):
    """
    Fetch the weather for a given city.
    
    Args: 
        city: The city name to fetch the weather for.
    """
 
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    
    return "Something went wrong❌❌"


tool_agent = Agent(name="Agent 007", instructions="You are a smart AI assistant who can help the user with anything",
tools=[
    WebSearchTool(), # Hosted tools
    get_weather # Function tools
])

result = Runner.run_sync(tool_agent, "Can you tell me what is the temparature of Burnpur 713325?")

print(result.final_output)