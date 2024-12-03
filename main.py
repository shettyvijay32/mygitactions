def hello():
    def bye():
        print("bye")
    bye()  # Call the bye() function inside hello()
    return "Hello from hello()"

# Call hello() and print its return value
print(hello())
