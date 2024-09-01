import requests
import requests.packages
from typing import List, Dict


class wallhavenPY:
    def __init__(
        self,
        hostname: str = "wallhaven.cc/api",
        api_key: str = "",
        ver: str = "v1",
        ssl_verify: bool = True,
    ):
        self.url = "https://{}/{}/".format(hostname, ver)
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()

    def get(self, endpoint: str) -> List[Dict]:
        full_url = self.url + endpoint
        headers = {"x-api-key": self._api_key}
        response = requests.get(url=full_url, verify=self._ssl_verify, headers=headers)
        data_out = response.json()
        print(full_url)
        if response.status_code >= 200 and response.status_code <= 299:  # OK
            return data_out
        # Todo: raise custom exception later
        raise Exception(data_out["message"])


client = wallhavenPY(api_key="RrikSnfd9HqmnoyIrsy1403Fld7ZtPeo")
list = client.get(endpoint="w/x6m79l")

another_list = list.get("data")

print(client.url)
print(another_list.get("url"))
