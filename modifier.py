def modify_function(link):
    colors = link[27:].split("-");
    palette = [];

    for color in colors:
        palette.append(f'"#{color}"')

    return f'[{", ".join(palette)}]'

# Modify the content
import time
import pyperclip

def modify_clipboard():
    while True:
        # Get the current clipboard content
        original_text = pyperclip.paste()

        # Modify the content
        if original_text.startswith('https://coolors.co/palette/'):
            modified_text = modify_function(original_text)

            # Set the modified text to the clipboard
            pyperclip.copy(modified_text)
            print('Modified text copied to clipboard')

        # Sleep for a short interval before checking again
        time.sleep(1)

if __name__ == '__main__':
    modify_clipboard()

    
print(modify_function("https://coolors.co/palette/264653-2a9d8f-e9c46a-f4a261-e76f51"))
