import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN")
TEST_GUILD_ID = int(os.getenv("TEST_GUILD_ID"))
DEFAULT_SUMMARY_COUNT = int(os.getenv("DEFAULT_SUMMARY_MESSAGE_COUNT", "100"))
COMMAND_PREFIX: str = os.getenv("COMMAND_PREFIX", "!")
