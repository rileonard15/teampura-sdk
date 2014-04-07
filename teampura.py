import os
import urllib2
import json



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











