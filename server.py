# server.py
from fastmcp import FastMCP
import math

mcp = FastMCP("Calculator Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b

@mcp.tool
def subtract(a: int, b: int) -> int:
    """Subtracts two numbers."""
    return a - b

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divides two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool
def percentage(part: float, whole: float) -> float:
    """Calculates the percentage of a part relative to a whole."""
    if whole == 0:
        raise ValueError("Whole cannot be zero.")
    return (part / whole) * 100

@mcp.tool
def power(base: float, exponent: int) -> float:
    """Raises a number to the power of another."""
    return base ** exponent

@mcp.tool
def square_root(number: float) -> float:
    """Calculates the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return number ** 0.5

@mcp.tool
def factorial(n: int) -> int:
    """Calculates the factorial of a number."""
    if n < 0:
        raise ValueError("Cannot calculate factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@mcp.tool
def fibonacci(n: int) -> int:
    """Calculates the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Cannot calculate Fibonacci of a negative number.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@mcp.tool
def gcd(a: int, b: int) -> int:
    """Calculates the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return abs(a)

@mcp.tool
def lcm(a: int, b: int) -> int:
    """Calculates the least common multiple of two numbers."""
    if a == 0 or b == 0:
        raise ValueError("Cannot calculate LCM with zero.")
    return abs(a * b) // gcd(a, b)


@mcp.tool
def is_prime(n: int) -> bool:
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@mcp.tool
def prime_factors(n: int) -> list:
    """Returns the prime factors of a number."""
    if n <= 1:
        return []
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

@mcp.tool
def sin(angle: float) -> float:
    """Calculates the sine of an angle in radians."""
    return math.sin(angle)

@mcp.tool
def cos(angle: float) -> float:
    """Calculates the cosine of an angle in radians."""
    return math.cos(angle)

@mcp.tool
def tan(angle: float) -> float:
    """Calculates the tangent of an angle in radians."""
    return math.tan(angle)

@mcp.tool
def log(x: float, base: float = math.e) -> float:
    """Calculates the logarithm of a number with a given base."""
    return math.log(x, base)

@mcp.tool
def log10(x: float) -> float:
    """Calculates the base-10 logarithm of a number."""
    return math.log10(x)

@mcp.tool
def degrees_to_radians(degrees: float) -> float:
    """Converts an angle from degrees to radians."""
    return math.radians(degrees)

@mcp.tool
def radians_to_degrees(radians: float) -> float:
    """Converts an angle from radians to degrees."""
    return math.degrees(radians)

if __name__ == "__main__":
    # mcp.run()
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000, path="/mcp/calculator")
