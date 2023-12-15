"""
This script provides a custom callback handler for processing messages in a chat model, 
using the langchain library. The ChatModelStartHandler class extends the BaseCallbackHandler 
and overrides the 'on_chat_model_start' method to format and print messages using the 'boxen' 
library. Each message is printed in a box with a specific color depending on the type of message.

The 'boxen_print' function is a helper function that uses the 'boxen' library to print messages 
in a decorative box with customizable options like color and title.

Classes:
- ChatModelStartHandler: Custom callback handler for processing chat model messages.

Functions:
- boxen_print: Prints messages in a decorative box with specified color and title.

Usage:
This script can be used in a chat-based application where messages from different sources 
(system, human, AI, etc.) are to be displayed distinctively. It enhances the visual 
representation of the chat flow, making it easier to differentiate between message types.
"""
from langchain.callbacks.base import BaseCallbackHandler
from pyboxen import boxen


def boxen_print(*args, **kwargs):
    """
    Prints messages in a decorative box using the boxen library.

    This function takes message content along with optional arguments like color and title
    to format the message in a box. It enhances the readability and visual appeal of
    the printed messages in the console.

    Args:
        *args: Variable length argument list for the message content.
        **kwargs: Arbitrary keyword arguments for customization like color and title.
    """
    print(boxen(*args, **kwargs))


class ChatModelStartHandler(BaseCallbackHandler):
    """
    Custom callback handler for processing messages in a chat model.

    This class extends BaseCallbackHandler from langchain.callbacks.base. It overrides the
    'on_chat_model_start' method to format and print each message using the 'boxen_print'
    function with different colors based on the message type.

    Methods:
        on_chat_model_start: Process and print messages at the start of a chat model interaction.
    """

    def on_chat_model_start(self, serialized, messages, **kwargs):
        """
        Processes and prints messages at the start of a chat model interaction.

        This method is called when the chat model interaction begins. It iterates through
        the messages and uses the 'boxen_print' function to display each message in a
        formatted box. The color and title of the box vary based on the message type.

        Args:
            serialized: Serialized data for the chat model interaction.
            messages: A list of message objects to be processed and displayed.
            **kwargs: Arbitrary keyword arguments.
        """
        print("\n\n\n\n========== Sending Messages ==========\n\n")

        for message in messages[0]:
            # Determine the message type and print accordingly
            if message.type == "system":
                boxen_print(message.content, title=message.type, color="yellow")

            elif message.type == "human":
                boxen_print(message.content, title=message.type, color="green")

            elif message.type == "ai" and "function_call" in message.additional_kwargs:
                call = message.additional_kwargs["function_call"]
                boxen_print(
                    f"Running tool {call['name']} with args {call['arguments']}",
                    title=message.type,
                    color="cyan",
                )

            elif message.type == "ai":
                boxen_print(message.content, title=message.type, color="blue")

            elif message.type == "function":
                boxen_print(message.content, title=message.type, color="purple")

            else:
                boxen_print(message.content, title=message.type)
