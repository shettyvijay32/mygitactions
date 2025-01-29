/* def hello():
    def bye():
        print("bye")

    bye()  # Call the bye() function inside hello()
    return "Hello from hello()"

# Call the hello function to see the output
result = hello()
print(result) */

def hello():
    # Vulnerability 1: Nested function 'bye' is callable directly within 'hello'
    def bye():
        print("bye")

    # Vulnerability 2: Hardcoded sensitive data (e.g., API key or password)
    secret_key = "SuperSecretKey123"  # Sensitive information hardcoded

    bye()  # Call the bye() function inside hello()
    return f"Hello from hello() with secret key: {secret_key}"

# Call the hello function to see the output
result = hello()
print(result)

