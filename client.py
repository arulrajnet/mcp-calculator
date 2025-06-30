from fastmcp import Client
import asyncio

async def main():
    # Connect via SSE
    async with Client("http://localhost:8000/mcp/calculator") as client:
        # List available tools
        tools = await client.list_tools()
        print(f"Available tools: {[tool.name for tool in tools]}")
        print(f"Total tools: {len(tools)}")
        print()

        # Test some basic calculations
        print("Testing basic operations:")
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"5 + 3 = {result}")

        result = await client.call_tool("multiply", {"a": 4, "b": 7})
        print(f"4 × 7 = {result}")

        result = await client.call_tool("divide", {"a": 15, "b": 3})
        print(f"15 ÷ 3 = {result}")
        print()

        # Test advanced functions
        print("Testing advanced functions:")
        result = await client.call_tool("factorial", {"n": 5})
        print(f"5! = {result}")

        result = await client.call_tool("fibonacci", {"n": 10})
        print(f"10th Fibonacci number = {result}")

        result = await client.call_tool("is_prime", {"n": 17})
        print(f"Is 17 prime? {result}")

        result = await client.call_tool("gcd", {"a": 48, "b": 18})
        print(f"GCD of 48 and 18 = {result}")
        print()

        # Test trigonometric functions
        print("Testing trigonometric functions:")
        angle_deg = 45
        angle_rad = await client.call_tool("degrees_to_radians", {"degrees": angle_deg})
        print(f"{angle_deg}° = {angle_rad} radians")

        sin_result = await client.call_tool("sin", {"angle": angle_deg})
        print(f"sin({angle_deg}°) = {sin_result}")

if __name__ == "__main__":
    asyncio.run(main())
