from django.shortcuts import render
import requests
import json

def home( request ):
	api_request = requests.get( "https://api.github.com/users?since=0", verify=False )
	api_content = json.loads( api_request.content )
	return render( request, "home.html", { "api_content": api_content } )

def user( request ):
	user = request.POST.get( "user" )
	user_request = requests.get( "https://api.github.com/users/" + user, verify=False )
	user_info = json.loads( user_request.content )
	return render( request, "user.html", { "user": user, "user_info": user_info } )
