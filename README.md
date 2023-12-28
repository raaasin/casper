# Casper - Frost Hacks Discord Bot

Casper is a Discord bot tailored specifically for the Frost Hacks server. Its primary function is to warmly greet new users joining the server and create an engaging environment through welcoming messages.

## Features:

### Greeting Functionality:

Upon a new user joining the server, Casper welcomes them with a personalized message in the system channel, expressing excitement about their presence within the Frost Hacks community.

### How Casper Works:

- **On Ready Event**: Casper notifies its online status upon successful connection to the Discord server.
- **On Member Join Event**: Welcomes new members to the server with a randomly selected personalized greeting message from a predefined list.

## Setting Up Casper:

To set up Casper for your Discord server:

1. Clone this repository.
2. Install the necessary dependencies.
3. Replace the placeholder value for `token` in the `creds.py` file with your bot token.
4. Ensure Casper has appropriate permissions within your Discord server.
5. Run the bot.

## Customization:

Feel free to customize the list of welcome messages to suit your server's tone and community better. You can modify the messages within the `welcome_messages` list in the code.

## How to Run:

Run the bot by executing the Python script:

```bash
python bot.py
```

## Note:

Ensure your bot has the necessary intents enabled, especially `intents.members`, to correctly handle member join events.

## Credits:

Casper makes use of the Discord.py library to interact with Discord APIs.
