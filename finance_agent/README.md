# 💼 Financial Analysis Team

A sophisticated multi-agent AI system built using the **Agno Framework** with **Groq's Kimi-K2-Instruct** model for comprehensive financial analysis and market research. This team combines web search capabilities with financial data analysis to provide comprehensive market insights.

## ✨ Features

- **🤝 Multi-Agent Coordination**: Two specialized agents working together
- **🔍 Web Search Agent**: Real-time market news and information retrieval
- **📊 Finance Agent**: Stock prices, analyst recommendations, and financial data
- **🌐 Dual Search**: DuckDuckGo + Serper API for comprehensive results
- **📈 YFinance Integration**: Real-time stock data and financial metrics
- **🚀 Fast AI Responses**: Powered by Groq's Kimi-K2-Instruct model
- **📝 Comprehensive Reports**: Structured analysis with clear sections
- **🔧 Tool Call Visibility**: Shows search and data operations for transparency
- **⚡ Stream Processing**: Real-time streaming responses
- **🔒 Environment Variables**: Secure API key management

## 🏗️ Architecture

### Team Structure

The Financial Analysis Team consists of two coordinated agents:

#### 1. **Web Agent**
- **Role**: Search the web for market information and news
- **Tools**: DuckDuckGo Search, Serper API
- **Instructions**: Always include sources for information

#### 2. **Finance Agent**
- **Role**: Get financial data and provide analysis
- **Tools**: YFinance (stock prices, analyst recommendations, company info)
- **Instructions**: Use tables to display data, coordinate with web agent

#### 3. **Team Coordinator**
- **Mode**: Coordinate between agents
- **Success Criteria**: Comprehensive financial reports with clear sections and data-driven insights
- **Instructions**: Include sources, use tables, coordinate information gathering

### Code Structure

```
finance_agent/
├── financial_analysis_team.py  # Multi-agent team implementation
├── requirements.txt           # Python dependencies
├── README.md                 # This documentation
└── .env                     # Environment variables (create this)
```

## 📦 Dependencies

- **agno**: Core Agno framework for AI agents
- **groq**: Groq API client for AI model access
- **duckduckgo-search**: DuckDuckGo search functionality
- **google-search-results**: Serper API for enhanced search
- **yfinance**: Yahoo Finance data retrieval
- **python-dotenv**: Environment variable management

## 🚀 Quick Start

### 1. Installation

Navigate to the finance agent directory:

```bash
cd finance_agent
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Environment Setup

The script looks for environment variables in the parent directory. Create a `.env` file in the project root:

```bash
cd .. # Go to project root
touch .env
```

Add your API keys to the `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

**Get your API keys**:
- **Groq API key**: Visit [Groq Console](https://console.groq.com/) for free access
- **Serper API key**: Visit [Serper.dev](https://serper.dev/) for free access

### 3. Run the Financial Analysis Team

```bash
cd finance_agent  # Back to agent directory
python3 financial_analysis_team.py
```

The team will automatically analyze AI semiconductor companies' market outlook and financial performance.

## 💡 Usage Examples

### Default Analysis

The script comes pre-configured to analyze:
```
"What's the market outlook and financial performance of AI semiconductor companies?"
```

### Custom Analysis

To analyze different topics, modify the query in `financial_analysis_team.py`:

```python
agent_team.print_response("Your custom financial query here", stream=True)
```

### Example Queries

- **Market Analysis**: "What's the current state of the renewable energy market?"
- **Stock Performance**: "Analyze Tesla's financial performance over the last quarter"
- **Sector Comparison**: "Compare the performance of tech giants vs traditional banks"
- **Investment Research**: "What are the best investment opportunities in AI stocks?"
- **Economic Analysis**: "How is inflation affecting the housing market?"

## 🛠️ Configuration

### Model Configuration

All agents use the same model configuration:
- **Model**: `moonshotai/kimi-k2-instruct`
- **Provider**: Groq
- **Features**: Fast inference, high-quality responses
- **API Key**: Retrieved from environment variables

### Agent Instructions

#### Web Agent Instructions:
- Always include sources
- Search for current and accurate information
- Provide comprehensive answers

#### Finance Agent Instructions:
- Use tables to display data
- Act as a financial analyst
- Coordinate with web agent for latest information

#### Team Instructions:
- Always include sources
- Use tables to display data
- Coordinate between agents for comprehensive analysis

### Success Criteria

The team is configured to deliver:
> "A comprehensive financial news report with clear sections and data-driven insights."

## 🔧 Customization

### Changing the Analysis Query

Modify the last line in `financial_analysis_team.py`:

```python
agent_team.print_response("Your custom query here", stream=True)
```

### Adding Custom Instructions

Modify the agent configurations:

```python
web_agent = Agent(
    # ... existing configuration ...
    instructions=[
        "Always include sources",
        "Focus on recent market developments",  # Add custom instruction
        "Prioritize reliable financial sources"
    ],
)
```

### Modifying YFinance Tools

Customize the financial data tools:

```python
finance_agent = Agent(
    # ... existing configuration ...
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
        historical_data=True,  # Add historical data
        financial_statements=True,  # Add financial statements
    )],
)
```

## 📊 Output Format

The team provides structured output including:

### Market Analysis
- Current market conditions
- Recent news and developments
- Industry trends and outlook

### Financial Data
- Stock prices and performance metrics
- Analyst recommendations
- Company information and fundamentals

### Comprehensive Reports
- Executive summary
- Data-driven insights
- Source citations
- Tabulated financial metrics

## 🚨 Error Handling

The team includes error handling for:

- **API Connection Issues**: Graceful handling of network problems
- **Invalid API Keys**: Clear error messages for authentication issues
- **Data Retrieval Failures**: Fallback responses when data sources fail
- **Model Errors**: Handling of deprecated or unavailable models
- **General Exceptions**: Logged errors with continued operation

## 🔒 Security & Privacy

- **API Key Security**: Keys stored in environment variables, not in code
- **No Data Storage**: Team doesn't store conversation history by default
- **Dual Search Privacy**: DuckDuckGo for privacy, Serper for comprehensive results
- **Gitignore Protection**: Sensitive files excluded from version control
- **Environment Isolation**: Uses parent directory .env for security

## 📋 Requirements

### System Requirements
- Python 3.7 or higher
- Internet connection for web searches and financial data
- Terminal/Command line access

### API Requirements
- Valid Groq API key (free tier available)
- Valid Serper API key (free tier available)
- No additional API keys required for YFinance

## 🐛 Troubleshooting

### Common Issues

1. **Model Decommissioned Error**:
   ```bash
   ERROR: The model `llama-3.1-70b-versatile` has been decommissioned
   ```
   **Solution**: The script now uses `moonshotai/kimi-k2-instruct` which is currently supported.

2. **ModuleNotFoundError**:
   ```bash
   pip install -r requirements.txt
   ```

3. **API Key Errors**:
   - Check your `.env` file exists in the project root
   - Verify your API keys are correct
   - Ensure no extra spaces in the keys
   - Test keys individually with simple API calls

4. **Environment File Not Found**:
   ```bash
   # Ensure .env is in the parent directory
   cd .. # Go to project root
   ls -la .env # Check if file exists
   ```

5. **Permission Errors**:
   ```bash
   chmod +x financial_analysis_team.py
   ```

6. **YFinance Data Errors**:
   - Check internet connection
   - Verify stock symbols are correct
   - Some data may be delayed or unavailable

### Debug Mode

Add debug information by modifying the script:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/finance-enhancement`)
3. Commit your changes (`git commit -m 'Add finance enhancement'`)
4. Push to the branch (`git push origin feature/finance-enhancement`)
5. Open a Pull Request

### Enhancement Ideas

- Add more financial data sources (Alpha Vantage, Quandl)
- Implement portfolio analysis capabilities
- Add cryptocurrency analysis
- Create sector-specific analysis templates
- Add risk assessment tools
- Implement automated report generation

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Related Links

- [Agno Framework Documentation](https://docs.agno.ai/)
- [Groq API Documentation](https://console.groq.com/docs)
- [Serper API Documentation](https://serper.dev/api-documentation)
- [YFinance Documentation](https://pypi.org/project/yfinance/)
- [DuckDuckGo Search API](https://duckduckgo.com/api)

## 🙋‍♂️ Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the error messages carefully
3. Ensure all dependencies are installed correctly
4. Verify your API keys are set up properly
5. Check that you're using supported models

For complex issues:
- Review individual agent logs
- Test API keys independently
- Check network connectivity
- Verify environment variable loading

---

**Made with ❤️ using the Agno Framework and Groq AI**

### Example Output

```
🤖 Financial Analysis Team is analyzing AI semiconductor companies...

📊 Market Outlook:
- AI semiconductor market showing strong growth
- Key players: NVIDIA, AMD, Intel, TSMC
- Market drivers: AI adoption, data center demand

💰 Financial Performance:
[TABLE: Stock prices, P/E ratios, revenue growth]

📈 Analyst Recommendations:
- NVIDIA: Strong Buy (avg target: $150)
- AMD: Buy (avg target: $120)
- Intel: Hold (avg target: $35)

🔍 Sources:
- Yahoo Finance
- Recent market news
- Analyst reports

📋 Investment Insights:
[Comprehensive analysis based on data]
```