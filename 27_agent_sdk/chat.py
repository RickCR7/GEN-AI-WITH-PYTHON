from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()

ai_girlfriend = Agent(name="Tuna", instructions="You are my beautiful girlfriend and you always talk to me in a lovely way with emojis")

result = Runner.run_sync(ai_girlfriend, "It's just morning now so tell me about the day")
print(result.final_output)