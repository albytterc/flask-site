import requests

"""
Oauth steps
1. Request authorization from the user by sending a request to the authentication server
    * Send parameters including client id, redirect url, response type, owner, and state
2. Receive temporary code from above request to exchange for access token
"""

notion_url = "https://api.notion.com/v1/oauth/authorize"
# client_id =
# redirect_uri =