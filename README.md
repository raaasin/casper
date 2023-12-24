# Casper - Frost Hacks Discord Bot

Casper is a Discord bot tailored specifically for the Frost Hacks server. Its primary functions are to warmly greet new users joining the server and to interact seamlessly with Google's Gemini API.

### Features:

#### Greeting Functionality:

Upon a new user joining the server, Casper welcomes them with a personalized message in the system channel, expressing excitement about their presence within the Frost Hacks community.

#### Interaction with Gemini API:

Casper utilizes Google's Gemini API, a robust family of multimodal large language models, to engage in conversations with server members. This functionality allows for seamless interaction with the bot through text messages.

### How Casper Works:

- **On Ready Event**: Casper notifies its online status upon successful connection to the Discord server.
- **On Member Join Event**: Welcomes new members to the server with a personalized greeting and an optional GIF.
- **On Message Event**: Listens for messages and interacts using Google's Gemini API. When a user sends a message, Casper processes it through the Gemini model and responds with conversational text.

### Setting Up Casper:

To set up Casper for your Discord server:

1. Clone this repository.
2. Install the necessary dependencies.
3. Replace the placeholder values for `token` and `key` in the `creds.py` file with your bot token and Gemini API key, respectively.
4. Ensure Casper has appropriate permissions within your Discord server.
5. Run the bot.

### Gemini API:

Google Gemini stands as the successor to LaMDA and PaLM 2, offering powerful multimodal language models. Casper leverages Gemini to engage in natural language conversations with users, providing an enriched interactive experience within the Discord server.
