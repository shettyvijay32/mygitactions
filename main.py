def hello():
    def bye():
        print("bye")

    bye()  # Call the bye() function inside hello()
    return "Hello from hello()"
