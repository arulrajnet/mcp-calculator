# MCP Calculator

A Model Context Protocol (MCP) server example with calculator tools, built using FastMCP.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### 1. Clone the Repository
```bash
git clone https://github.com/arulrajnet/mcp-calculator.git
cd mcp-calculator
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
# Install the package in development mode
pip install -e .

# Or install with development dependencies
pip install -e .[dev]
```

## Running the Server

Start the MCP calculator server:

```bash
python server.py
```

The server will start on `http://localhost:8000/mcp/calculator` using the streamable HTTP transport.

You should see output similar to:
```
Uvicorn running on http://0.0.0.0:8000
```

## Testing with the Client

### 1. Run the Test Client
In a new terminal (while the server is running):

```bash
python client.py
```

This will connect to the server and list all available tools.

### 2. Example Client Usage
You can modify `client.py` to test specific calculator functions:

```python
from fastmcp import Client
import asyncio

async def main():
    # Connect via SSE
    async with Client("http://localhost:8000/mcp/calculator") as client:
        # List available tools
        tools = await client.list_tools()
        print(f"Available tools: {[tool['name'] for tool in tools]}")

        # Test some calculations
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"5 + 3 = {result}")

        result = await client.call_tool("factorial", {"n": 5})
        print(f"5! = {result}")

        result = await client.call_tool("is_prime", {"n": 17})
        print(f"Is 17 prime? {result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Development

### Code Formatting
```bash
black .
isort .
```

### Type Checking
```bash
mypy .
```

### Running Tests
```bash
pytest
```

### Running Tests with Coverage
```bash
pytest --cov=. --cov-report=html
```

## Author

<p align="center">
  <a href="https://x.com/arulrajnet">
    <img src="https://github.com/arulrajnet.png?size=100" alt="Arulraj V" width="100" height="100" style="border-radius: 50%;" class="avatar-user">
  </a>
  <br>
  <strong>Arul</strong>
  <br>
  <a href="https://x.com/arulrajnet">
    <img src="https://img.shields.io/badge/Follow-%40arulrajnet-1DA1F2?style=for-the-badge&logo=x&logoColor=white" alt="Follow @arulrajnet on X">
  </a>
  <a href="https://github.com/arulrajnet">
    <img src="https://img.shields.io/badge/GitHub-arulrajnet-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub @arulrajnet">
  </a>
  <a href="https://linkedin.com/in/arulrajnet">
    <img src="https://custom-icon-badges.demolab.com/badge/LinkedIn-arulrajnet-0A66C2?style=for-the-badge&logo=linkedin-white&logoColor=white" alt="LinkedIn @arulrajnet">
  </a>
</p>

