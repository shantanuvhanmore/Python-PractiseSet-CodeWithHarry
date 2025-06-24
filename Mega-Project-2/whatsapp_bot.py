import pyautogui
import pyperclip
import time
import re
import os
import openai  # Make sure you set your API key below or via environment

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to click at a specific location
def click_at(x, y, t=0.5):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(t)

# Function to check if last message was sent by a specific sender
def last_is_sender(sender_name, chat):
    lines = chat.strip().split('\n')
    last_message = ""
    
    # Go in reverse to find the last message that starts with a timestamp
    for i in range(len(lines) - 1, -1, -1):
        if re.match(r"\[\d{2}-\d{2}-\d{4} \d{2}:\d{2}\]", lines[i]):
            # Found the beginning of the last message
            last_message = lines[i]
            # Check if the next lines (until next timestamp or end) are part of it
            j = i + 1
            while j < len(lines) and not re.match(r"\[\d{2}-\d{2}-\d{4} \d{2}:\d{2}\]", lines[j]):
                last_message += " " + lines[j]
                j += 1
            break

    # Extract the sender name from the message
    try:
        start = last_message.index("] ") + 2
        end = last_message.index(":", start)
        sender = last_message[start:end].strip()
        return sender.lower() == sender_name.lower()
    except ValueError:
        print(f"Could not extract sender name and last message was '{last_message}'")
        return False

# Function to call OpenAI and get a response
def get_openai_response(prompt):
    print("inside get_responce func ..")
    personality = (
    "You are a chatbot who mimics the chats like shantanuvhanmore😏. "
    "You analyze the chats and language and reply according to the language and style as shantanuvhanmore😏. "
    "You are a fun, lovely person and great with witty banter. "
    "If it's a girl (except shantanuvhanmore😏), then replies should be a little playful and flirtatious."
    "just return reply text"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Change to gpt-4 if needed
        messages=[
            {"role": "system", "content": personality},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.8
    )

    res = response['choices'][0]['message']['content'].strip()
    print(res)
    return res



def main():

    sender_name = input("Enter who do you want to message: ")
    # opening whatspp
    pyautogui.keyDown('winleft')
    pyautogui.press('2')
    pyautogui.keyUp('winleft')

    #search bar 
    pyautogui.hotkey('ctrl', 'f')

    #paste sender name 
    pyperclip.copy(sender_name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.7)

    # select chat from search
    click_at(189,169)
    time.sleep(0.7)

    #search cancel
    click_at(386,108, 1.0)
    try:
        #Infinite loop
        while True:

            #Click and drag to select chat region
            pyautogui.rightClick(438,116)
            time.sleep(3.0)

            pyautogui.doubleClick(472,145)
            time.sleep(2.0)

            pyautogui.leftClick(438,116)
            time.sleep(2.0)

            #scroll down
            pyautogui.scroll(-500)

            # Hold down the Shift key
            pyautogui.keyDown('shift')

            # Click at desired position (e.g., x=500, y=500)
            pyautogui.click(478,626)

            # Release the Shift key
            pyautogui.keyUp('shift')
            time.sleep(1.0)

            # Copy selected chat to clipboard
            click_at(1157,70) #copy button
            time.sleep(1.0)

        
            chat = pyperclip.paste()
            print(chat)

            # Click at chatbx
            click_at(571,698)
            # Check if last sender is Aditya Tilekar
            if last_is_sender(sender_name, chat):
                print("ai responce loading...")
                # Call OpenAI function
                ai_response = get_openai_response(chat)
                time.sleep(4.0)

                # Paste chat (or response if you prefer)
                pyperclip.copy(ai_response)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.3)

                # Press Enter
                pyautogui.press('enter')

            # Optional delay before next check
            time.sleep(5)
    except: KeyboardInterrupt



if __name__ == "__main__":
    main()

