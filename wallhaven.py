import json
import requests
from typing import List, Dict, Optional
from errors import WallhavenAPIError


class WallhavenPY:
    """
    A client for interacting with the Wallhaven API.

    Attributes:
        api_key (Optional[str]): The API key for authentication (optional).
        ssl_verify (bool): Whether to verify SSL certificates (default: True).
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        ssl_verify: bool = True,
    ):
        """
        Initialize the WallhavenPY client.

        Args:
            api_key (Optional[str]): The API key for authentication.
            ssl_verify (bool): Whether to verify SSL certificates.
        """
        self.url = "https://wallhaven.cc/api/v1/{}"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            import urllib3

            # Disable SSL warnings if SSL verification is turned off
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def get(self, endpoint: str) -> Dict:
        """
        Fetch data from a specified endpoint.

        Args:
            endpoint (str): The API endpoint to query.

        Returns:
            Dict: The JSON response from the API.

        Raises:
            WallhavenAPIError: If an error occurs during the request or response processing.
        """
        full_url = self.url.format(endpoint)
        headers = {"X-API-KEY": self._api_key} if self._api_key else {}
        try:
            response = requests.get(
                url=full_url, verify=self._ssl_verify, headers=headers
            )
            response.raise_for_status()  # Raises HTTPError for bad responses
            data_out = response.json()
            return data_out
        except requests.exceptions.HTTPError as http_err:
            raise WallhavenAPIError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            raise WallhavenAPIError(f"Request error occurred: {req_err}")
        except ValueError as json_err:
            raise WallhavenAPIError(f"Error parsing JSON: {json_err}")

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
        """
        Search for wallpapers based on various parameters.

        Args:
            categories (Optional[str]): Categories to filter by.
            purity (Optional[str]): Purity filter for SFW, Sketchy, NSFW.
            sorting (Optional[str]): Sort wallpapers by criteria (e.g., 'relevance').
            order (Optional[str]): Order of results ('desc', 'asc').
            topRange (Optional[str]): Time range for top list (e.g., '1d', '1w').
            MinimumResolution (Optional[str]): Minimum resolution (e.g., '1920x1080').
            resolutions (Optional[List[str]]): List of desired resolutions.
            ratios (Optional[List[str]]): List of desired aspect ratios.
            colors (Optional[str]): Filter images by colors.
            page (Optional[int]): Page number for pagination.
            seed (Optional[str]): Seed value for randomization.

        Returns:
            Dict: The JSON response from the API.

        Raises:
            WallhavenAPIError: If an error occurs during the request or response processing.
        """
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
        try:
            response = requests.get(
                url=full_url,
                params={k: v for k, v in query_params.items() if v is not None},
                verify=self._ssl_verify,
                headers=headers,
            )
            response.raise_for_status()  # Raises HTTPError for bad responses
            data_out = response.json()
            return data_out
        except requests.exceptions.HTTPError as http_err:
            raise WallhavenAPIError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            raise WallhavenAPIError(f"Request error occurred: {req_err}")
        except ValueError as json_err:
            raise WallhavenAPIError(f"Error parsing JSON: {json_err}")

    def get_wallpaper(self, wallpaper_id: str) -> Dict:
        """
        Retrieve detailed information about a specific wallpaper by its ID.

        Args:
            wallpaper_id (str): The unique identifier of the wallpaper.

        Returns:
            Dict: The JSON response containing wallpaper details.

        Raises:
            WallhavenAPIError: If an error occurs during the request or response processing.
        """
        endpoint = f"w/{wallpaper_id}"
        return self.get(endpoint)

    def get_collections(self, username: str) -> Dict:
        """
        Retrieve the collections of a specific user.

        Args:
            username (str): The username of the user whose collections you want to fetch.

        Returns:
            Dict: The JSON response containing the user's collections.

        Raises:
            WallhavenAPIError: If an error occurs during the request or response processing.
        """
        endpoint = f"collections/{username}"
        return self.get(endpoint)

    def get_collection_wallpapers(
        self, username: str, collection_id: str, page: Optional[int] = None
    ) -> Dict:
        """
        Retrieve the wallpapers in a specific collection.

        Args:
            username (str): The username of the collection owner.
            collection_id (str): The ID of the collection.
            page (Optional[int]): The page number for pagination (default: 1).

        Returns:
            Dict: The JSON response containing wallpapers in the collection.

        Raises:
            WallhavenAPIError: If an error occurs during the request or response processing.
        """
        endpoint = f"collections/{username}/{collection_id}"
        if page:
            endpoint += f"?page={page}"
        return self.get(endpoint)

    def get_tag(self, tag_id: str) -> Dict:
        """
        Retrieve detailed information about a specific tag by its ID.

        Args:
            tag_id (str): The unique identifier of the tag.

        Returns:
            Dict: The JSON response containing tag details.

        Raises:
            WallhavenAPIError: If an error occurs during the request or response processing.
        """
        endpoint = f"tag/{tag_id}"
        return self.get(endpoint)

    def save_as_json(self, data: Dict, file_path: str) -> None:
        """
        Save the provided data as a JSON file.

        Args:
            data (Dict): The data to be saved as a JSON file.
            file_path (str): The path where the JSON file will be saved.

        Raises:
            WallhavenAPIError: If an error occurs while writing the file.
        """
        try:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Data successfully saved to {file_path}")
        except IOError as io_err:
            raise WallhavenAPIError(f"Error saving data to {
                                    file_path}: {io_err}")
