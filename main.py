import requests
from typing import List, Dict, Optional
from errors import WallhavenAPIError  # Import the custom exception


class WallhavenPY:
    def __init__(
        self,
        api_key: Optional[str] = None,
        ssl_verify: bool = True,
    ):
        self.url = "https://wallhaven.cc/api/v1/{}"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            import urllib3

            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def get(self, endpoint: str) -> Dict:
        full_url = self.url.format(endpoint)
        headers = {"X-API-KEY": self._api_key} if self._api_key else {}
        response = requests.get(url=full_url, verify=self._ssl_verify, headers=headers)
        data_out = response.json()
        if response.status_code >= 200 and response.status_code <= 299:  # OK
            return data_out
        # Raise custom exception
        raise WallhavenAPIError(data_out.get("message", "Unknown error"))

    def search(
        self,
        categories: Optional[str] = None,
        purity: Optional[str] = None,
        sorting: Optional[str] = None,
        order: Optional[str] = None,
        topRange: Optional[str] = None,
        MinimumResolution: Optional[str] = None,
        resolutions: Optional[List[str]] = None,
        ratios: Optional[List[str]] = None,
        colors: Optional[str] = None,
        page: Optional[int] = None,
        seed: Optional[str] = None,
    ) -> Dict:
        query_params = {
            "categories": categories,
            "purity": purity,
            "sorting": sorting,
            "order": order,
            "topRange": topRange,
            "MinimumResolution": MinimumResolution,
            "resolutions": ",".join(resolutions) if resolutions else None,
            "ratios": ",".join(ratios) if ratios else None,
            "colors": colors,
            "page": page,
            "seed": seed,
        }
        full_url = self.url.format("search")
        headers = {"X-API-KEY": self._api_key} if self._api_key else {}
        response = requests.get(
            url=full_url,
            params={k: v for k, v in query_params.items() if v is not None},
            verify=self._ssl_verify,
            headers=headers,
        )
        data_out = response.json()
        if response.status_code >= 200 and response.status_code <= 299:  # OK
            return data_out
        # Raise custom exception
        raise WallhavenAPIError(data_out.get("message", "Unknown error"))


# Example usage
client = WallhavenPY(api_key="RrikSnfd9HqmnoyIrsy1403Fld7ZtPeo")
try:
    collection_data = client.get(endpoint="collections")
    print(collection_data)

    search_results = client.search(
        categories="111", purity="100", sorting="random", order="desc", page=1
    )
    print(search_results)
except WallhavenAPIError as e:
    print(f"An error occurred: {e}")
