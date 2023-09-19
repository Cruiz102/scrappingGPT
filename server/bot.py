import pyautogui

import pyautogui
import time


def login_to_app(username, password):
    """
    Login to the chatbot application.
    """
    #  Google authetification way
    pyautogui.click("images/login.png")
    time.sleep(2)
    pyautogui.click("images/continue_with_google.png")
    time.sleep(2)
    pyautogui.click("images/cesar.png")
    

import pyautogui

def click_button_by_color(target_color, tolerance=10):
    """
    Clicks a button on the screen identified by its color.
    
    :param target_color: The RGB color of the button.
    :param tolerance: A tolerance value to match colors that are close to the target_color.
    """
    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Iterate over the screen
    for x in range(screen_width):
        for y in range(screen_height):
            # Get the color of the pixel at the current location
            pixel_color = pyautogui.pixel(x, y)
            
            # Check if the pixel color matches the target color within the tolerance
            if all([abs(target - current) <= tolerance for target, current in zip(target_color, pixel_color)]):
                # Click the button
                pyautogui.click(x, y)
                return True  # Return True if the button is found and clicked

    return False  # Return False if the button is not found

# Use the function
button_color = (255, 0, 0)  # For example, red color. Replace with the actual RGB value of your button.
if not click_button_by_color(button_color):
    print("Button not found!")


def wait_for_response():
    selected_text = ""
    while True:
        # Use a hotkey combination to select all text (e.g., Ctrl+A for many applications)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)  # Allow some time for the selection to occur
        
        # Copy the selected text to the clipboard
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)  # Allow some time for copying to clipboard

        # Get the copied text
        selected_text = pyautogui.paste()

        # Check conditions
        if "Stop generating" in selected_text:
            # If "Stop generating" is found or the specific button image is found, keep waiting
            button_image_location = pyautogui.locateOnScreen('button_image.png')
            if button_image_location:
                time.sleep(5)  # Wait for a bit before checking again
                continue
        elif "Regenerate" in selected_text:
            # If "Regenerate" is found, break the loop
            break

        time.sleep(5)  # Wait for a bit before the next check

    return selected_text


def interact_with_chatbot(message):
    """
    Send a message to the chatbot and retrieve its response.
    """
    # Locate the chat input box and send button
    pyautogui.click("images/send_message.png")
    time.sleep(2)
    pyautogui.write(message)
    pyautogui.click("images/send.png")
    print(wait_for_response())
    




def read_from_chat():
    # Use pyautogui to capture chat content
    # This is a placeholder, you'd need to provide the specifics
    chat_content = pyautogui.screenshot()
    return chat_content

def send_to_chat(message):
    # Use pyautogui to send messages to the chat
    pyautogui.write(message)



if __name__ == "__main__":
    button_color = (25,195,125)  # This is just an example for a red button. Replace with the actual RGB value of your button.
    button_clicked = click_button_by_color(button_color)
    if button_clicked:
        print("Button clicked successfully!")
    else:
        print("Button not found!")

    # interact_with_chatbot("Hola como estas")
    # pyautogui.click("images/login.png")
    # time.sleep(2)
    # pyautogui.click("images/continue_with_google.png")
    # time.sleep(2)
    # pyautogui.click("images/cesar.png")

    