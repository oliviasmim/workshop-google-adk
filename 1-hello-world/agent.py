from google.adk.agents import Agent

root_agent = Agent(
    name="greeter_agent",
    model="gemini-2.0-flash",
    description=(
        "A simple agent that greets the user to the workshop in how to use the google adk"
    ),
    instruction=(
        "You are a friendly assistant. Greet the user to the workshop and ask their name."
    ),
) 