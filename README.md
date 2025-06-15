# Chat Summarization Bot

A Discord bot that provides on-demand summaries of recent conversations, helping users catch up quickly and identify key points.

---

## Key Features

* **On-Demand Summaries**: Invoke a command to summarize the last N messages in a channel.
* **Readable Output**: Summaries delivered as concise text.
* **Configurable Channels**: Administrators can enable or disable summarization per channel.
* **Privacy-Aware**: Only reads messages in allowed channels when requested; no data is stored long-term.

---

### How to Invite & Enable

1. **Invite the Bot**

   * Use the invite link provided by me.
   * Ensure it has permissions to read message history and send messages/attachments in the desired channels.

2. **Enable Summarization**

   * A server admin runs:

     ```txt
     /addchannel
     ```

   * To disable in a channel:

     ```txt
     /removechannel
     ```

   * To view enabled channels:

     ```txt
     /channels
     ```

---

### Basic Usage

* **Summarize Recent Messages**

  ```txt
  /summarize [N]
  ```

  * Summarizes the last N messages in the current channel.
  * If N is omitted, a default number (100) is used.
  * Example: `/summarize 50`.

* **Help & Information**

  ```txt
  /help
  ```

  * Shows a brief description of available commands and usage notes.

---

### Behavior & Output

* **Processing Notice**: After you issue `/summarize`, the bot will respond with “Processing…” and then edit that message with the summary when ready.

---

### Permissions & Privacy

* **Read History Only When Requested**: The bot only accesses past messages when a summary is explicitly requested in an enabled channel.
* **No Unintended Storage**: Message content isn’t stored long-term.
* **Opt-In Channels Only**: Summaries occur only in channels explicitly enabled by an admin.

---
