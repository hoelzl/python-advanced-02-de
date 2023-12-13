from .formal import formal_names, say_greetings
from .informal import familiar_names, say_hi


def say_hello(name=""):
    """Says hello to a person."""
    if name == "":
        print("Hello!")
    else:
        print(f"Hello, {name}!")


def greet(name=""):
    """Greets a person."""
    if name in familiar_names:
        say_hi(name)
    elif name in formal_names:
        say_greetings(name)
    else:
        say_hello(name)
