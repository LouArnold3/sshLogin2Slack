mport urllib3
import json
from datetime import datetime
import time
import getpass
import socket

http = urllib3.PoolManager()
slack_wh = (
    "<SlackWebhook>"
)


time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = getpass.getuser()
action = "SUCCESSFUL SSH AUTHENTICATION"
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

msg = {
    "TIME": time,
    "USER": user,
    "HOSTNAME": hostname,
    "IP_ADDRESS": IPAddr,
    "ACTION": action,
}

time2 = str(msg["TIME"])
user2 = str(msg["USER"])
hostname2 = str(msg["HOSTNAME"])
ip_addr2 = str(msg["IP_ADDRESS"])
action2 = str(msg["ACTION"])

slack_msg = (
    f"TIME : {time2}"
    + f"\nUSER : {user2}"
    + f"\nHOSTNAME : {hostname2}"
    + f"\nIPADDRESS : {ip_addr2}"
    + f"\nACTION: {action2}"
)
slack = {"channel": "#shield-testing", "text": slack_msg}
encoded_msg = json.dumps(slack).encode("utf-8")
resp = http.request("POST", slack_wh, body=encoded_msg)
status = resp.status
data = resp.data
print(status, data)
print(slack_msg)
