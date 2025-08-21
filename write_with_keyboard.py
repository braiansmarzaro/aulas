import time
from pynput.keyboard import Controller

# Initialize the keyboard controller
keyboard = Controller()

def type_string_with_delay(text, initial_delay=5, char_delay=0.02):
  """
  Waits for an initial period, then simulates typing a string
  character by character with a delay.

  Args:
    text (str): The string to be typed.
    initial_delay (int): The number of seconds to wait before typing begins.
    char_delay (float): The delay in seconds between each character typed.
  """
  print(f"Typing will begin in {initial_delay} seconds...")
  print("Please place your cursor in the desired text field.")
  
  # Wait for the user to position their cursor
  time.sleep(initial_delay)
  
  print("Starting to type.")
  
  # Iterate over each character in the provided string
  for char in text:
    # Simulate pressing and releasing the key for the character
    keyboard.press(char)
    keyboard.release(char)
    
    # Pause the execution for the specified character delay
    time.sleep(char_delay)
  print("...Typing complete!")

# --- Main execution block ---
if __name__ == "__main__":
  # The message you want to be typed out
  message_to_type = "I see volunteering for the World Cup as a significant responsibility, as volunteers often create the lasting impression visitors have of the event. In practice, this means being a problem-solver: knowledgeable, cheerful, and always ready to help. More than just providing information or assisting with logistics, my goal is to convey the warmth of both my city and Brazil through a positive attitude and a friendly smile. I want to be a memorable part of each visitor's positive World Cup story, helping reflect an image of our country that is not only friendly but also organized and reliable."
  
  # Call the function with the desired message
  # You can adjust the delays here if needed
  type_string_with_delay(message_to_type, initial_delay=5, char_delay=0.08)
