#!/usr/bin/env python3
"""
Basic Web Search Agent using Agno Framework

This agent can perform web searches using DuckDuckGo and provide comprehensive answers
with proper source citations.
"""

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()


def create_web_search_agent():
    """Create and return a configured web search agent."""
    web_search_agent = Agent(
        name="Web Search Agent",
        role="Search the web for information and provide comprehensive answers",
        model=Groq(id="moonshotai/kimi-k2-instruct", api_key=os.getenv("GROQ_API_KEY")),
        tools=[DuckDuckGoTools()],
        instructions=[
            "Always search the web for current and accurate information",
            "Include sources and citations in your responses",
            "Provide comprehensive and well-structured answers",
            "If multiple sources confirm information, mention this",
            "Always verify facts through web searches when possible",
            "Current date is: " + datetime.now().strftime("%Y-%m-%d"),
        ],
        show_tool_calls=True,
        markdown=True,
    )
    return web_search_agent


def main():
    """Main function to run the web search agent."""
    agent = create_web_search_agent()
    
    print("🔍 Web Search Agent is ready!")
    print("Ask me anything and I'll search the web for the latest information.")
    print("Type 'quit' to exit.\n")
    
    while True:
        try:
            user_query = input("You: ")
            if user_query.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if user_query.strip():
                print("\n" + "="*50)
                agent.print_response(user_query, stream=True)
                print("="*50 + "\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()