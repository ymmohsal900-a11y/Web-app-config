    @app.route("/login")
def login():
    session["flow"] = _build_msal_app().initiate_auth_code_flow(
        scopes=current_app.config["SCOPE"],
        redirect_uri=url_for("authorized", _external=True)
    )
    return redirect(session["flow"]["auth_uri"])
