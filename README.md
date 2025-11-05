# Grok Discord Bot

A Discord bot that integrates with xAI's Grok API to answer questions when mentioned in replies.

## Setup

1. Create a Discord bot at https://discord.com/developers/applications and get the token.
2. Get an xAI API key at https://x.ai/api-keys.
3. Copy `.env.example` to `.env` and fill in your tokens.
4. Install dependencies: `pip install -r requirements.txt`
5. Run the bot: `python main.py`

## Usage

Reply to any message and mention the bot (@GrokBot) with your question. The bot will respond with an answer from Grok.

Example:
- User A: "What's the capital of France?"
- User B: Reply to User A's message: "@GrokBot explain this"

The bot will query Grok and reply.