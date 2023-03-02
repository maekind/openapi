""" Contains classes and methods for retreiving video information """
import json
import requests


class NotValidResponseException(BaseException):
    """ NotValidResponseException custom exception """


class Parser():
    """ Class that gets the video information from vimeo baes url """
    VIMEO_URL = r"https://vimeo.com/"
    TIMEOUT = 5  # seconds
    # BEGIN_TITLE_KEY = '<meta property="og:title" content="'
    # END_TITLE_KEY = '">'
    # BEGIN_IMAGE_KEY = '<meta property="og:image" content="'
    # END_IMAGE_KEY = '">'
    # BEGIN_DESCRIPTION_KEY = '<meta property="og:description" content="'
    # END_DESCRIPTION_KEY = '">'

    # AFTER AUGUST 2017
    KEY = "config_url"
    SUBKEY = "https"

    def __init__(self, video_id: str) -> None:
        """ Default constructor
            @param video_id: The video id retreived from the video url at vimeo
        """
        self._video_id = video_id
        self._base_url = f'{self.VIMEO_URL}{video_id}'

    def fetch_data(self):
        """ Method to fetch video info.
            The method assumes that a valid video id has been initialized.
            ---
            Exception: NotValidResponseException is raised if status code is different than 200
            or response content is not a valid json data.
            ---
            Return: json data object.
        """
        try:
            response = requests.get(self._base_url, timeout=self.TIMEOUT)

            response.raise_for_status()

            print(
                f"Video id {self._video_id} information fetched successfully!")

            # Try to find json url
            json_url = self._get_json_url(str(response.content))
            # Pase json data and retrieve video information
            return self._parse_json_url(json_url)

        except requests.exceptions.Timeout as error:
            raise NotValidResponseException('Timeout') from error
        except Exception as ex:
            raise ex

    def _get_json_url(self, webpage_data: str) -> str:
        """ Method for getting the video's json url

            Exception: NotValidResponseException is raised is status code is different than 200.
        """
        try:
            temp_data = webpage_data[webpage_data.index(self.KEY):]
            temp_data = temp_data[temp_data.index(self.SUBKEY):]
            json_url = temp_data[:temp_data.index('"')]
            # print(json_url)
            return json_url.replace('\\', '')

        except Exception as error:
            raise NotValidResponseException("Unable to get the json url!") from error

    def _parse_json_url(self, url: str) -> str:
        """ Method for retreiving video's json data 
            Json data can be available in the "json_data" class property.

            Exception: NotValidResponseException is raised is status code is different than 200.
        """
        response = requests.get(url, timeout=self.TIMEOUT)

        response.raise_for_status()

        return json.loads(response.content)
