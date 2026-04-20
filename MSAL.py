import msal
def _build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        current_app.config["CLIENT_ID"],
        authority=authority or current_app.config["AUTHORITY"],
        client_credential=current_app.config["CLIENT_SECRET"],
        token_cache=cache,
    )
