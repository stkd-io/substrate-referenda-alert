from email import message
from substrateinterface import SubstrateInterface
import os
from slack_sdk import WebClient

ACCOUNT = os.environ['ACCOUNT']
WSS_URL = os.environ['WSS_URL']
SLACK_CHANNEL_NAME = os.environ['SLACK_CHANNEL_NAME']
SLACK_API = os.environ['SLACK_API']

def send_slack_message(api, channel_name, message):
    client = WebClient(api)
    response = client.chat_postMessage(
        channel=channel_name,
        text=message)

def lastRefVoted(account):
    votes = substrate.query(
        module='Democracy',
        storage_function="VotingOf",
        params=[account]
    )
    votes_descaled = votes.decode()
    if "Direct" in votes_descaled:
        dir_votes = votes_descaled['Direct']
        total_votes = dir_votes['votes']
        latest_vote = total_votes[len(total_votes)-1]
        return latest_vote[0]
    #runs if the wallet is Delegating democracy votes
    if "Delegating" in votes_descaled:
        get_address = votes_descaled['Delegating']
        delegated_address = get_address['target']
        ACCOUNT = delegated_address
        votes = substrate.query(
            module='Democracy',
            storage_function="VotingOf",
            params=[ACCOUNT]
        )
        votes_descaled = votes.decode()
        dir_votes = votes_descaled['Direct']
        total_votes = dir_votes['votes']
        latest_vote = total_votes[len(total_votes)-1]
        return latest_vote[0]
    else:
        print("Something went horribly wrong! Or you haven't voted or delegated")


substrate = SubstrateInterface(
    url=WSS_URL
)

#Starting number of pending referendum
lowestUnbaked = substrate.query(
    module='Democracy',
    storage_function='LowestUnbaked',
)

index = int(str(lowestUnbaked).encode("utf-8").decode("utf-8"))
last_vote = lastRefVoted(ACCOUNT)
print("lastest vote was for a Referendum was: " + str(last_vote) )
ref = " "

while ref != None:
    ref = substrate.query(
        module='Democracy',
        storage_function="ReferendumInfoOf",
        params=[index]
    )
    if ref != None:
        if index > last_vote:
            message = "New Referenda: " + str(index)
            print(message)
            send_slack_message(SLACK_API, SLACK_CHANNEL_NAME, message)
        index+=1
#remove the last increment from the loop        
print("Lastest Referendum is: " + str(index-1) )