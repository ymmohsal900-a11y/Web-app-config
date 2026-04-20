@app.route(current_app.config["REDIRECT_PATH"])
def authorized():
    try:
        cache = msal.SerializableTokenCache()
        result = _build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            session.get("flow", {}),
            request.args
        )
        
        if "error" in result:
            current_app.logger.error("Invalid login attempt")
            return "Login failed"

        session["user"] = result.get("id_token_claims")
        current_app.logger.info("Login successful")

        return redirect(url_for("index"))

    except Exception as e:
        current_app.logger.error("Login exception: " + str(e))
        return "Error occurred"
