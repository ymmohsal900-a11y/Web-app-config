@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        current_app.config["AUTHORITY"] + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True)
    )
