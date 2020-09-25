from __future__ import annotations
from abc import ABC, abstractmethod


class MessageCreator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = (
            f"Creator: The same creator's code has just worked with {product.send()}"
        )

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class SMSMessageCreator(MessageCreator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> Message:
        return SMSMessage()


class EmailMessageCreator(MessageCreator):
    def factory_method(self) -> Message:
        return EmailMessage()


class Message(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def send(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class SMSMessage(Message):
    def send(self) -> str:
        return "Message sent by SMS"


class EmailMessage(Message):
    def send(self) -> str:
        return "Message sent by E-Mail"


def client_code(creator: MessageCreator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.some_operation()}",
        end="",
    )


if __name__ == "__main__":
    print("App: Launched with the SMSMessageCreator.")
    client_code(SMSMessageCreator())
    print("\n")

    print("App: Launched with the EmailMessageCreator.")
    client_code(EmailMessageCreator())
