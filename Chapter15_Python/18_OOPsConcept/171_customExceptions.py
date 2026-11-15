# Create a class for custom exceptions in Python. Custom exceptions allow you to define your own error types, which can be useful for handling specific error conditions in your code. Below is an example of how to create a custom exception class:


class InvalidException(Exception):
    pass

    def can_you_drink(age):
        if age < 0:
            raise InvalidException("Age cannot be negative.")
        if age < 21:
            raise InvalidException("You are not old enough to drink.")
        return True