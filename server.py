from flask import Flask, request, make_response, Response
import json
import os
from slackclient import SlackClient
from slashCommand import *

slack_client = SlackClient(os.environ['SLACK_BOT_TOKEN'])
app = Flask(__name__)

commander = Slash("Hey there! It works.")

#TODO: Add checks for all responses from slack api calls

@app.route("/slack/ask", methods=["POST"])
def command():
  info = request.form

  print(request)

  # # get uid of the user
  # im_id = slack_client.api_call(
  #   "im.open",
  #   user=info["user_id"]
  # )["channel"]["id"]

  # # send user a response via DM
  # ownerMsg = slack_client.api_call(
  #   "chat.postMessage",
  #   channel=im_id,
  #   text=commander.getMessage()

  # send channel a response
  channelMsg = slack_client.api_call(
    "chat.postMessage",
    channel="#" + info["channel_name"],
    text="Hey there! It works. Your question was: '" + request.form.get('text', "...wait, you didn't ask a question!") + "'"
  )

  return make_response("", 200)

# Start the Flask server
if __name__ == "__main__":
  app.run()
