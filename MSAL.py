CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

AUTHORITY = "https://login.microsoftonline.com/common"
REDIRECT_PATH = "/getAToken"
SCOPE = ["User.Read"]
