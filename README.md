# OMDb-Discord-Bot

Discord bot for retrieving movie/series information from the Open Movie Databse (OMDb). Search by title or IMDb ID (e.g. tt0133093).

The bot provides the following information (if available):

- Title and link to the IMDb entry
- Poster / Image
- Description
- Rating
- Runtime
- Genre
- Year(s)

## Prerequisites

- A [Discord](https://discord.com/) account, privilege to invite the bot to a server (e.g. your Discord server).

- [Python](https://www.python.org/) installed.

## Instructions

1. Clone the repo.

   ```terminal
   $ git clone https://github.com/jet76/OMDb-Discord-Bot.git
   ```

2. Install the requirements.

   ```terminal
   $ pip install -r requirements.txt
   ```

3. Visit [OMDb API](https://www.omdbapi.com/) and request an [API key](https://www.omdbapi.com/apikey.aspx). After you receive your OMDb API Key, copy-paste it into `.env` and save the file.

4. Proceed to the [Discord Developer Portal](https://discord.com/developers/) and create a new [Application](https://discord.com/developers/applications).

   - In the application's settings, click 'Bot' then 'Add Bot' to create a bot user.

   - Locate the 'Build-A-Bot' section and click the 'COPY' button underneath 'TOKEN' then paste the bot token into `.env` and save the file.

   - In the aplication's settings, click 'OAuth2, then under 'Scopes' check the box for 'bot' and click the 'Copy' button to copy the authorization url.

   - Open your web browser, proceed to the authorization url, and authorize the bot. The bot should now show as a (offline) member of the server.

5. Run the bot.

   ```terminal
   $ python3 ombd_bot
   ```

   The console should display

   ```terminal
   Logged in as
   YOUR BOT NAME
   YOUR BOT ID
   ```

   The bot should also appear as online in the Discord server.

6. Use the `!omdb` command to search for movies/series by title e.g. `!omdb The Matrix` or IMDb ID e.g. `!omdb tt0133093`.
