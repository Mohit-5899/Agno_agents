#!/usr/bin/env python3
"""
Streamlit Web Interface for Web Search Agent

A modern web interface for the web search agent built with Streamlit.
Provides an intuitive chat interface for web search queries.
"""

import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="🔍 Web Search Agent",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

def create_web_search_agent(api_key):
    """Create and return a configured web search agent."""
    try:
        if not api_key:
            return None
            
        agent = Agent(
            name="Web Search Agent",
            role="Search the web for information and provide comprehensive answers",
            model=Groq(id="moonshotai/kimi-k2-instruct", api_key=api_key),
            tools=[DuckDuckGoTools()],
            instructions=[
                "Always search the web for current and accurate information",
                "Include sources and citations in your responses",
                "Provide comprehensive and well-structured answers",
                "If multiple sources confirm information, mention this",
                "Always verify facts through web searches when possible",
                "Current date is: " + datetime.now().strftime("%Y-%m-%d"),
                "Format your response in a clear, readable way",
                "Use bullet points and sections when appropriate"
            ],
            show_tool_calls=True,
            markdown=True,
        )
        return agent
    except Exception as e:
        st.error(f"❌ Error creating agent: {str(e)}")
        return None

def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "agent" not in st.session_state:
        st.session_state.agent = None
    if "api_key" not in st.session_state:
        st.session_state.api_key = os.getenv("GROQ_API_KEY", "")

def display_chat_messages():
    """Display all chat messages in the conversation."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():
    """Handle user input and generate agent response."""
    # Only show input if API key is available
    if not st.session_state.api_key:
        st.info("👆 Please enter your Groq API key in the sidebar to start chatting!")
        return
    
    if prompt := st.chat_input("Ask me anything! I'll search the web for you..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("🔍 Searching the web..."):
                try:
                    if st.session_state.agent is None:
                        st.error("❌ Agent not initialized. Please check your API key.")
                        return
                    
                    # Get response from agent
                    response = st.session_state.agent.run(prompt)
                    
                    # Display the response
                    if hasattr(response, 'content'):
                        content = response.content
                    else:
                        content = str(response)
                    
                    st.markdown(content)
                    
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": content})
                    
                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

def sidebar_configuration():
    """Create sidebar with configuration options."""
    with st.sidebar:
        st.header("🔧 Configuration")
        
        # API Key Input
        st.subheader("🔑 Groq API Key")
        
        # API Key input field
        api_key_input = st.text_input(
            "Enter your Groq API Key:",
            value=st.session_state.api_key,
            type="password",
            help="Get your free API key from https://console.groq.com/",
            placeholder="gsk_..."
        )
        
        # Update session state if API key changed
        if api_key_input != st.session_state.api_key:
            st.session_state.api_key = api_key_input
            st.session_state.agent = None  # Reset agent when API key changes
            if api_key_input:
                st.rerun()  # Refresh to create new agent
        
        # API Key status
        if st.session_state.api_key:
            st.success("✅ Groq API Key configured")
            st.caption(f"Key: ...{st.session_state.api_key[-8:]}" if len(st.session_state.api_key) > 8 else "Key: Set")
        else:
            st.error("❌ Groq API Key required")
            st.info("Get your free API key from [Groq Console](https://console.groq.com/)")
        
        # Test API Key button
        if st.session_state.api_key and st.button("🔍 Test API Key", use_container_width=True):
            with st.spinner("Testing API key..."):
                test_agent = create_web_search_agent(st.session_state.api_key)
                if test_agent:
                    st.success("✅ API key is valid!")
                else:
                    st.error("❌ Invalid API key or connection error")
        
        st.divider()
        
        # Agent Information
        st.header("🤖 Agent Info")
        st.info("""
        **Model**: Moonshot AI (Kimi-K2-Instruct)  
        **Provider**: Groq  
        **Tools**: DuckDuckGo Search  
        **Features**: Real-time web search with citations
        """)
        
        st.divider()
        
        # Usage Statistics
        st.header("📊 Session Stats")
        user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
        agent_responses = len([m for m in st.session_state.messages if m["role"] == "assistant"])
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Questions", user_messages)
        with col2:
            st.metric("Responses", agent_responses)
        
        st.divider()
        
        # Clear conversation
        if st.button("🗑️ Clear Conversation", type="secondary", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        st.divider()
        
        # Example queries
        st.header("💡 Example Queries")
        example_queries = [
            "What's the latest news about AI?",
            "Current stock price of Tesla",
            "Weather forecast for New York",
            "Best Python frameworks in 2024",
            "Latest research on climate change"
        ]
        
        for query in example_queries:
            if st.button(f"📝 {query}", key=f"example_{hash(query)}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": query})
                st.rerun()

def main_interface():
    """Create the main chat interface."""
    st.title("🔍 Web Search Agent")
    st.caption("Powered by Groq AI and DuckDuckGo Search")
    
    # Check if API key is required
    if not st.session_state.api_key:
        st.warning("🔑 **API Key Required**")
        st.markdown("""
        To use the Web Search Agent, you need a Groq API key:
        
        1. 📝 **Get your free API key** from [Groq Console](https://console.groq.com/)
        2. 🔑 **Enter it in the sidebar** on the left
        3. 🚀 **Start searching!**
        
        The Groq API is free to use and provides fast AI responses.
        """)
        return
    
    # Display welcome message if no conversation yet
    if not st.session_state.messages:
        st.markdown("""
        ### Welcome to the Web Search Agent! 👋
        
        I'm here to help you find current information from the web. I can:
        - 🔍 Search for real-time information
        - 📰 Find latest news and updates  
        - 📊 Get current data and statistics
        - 🔬 Research topics with proper citations
        - 🌍 Answer questions with web-verified facts
        
        **Just type your question below to get started!**
        """)
        
        # Display example cards
        st.markdown("#### 💡 Try these examples:")
        
        cols = st.columns(3)
        examples = [
            ("🤖 AI News", "What's the latest in artificial intelligence?"),
            ("📈 Stock Info", "Current Tesla stock price and news"),
            ("🌤️ Weather", "Weather forecast for San Francisco")
        ]
        
        for i, (title, query) in enumerate(examples):
            with cols[i % 3]:
                if st.button(title, key=f"main_example_{i}", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": query})
                    st.rerun()

def main():
    """Main application function."""
    # Initialize session state
    initialize_session_state()
    
    # Create sidebar first (so user can input API key)
    sidebar_configuration()
    
    # Initialize agent if API key is available and agent not created
    if st.session_state.api_key and st.session_state.agent is None:
        with st.spinner("🚀 Initializing Web Search Agent..."):
            st.session_state.agent = create_web_search_agent(st.session_state.api_key)
    
    # Main interface
    main_interface()
    
    # Display chat messages
    display_chat_messages()
    
    # Handle user input
    handle_user_input()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"❌ Application Error: {str(e)}")
        st.info("Please check your configuration and try again.")