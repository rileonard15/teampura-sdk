import os
import urllib2
import urllib
import json


API_KEY = ""
SECRET_KEY = ""

class Oauth():
    # Create teampura login url
    @classmethod
    def login_url_generator(self, redirect_uri, scope=""):
        # sample scope < user,project,items >
        # sample redirect_uri http://www.myapp.com/login

        url = "http://teampura.com/dialog/oauth?"
        url += "api_key=" + API_KEY
        url += "&redirect_uri=" + str(urllib.quote(redirect_uri, ''))
        url += "&scope=" + scope

        return url

    # Generate access token using the code given
    @classmethod
    def generate_access_token(self, code):
        url = "http://teampura.com/accesstoken?"
        url += "api_key=" + API_KEY + "&"
        url += "secret_key=" + SECRET_KEY + "&"
        url += "code=" + code.replace(" ", "+") # replace space to "+" for url handling

        response = urllib2.urlopen(url)
        api_response = json.loads(response.read())

        return api_response # this response contains json data

class Teampura():
    # Add team name and token
    def __init__(self, team=None, token=None):
        self.url = "teampura.com/"
        self.api_version = "api/v3/"
        if team:
            self.team = team
        else:
            self.team = "default_team"

        self.token = token

    # Create api url
    def api_url(self, kind, filters={}, category=""):
        url = "http://" + self.team + "." + self.url + self.api_version + kind

        if category:
            url += "/" + category

        url += "?access_token=" + self.token

        fs = ""
        if filters:
            for name, value in filters.items():
                fs += "&" + name + "=" + str(value).upper()
            url += fs

        return url

    # Fetch something in teampura
    def fetch(self, kind, filters={}, category=""):
        url = self.api_url(kind, filters=filters, category=category)

        response = urllib2.urlopen(url)
        api_response = json.loads(response.read())

        return api_response

    # Add or update something in teampura
    def create_data(self, kind, data={}, category=""):
        url = self.api_url(kind, category=category)

        data = json.dumps(data)
        req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
        response = urllib2.urlopen(req)
        api_response = json.loads(response.read())
        response.close()

        return api_response



""" SAMPLE USAGE """


# from teampura import Oauth
# from teampura import Teampura

""" generate teampura code """

# Oauth.login_url_generator("http://myapp.com/login", "user,items,projects,notes")

""" generate accesstoken """
# code = "< the code given by the teampura app >"
# response = Oauth.generate_access_token(code)


""" FETCH items """
# pura = Teampura("< team_name >", response["token"])
# kind = "items"
# data = {"filter_status": "DONE"}
# pura.fetch(kind, filters=data)

""" Update item """
# kind = "items"
# update_data = {"status": "DONE"}
# item_id = "5665117697998848"
# pura.create_data(kind, data=update_data, category=item_id)

""" add item """
# kind = "items"
# new_data = {"title": "item title", "content": "item content"}
# pura.create_data(kind, data=new_data)













