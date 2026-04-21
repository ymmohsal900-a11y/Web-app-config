import msal
from django.shortcuts import redirect, render
from django.conf import settings
from django.urls import reverse

def _build_msal_app(cache=None):
    return msal.ConfidentialClientApplication(
        settings.CLIENT_ID, 
        authority=settings.AUTHORITY,
        client_credential=settings.CLIENT_SECRET, 
        token_cache=cache
    )

def sign_in(request):
    # TODO: Initialize the MSAL confidential client
    client_app = _build_msal_app()
    
    # TODO: Generate the authorization URL
    auth_url = client_app.get_authorization_request_url(
        settings.SCOPE,
        redirect_uri=request.build_absolute_uri(reverse('callback'))
    )
    return redirect(auth_url)

def callback(request):
    # TODO: Acquire the token using the code returned by Microsoft
    client_app = _build_msal_app()
    
    # Get the code from the GET parameters
    code = request.GET.get('code')
    
    if code:
        result = client_app.acquire_token_by_authorization_code(
            code,
            scopes=settings.SCOPE,
            redirect_uri=request.build_absolute_uri(reverse('callback'))
        )
        
        if "error" in result:
            return render(request, "auth_error.html", {"error": result.get("error_description")})
            
        # TODO: Save user info to the session
        request.session["user"] = result.get("id_token_claims")
        
    return redirect("index") # Redirect to your home page
