import requests
import time

# Microsoft Teams API endpoint for sending messages
send_message_url = "https://graph.microsoft.com/v1.0/me/chats/{chat_id}/messages"

# Predefined reply
reply_message = "bibitki"

# Microsoft Teams access token
access_token = "<your_access_token>"

# ID of the chat or conversation to monitor and send replies
chat_id = "<chat_id>"

# Loop to continuously check for new messages
while True:
    try:
        # Make a GET request to the Microsoft Teams API to get the latest messages
        response = requests.get(f"https://graph.microsoft.com/v1.0/me/chats/{chat_id}/messages",
                                headers={"Authorization": f"Bearer {access_token}"})

        # Check if the response was successful
        if response.status_code == 200:
            messages = response.json().get('value', [])

            # Iterate over the messages
            for message in messages:
                # Check if the message is new
                if message.get('isRead') is False:
                    # Get the sender's user ID
                    sender_id = message['from']['user']['id']

                    # Send a reply message
                    requests.post(send_message_url.format(chat_id=chat_id),
                                  headers={"Authorization": f"Bearer {access_token}"},
                                  json={"body": {"content": reply_message},
                                        "to": [{"userId": sender_id}]})

                    # Mark the message as read
                    requests.patch(f"https://graph.microsoft.com/v1.0/me/chats/{chat_id}/messages/{message['id']}",
                                   headers={"Authorization": f"Bearer {access_token}"},
                                   json={"isRead": True})

        # Add a delay before the next iteration
        time.sleep(1)  # Adjust the delay as needed

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

    # Break the loop by pressing the 'q' key
    if input("Press 'q' to stop the script: ") == 'q':
        break
