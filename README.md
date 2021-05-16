# hailey-python
Multi-purpose Discord moderation bot. Original version went defunct due to API changes, so this is a rewrite.

## Usage
The "official" bot instance is not public, so YOU have to run it. This is actually not as hard as it sounds.

### Prerequisites
- Python 3 with pip
- A computer on which you can run the bot 24/7 or whatever time frames you want (the latter would require either cronjob or manual effort, both of which are not covered here)
- Git (recommended) 

1. Install discord.py
  - This is as simple as a `pip install discord`.
2. Get a bot token
  - Go to https://discord.com/developers
  - Click "New application"
  - Name: whatever you want; recommended to be "Hailey the Snake"
  - Click "Bot", followed by "Add Bot" and then "Yes, do it!"
  - Add a good profile picture. Recommended to be the following: (insert photo here when the pfp is ready)
  - Scroll down and turn on "SERVER MEMBERS INTENT". Otherwise, the bot will not run without some code changes.
  - Click "OAuth2" on the sidebar
  - Enable the "bot" scope
  - Select "administrator" (or whatever perms you want for the bot) as the permissions.
  - Copy the link above the permissions box (should look something like https://discord.com/api/oauth2/authorize?client_id=000000000000000000&permissions=8&scope=bot)
  - Select "Bot" on the sidebar
  - Copy the access token. **DO NOT SHARE IT! It will allow anyone to pose as your instance of the bot, giving them large permissions on any server it's on.** If Discord sees it on the 'net, they'll automatically regenerate the token.
3. Download the bot
  - If you have Git (git-scm.com) installed, clone the repository. This will allow you to update the bot by simply pulling the repo, instead of having to redownload the files.
  - If you aren't using Git, download the bot's zip file. As of now it is https://github.com/TheTechRobo/hailey-python/archive/refs/heads/main.zip. Extract the ZIP.
4. Configure the bot
  - Create a file called "TOKEN.txt" inside the bot's folder. Inside of it, put ONLY (no preceding or trailing spaces, no "hi", no nothing) the bot token.
  - Go into "hailey_data" and modify the file "INFO.py" to your liking. It contains basic configuration for the bot.
