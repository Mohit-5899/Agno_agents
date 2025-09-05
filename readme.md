# 🤖 Agno Agents Collection

A comprehensive collection of AI agents built with the **Agno Framework** for various tasks and use cases. This repository showcases the power and versatility of Agno-powered agents, from web search to specialized domain automation.

![GitHub Stars](https://img.shields.io/github/stars/Mohit-5899/Agno_agents?style=social)
![GitHub Forks](https://img.shields.io/github/forks/Mohit-5899/Agno_agents?style=social)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)

## 🚀 What is Agno?

[Agno](https://github.com/agno-agi/agno) is a powerful framework for building AI agents that can perform complex tasks, use tools, and interact with various APIs. It provides a simple yet powerful interface for creating sophisticated AI applications with:

- 🧠 **Multiple AI Models**: Support for OpenAI, Groq, Anthropic, and local models
- 🛠️ **Rich Tool Ecosystem**: Web search, file operations, APIs, databases, and more
- 💬 **Conversational Interfaces**: Chat, CLI, and web interfaces
- 🔗 **Easy Integration**: Simple Python API for rapid development

## 📁 Repository Structure

```
Agno_Agents/
├── README.md                    # This documentation
├── .env                        # Environment variables (API keys)
├── requirements.txt            # Project-wide dependencies
├── .gitignore                  # Git ignore rules (excludes .env files)
├── agno_codebase/              # Agno framework documentation
│   └── agno-agi-agno-*.txt    # Comprehensive Agno reference
├── web_search_agent/           # 🔍 Web Search Agent
│   ├── web_search_agent.py     # Command-line interface
│   ├── streamlit_app.py        # Modern web interface
│   ├── requirements.txt        # Agent dependencies
│   ├── README.md               # Detailed agent documentation
│   └── .gitignore             # Agent-specific ignores
├── finance_agent/              # 💼 Financial Analysis Team
│   ├── financial_analysis_team.py  # Multi-agent team for finance
│   ├── requirements.txt        # Agent dependencies
│   └── README.md               # Detailed agent documentation
└── financial_analysis_team.py  # 📊 Standalone finance team (root level)
```

## 🤖 Available Agents

### 1. 🔍 Web Search Agent

**Status**: ✅ Production Ready | **AI Model**: Groq (Kimi-K2-Instruct) | **Tools**: DuckDuckGo Search + Serper API

A sophisticated AI-powered web search agent that provides comprehensive answers with proper source citations and real-time information retrieval.

### 2. 💼 Financial Analysis Team

**Status**: ✅ Production Ready | **AI Model**: Groq (Kimi-K2-Instruct) | **Tools**: DuckDuckGo, Serper API, YFinance

A multi-agent team system that combines web search and financial data analysis for comprehensive market insights and financial performance reports.

#### ✨ Key Features
- 🌐 **Modern Web Interface**: Beautiful Streamlit UI with chat functionality
- 🔑 **Dynamic API Key**: Enter API key directly in web interface (no file setup!)
- 🔍 **Dual Search**: DuckDuckGo + Serper API for comprehensive results
- 📝 **Source Citations**: Automatic citation and verification of sources
- 🕒 **Date Awareness**: Context-aware responses with current date
- 💬 **Dual Interface**: Both web UI and command-line options
- ⚡ **Fast Responses**: Powered by Groq's high-speed inference
- 📱 **Mobile Friendly**: Responsive design works on all devices
- 🔒 **Secure**: No API keys stored permanently, session-only storage

#### 🚀 Quick Start

**Option A: Web Interface (Recommended)**
```bash
cd web_search_agent
pip install -r requirements.txt
streamlit run streamlit_app.py
```
Open browser at `http://localhost:8501` and enter your Groq API key in the sidebar!

**Option B: Command Line**
```bash
cd web_search_agent
echo "GROQ_API_KEY=your_key_here" > .env
python3 web_search_agent.py
```

#### 📖 Documentation
- [📚 Complete Web Search Agent Guide](./web_search_agent/README.md)
- [🔑 Get Free Groq API Key](https://console.groq.com/)

---

## 🔮 Upcoming Agents

### 🎯 Planned Development

| Agent | Description | Status | Expected |
|-------|-------------|--------|----------|
| 💼 **Finance Agent** | Stock analysis and portfolio management | ✅ **Available** | **Now!** |
| 📧 **Email Assistant** | Automated email management and smart responses | 🔄 Planning | Q1 2025 |
| 📊 **Data Analyst** | CSV/Excel processing with intelligent insights | 🔄 Planning | Q1 2025 |
| 🧑‍💻 **Code Reviewer** | Automated code analysis and suggestions | 🔄 Planning | Q1 2025 |
| 📝 **Content Creator** | Blog posts, articles, and creative writing | 🔄 Planning | Q1 2025 |
| 🌐 **Social Media Manager** | Content scheduling and engagement automation | 🔄 Planning | Q2 2025 |

### 🛠️ Agent Categories

| **🔍 Information & Research** | **💼 Business & Productivity** | **🎨 Creative & Content** |
|------------------------------|--------------------------------|--------------------------|
| Web Search Agent ✅ | Email Assistant 🔄 | Content Creator 🔄 |
| Research Assistant 🔄 | Data Analyst 🔄 | Social Media Manager 🔄 |
| Document Analyzer 🔄 | Finance Agent ✅ | Image Generator 🔄 |

| **🧑‍💻 Development & Tech** | **🤝 Communication** | **🏢 Enterprise** |
|---------------------------|---------------------|-------------------|
| Code Reviewer 🔄 | Customer Support 🔄 | HR Assistant 🔄 |
| API Tester 🔄 | Meeting Scheduler 🔄 | Legal Doc Review 🔄 |
| Deployment Agent 🔄 | Translation Agent 🔄 | Compliance Monitor 🔄 |

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+** installed on your system
- **Internet connection** for web-based features
- **Groq API Key** (free at [console.groq.com](https://console.groq.com/))

### 🏃‍♂️ Quick Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mohit-5899/Agno_agents.git
   cd Agno_agents
   ```

2. **Choose an agent and install dependencies:**
   ```bash
   cd web_search_agent
   pip install -r requirements.txt
   ```

3. **Run the agent:**
   ```bash
   # Web Interface (recommended)
   streamlit run streamlit_app.py
   
   # OR Command Line
   python3 web_search_agent.py
   ```

### 🔑 API Configuration

**For Web Interface:** Simply enter your API key in the sidebar - no file setup needed!

**For CLI:** Create a `.env` file with your API keys:
```env
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

**Get API Keys:**
- [Groq API Key](https://console.groq.com/) - Free tier available
- [Serper API Key](https://serper.dev/) - Free tier available

## 🏗️ Building Your Own Agent

### 📋 Agent Template

Create new agents using this structure:

```python
#!/usr/bin/env python3
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

load_dotenv()

def create_your_agent():
    """Create and configure your agent."""
    return Agent(
        name="Your Agent Name",
        role="Agent description and purpose",
        model=Groq(id="llama-3.1-70b-versatile", api_key=os.getenv("GROQ_API_KEY")),
        tools=[DuckDuckGoTools()],  # Add your tools
        instructions=[
            "Clear, specific instructions for your agent",
            "Define the agent's behavior and capabilities",
            "Include any constraints or guidelines",
        ],
        show_tool_calls=True,
        markdown=True,
    )

def main():
    """Main application logic."""
    agent = create_your_agent()
    agent.print_response("Hello! Ready to help.", stream=True)

if __name__ == "__main__":
    main()
```

### 🗂️ Directory Structure for New Agents

```
your_agent_name/
├── your_agent.py           # Main agent implementation
├── streamlit_app.py        # Web interface (optional)
├── requirements.txt        # Dependencies
├── README.md              # Documentation
├── .env.example          # Example environment file
└── .gitignore           # Ignore patterns
```

## 🛠️ Development

### Available AI Models

| Provider | Models | Use Case |
|----------|--------|----------|
| **Groq** | Llama, Mixtral | Fast inference, real-time apps |
| **OpenAI** | GPT-3.5, GPT-4, GPT-4o | General purpose, high quality |
| **Anthropic** | Claude 3 Haiku, Sonnet, Opus | Advanced reasoning, long context |
| **Local** | Ollama, LM Studio | Privacy, offline use |

### Available Tools

- **🔍 Search**: DuckDuckGo, Google, Bing, Exa
- **📁 Files**: Read, write, process documents
- **🌐 Web**: HTTP requests, scraping, APIs
- **💾 Data**: SQL, NoSQL, vector databases
- **📧 Communication**: Email, Slack, Discord
- **🎨 Media**: Image, audio, video processing

### Best Practices

- ✅ Use environment variables for API keys
- ✅ Implement comprehensive error handling
- ✅ Provide clear documentation and examples
- ✅ Follow consistent naming conventions
- ✅ Include proper logging and debugging
- ✅ Test with various input scenarios
- ✅ Implement graceful error recovery

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

1. **🆕 Create New Agents** - Build agents for new use cases
2. **🐛 Fix Bugs** - Report and fix issues
3. **📚 Improve Documentation** - Enhance guides and examples
4. **⚡ Optimize Performance** - Improve speed and efficiency
5. **🧪 Add Tests** - Increase reliability and coverage

### Contribution Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-agent`)
3. Follow our agent template structure
4. Add comprehensive documentation
5. Test thoroughly with various scenarios
6. Commit changes (`git commit -m 'Add amazing agent'`)
7. Push to your branch (`git push origin feature/amazing-agent`)
8. Open a Pull Request with detailed description

### Agent Submission Checklist

- [ ] Follows standard directory structure
- [ ] Includes comprehensive README.md
- [ ] Has requirements.txt with all dependencies
- [ ] Uses environment variables for configuration
- [ ] Implements proper error handling
- [ ] Tested with various inputs
- [ ] Updates main repository README
- [ ] Includes example usage and screenshots

## 📊 Repository Statistics

- **🤖 Active Agents**: 2 (Web Search, Finance Team)
- **🔄 In Development**: 5 planned agents
- **🚀 Languages**: Python
- **🧠 AI Models**: Groq, OpenAI, Anthropic support
- **🛠️ Tools**: DuckDuckGo, file ops, web APIs

## 🔒 Security & Privacy

- **🔐 API Key Security**: Keys never committed to repository
- **🚫 No Hardcoded Secrets**: All sensitive data via environment variables
- **🔍 Privacy-First Search**: DuckDuckGo for anonymous searches
- **🛡️ Input Validation**: Agents validate and sanitize inputs
- **📝 Minimal Logging**: Sensitive data excluded from logs
- **🗂️ Gitignore Protection**: Comprehensive exclusion of sensitive files

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **Module Import Errors** | `pip install -r requirements.txt` in correct directory |
| **API Key Errors** | Verify key in web interface or `.env` file |
| **Permission Denied** | Check file permissions: `chmod +x agent_script.py` |
| **Port Already in Use** | Change Streamlit port: `streamlit run app.py --server.port 8502` |

### Getting Help

- 📖 Check individual agent documentation
- 🔍 Search existing [GitHub Issues](https://github.com/Mohit-5899/Agno_agents/issues)
- 💬 Open a new issue with detailed problem description
- 📧 Contact maintainers for complex problems

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

```
MIT License - Feel free to use, modify, and distribute
```

## 🔗 Useful Resources

- [📚 Agno Framework Documentation](https://docs.agno.ai/)
- [🧑‍💻 Agno GitHub Repository](https://github.com/agno-agi/agno)
- [⚡ Groq API Documentation](https://console.groq.com/docs)
- [🤖 OpenAI API Documentation](https://platform.openai.com/docs)
- [🐍 Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

## 🌟 Showcase

### 📈 Success Stories

*Share your implementations and use cases!*

### 🎯 Use Case Examples

- **🏢 Business Automation**: Customer support, email management, data analysis
- **🔬 Research & Analysis**: Market research, academic research, competitive analysis  
- **🎨 Creative Projects**: Content generation, social media management, creative writing
- **🧑‍💻 Development Tools**: Code review, documentation generation, API testing

### 🏆 Community Agents

*Your agent could be featured here! Submit a PR to showcase your creation.*

---

## 🙋‍♂️ Support & Community

- **⭐ Star** this repository if you find it useful
- **🍴 Fork** to create your own agent collection  
- **📢 Share** with others who might benefit
- **🤝 Contribute** to make it even better
- **💬 Discuss** ideas and improvements in Issues

### Connect With Us

- **GitHub**: [Mohit-5899](https://github.com/Mohit-5899)
- **Repository**: [Agno_agents](https://github.com/Mohit-5899/Agno_agents)

---

<div align="center">

**🚀 Made with ❤️ using the Agno Framework**

*Building the future of AI agents, one agent at a time.*

[![Built with Agno](https://img.shields.io/badge/Built%20with-Agno-blue?style=for-the-badge)](https://github.com/agno-agi/agno)
[![Powered by Groq](https://img.shields.io/badge/Powered%20by-Groq-green?style=for-the-badge)](https://groq.com/)

</div>