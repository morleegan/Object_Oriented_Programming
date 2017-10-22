import requests


class API:
    """Base class for all API calls
    """
    def __init__(self, *args, **kws):
        self.url = "http://localhost:8080/thalia"
        self.req_url = ""

        for opt in ['url']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def req_view(self, rid):
        """returns a single call through an id, example show with id = 99 is returned"""
        try:
            r = requests.get(self.url + self.req_url + "/" + str(rid))
            r.raise_for_status()
            return r.json()
        except requests.HTTPError:
            print("HTTP Error: key not found")
            return 404

    def req_view_all(self):
        """returns all of the selected class/var, example show, returns all shows"""
        try:
            r = requests.get(self.url + self.req_url)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError:
            print("HTTP Error: req_url not found")
            return 404

    def req_create(self, json_data):
        """not all APIs will create, POST api call"""
        # TODO: create a new key for each and return key
        try:
            r = requests.post(self.url + self.req_url, json=json_data)
            r.raise_for_status()
            return {"wid": 0}
        except requests.HTTPError:
            print("HTTPError: could not create")
            return 404

    def req_update(self, rid, json_data):
        """PUT api call, updates the values through what is given in json"""
        try:
            r = requests.put(self.url + self.req_url + '/' + str(rid), json=json_data)
            r.raise_for_status()
            return 200
        except requests.HTTPError:
            print("HTTPError: key not found")
            return 404

    def req_delete(self, rid):
        """Remove a '__' from the options"""
        try:
            r = requests.delete(self.url + self.req_url + '/' + str(rid))
            r.raise_for_status()
            return 200
        except requests.HTTPError:
            print("HTTPError: key not found")
            return 404
