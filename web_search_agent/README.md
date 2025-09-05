# 🔍 Web Search Agent

A sophisticated AI-powered web search agent built using the **Agno Framework** with **Groq's Moonshot AI** and **DuckDuckGo** search capabilities. This agent provides intelligent web search functionality with comprehensive answers, proper source citations, and real-time information retrieval.

## ✨ Features

- **🚀 Fast AI Responses**: Powered by Groq's Moonshot AI (Kimi-K2-Instruct model)
- **🔍 Dual Search**: Real-time web search using DuckDuckGo + Serper API
- **📝 Source Citations**: Automatically includes sources and citations in responses
- **💬 Interactive CLI**: User-friendly command-line interface
- **🌐 Streamlit Web UI**: Modern web interface with chat functionality
- **🕒 Date Awareness**: Agent knows the current date for time-sensitive queries
- **📊 Markdown Support**: Formatted responses with proper markdown rendering
- **🔧 Tool Call Visibility**: Shows search operations for transparency
- **⚡ Stream Processing**: Real-time streaming responses
- **🔒 Environment Variables**: Secure API key management with dotenv

## 🏗️ Architecture

### Core Components

1. **Agent Configuration**: 
   - Uses Groq's `moonshotai/kimi-k2-instruct` model
   - Configured with comprehensive search instructions
   - Date-aware responses

2. **Search Tools**:
   - `DuckDuckGoTools()` for privacy-focused web search
   - `SerperTools()` for enhanced Google search results
   - Real-time information retrieval with dual search capabilities

3. **Environment Management**:
   - `.env` file for API key storage
   - Secure credential handling

### Code Structure

```
web_search_agent/
├── web_search_agent.py    # Command-line application
├── streamlit_app.py       # Streamlit web interface
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
├── .env                  # Environment variables (create this)
└── .gitignore           # Git ignore rules
```

## 📦 Dependencies

- **agno**: Core Agno framework for AI agents
- **ddgs**: DuckDuckGo search functionality
- **google-search-results**: Serper API for enhanced search
- **groq**: Groq API client for AI model access
- **python-dotenv**: Environment variable management
- **streamlit**: Modern web interface framework

## 🚀 Quick Start

### 1. Installation

Clone or download this project and navigate to the directory:

```bash
cd web_search_agent
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Environment Setup

**Option A: Web Interface (Recommended)**
- No environment setup needed! 
- You'll enter your API key directly in the web interface

**Option B: CLI Interface**
Create a `.env` file in the project root:

```bash
touch .env
```

Add your Groq API key to the `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

**Get your API keys**: 
- **Groq API key**: Visit [Groq Console](https://console.groq.com/) to obtain your free API key
- **Serper API key**: Visit [Serper.dev](https://serper.dev/) to obtain your free API key

### 3. Run the Agent

You can run the agent in two ways:

#### Option A: Streamlit Web Interface (Recommended)
```bash
streamlit run streamlit_app.py
```
This opens a modern web interface at `http://localhost:8501`

**✨ No API key setup needed!** Just enter your Groq API key in the sidebar when the app loads.

#### Option B: Command Line Interface
```bash
python3 web_search_agent.py
```
This runs the agent in terminal/command line mode

## 💡 Usage Examples

Once the agent is running, you can ask various types of questions:

### News & Current Events
```
You: What's the latest news about AI developments?
You: Current stock price of Tesla
You: What happened in the tech industry today?
```

### Research Queries
```
You: Latest research on climate change
You: Best practices for Python development in 2024
You: Compare different AI models available today
```

### General Information
```
You: Weather forecast for New York
You: How to install Docker on Ubuntu
You: What are the benefits of renewable energy?
```

### Exit Commands
```
quit
exit
q
```

## 🌐 Streamlit Web Interface

The Streamlit interface provides a modern, user-friendly web experience:

### ✨ Web Interface Features

- **💬 Chat Interface**: Natural conversation flow with message history
- **🎨 Modern UI**: Clean, responsive design that works on desktop and mobile
- **⚙️ Configuration Panel**: Real-time status monitoring and settings
- **📊 Session Statistics**: Track questions asked and responses received
- **💡 Example Queries**: One-click access to common search types
- **🗑️ Clear Conversation**: Reset chat history with a single click
- **🔄 Real-time Updates**: Live search progress indicators
- **📱 Mobile Friendly**: Responsive design for all devices
- **🔑 Dynamic API Key**: Enter API key directly in the interface (no file setup needed)
- **🔍 Key Validation**: Test API key functionality with one click

### 🖥️ Interface Sections

#### Main Chat Area
- **Welcome Screen**: Helpful introduction and example cards
- **Message History**: Full conversation context with user and agent messages
- **Input Field**: Natural language query input with auto-focus
- **Search Indicators**: Visual feedback during web searches

#### Sidebar Configuration
- **🔑 API Key Input**: Secure password field for your Groq API key
- **✅ API Status**: Real-time connection status and key validation
- **🔍 Test API Key**: One-click API key verification button
- **🤖 Agent Information**: Model details and capabilities overview
- **📊 Session Statistics**: Usage metrics and conversation stats
- **💡 Quick Examples**: Pre-built queries for common use cases
- **🗑️ Settings**: Conversation management and preferences

### 🚀 Launching the Web Interface

```bash
# Navigate to the agent directory
cd web_search_agent

# Install dependencies (if not done already)
pip install -r requirements.txt

# Launch the Streamlit app (no environment setup needed!)
streamlit run streamlit_app.py
```

The interface will automatically open in your default browser at `http://localhost:8501`

### 📱 Using the Web Interface

1. **🔑 Enter API Key**: First, enter your Groq API key in the sidebar
2. **✅ Verify Connection**: Use the "Test API Key" button to verify it works  
3. **📝 Start Chatting**: Type your query in the chat input at the bottom
4. **🔍 View Results**: Watch as the agent searches and provides comprehensive answers
5. **💡 Try Examples**: Click sidebar examples or main page cards for quick queries
6. **📊 Monitor Usage**: Check the sidebar for API connection and usage statistics
7. **🗑️ Clear History**: Use the sidebar button to start fresh conversations

**🔒 Security Note**: Your API key is only stored in your browser session and is never saved to disk.

## 🛠️ Configuration

### Agent Instructions

The agent is configured with the following instructions:
- Always search the web for current and accurate information
- Include sources and citations in responses
- Provide comprehensive and well-structured answers
- Cross-verify information from multiple sources
- Include current date context for time-sensitive queries

### Model Configuration

- **Model**: `moonshotai/kimi-k2-instruct`
- **Provider**: Groq
- **Features**: Fast inference, high-quality responses
- **Context**: Date-aware processing

## 🔧 Customization

### Changing the AI Model

To use a different Groq model, modify line 24 in `web_search_agent.py`:

```python
model=Groq(id="llama-3.1-70b-versatile", api_key=os.getenv("GROQ_API_KEY")),
```

### Adding Custom Instructions

Modify the `instructions` list in the `create_web_search_agent()` function:

```python
instructions=[
    "Always search the web for current and accurate information",
    "Include sources and citations in your responses",
    # Add your custom instructions here
    "Focus on providing actionable insights",
]
```

### Environment Variables

You can add additional environment variables to the `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
DEBUG_MODE=false
MAX_SEARCH_RESULTS=10
```

## 🚨 Error Handling

The agent includes comprehensive error handling for:

- **API Connection Issues**: Graceful handling of network problems
- **Invalid API Keys**: Clear error messages for authentication issues
- **Search Failures**: Fallback responses when searches fail
- **User Interruption**: Clean exit with Ctrl+C
- **General Exceptions**: Logged errors with continued operation

## 🔒 Security & Privacy

- **API Key Security**: Keys stored in environment variables, not in code
- **No Data Storage**: Agent doesn't store conversation history by default
- **Dual Search Engines**: Uses both DuckDuckGo (privacy-focused) and Serper (comprehensive results)
- **Gitignore Protection**: Sensitive files excluded from version control

## 📋 Requirements

### System Requirements
- Python 3.7 or higher
- Internet connection for web searches
- Terminal/Command line access

### API Requirements
- Valid Groq API key (free tier available)
- Serper API key required for enhanced Google search results (free tier available)

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: 
   ```bash
   pip install -r requirements.txt
   ```

2. **API Key Errors**: 
   - Check your `.env` file exists
   - Verify your Groq API key is correct
   - Ensure no extra spaces in the key

3. **Permission Errors**:
   ```bash
   chmod +x web_search_agent.py
   ```

4. **Virtual Environment Issues**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Related Links

- [Agno Framework Documentation](https://docs.agno.ai/)
- [Groq API Documentation](https://console.groq.com/docs)
- [DuckDuckGo Search API](https://duckduckgo.com/api)

## 🙋‍♂️ Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the error messages carefully
3. Ensure all dependencies are installed correctly
4. Verify your API key is set up properly

---

**Made with ❤️ using the Agno Framework and Groq AI**