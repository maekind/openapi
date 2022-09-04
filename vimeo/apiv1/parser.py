""" Contains classes and methods for retreiving video information """
import requests
import json

class NotValidResponseException(BaseException):
    """ NotValidResponseException custom exception """


class Parser():
    """ Class that gets the video information from vimeo baes url """
    VIMEO_URL = r"https://vimeo.com/"
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
        """ Method to fetch video info

            Exception: NotValidResponseException is raised is status code is different than 200.
        """
        request = requests.get(self._base_url)

        if request.status_code == 200:
            print(
                f"Video id {self._video_id} information fetched successfully!")
            
            try:
                # Try to find json url
                json_url = self._get_json_url(str(request.content))
                # Pase json data and retrieve video information
                return self._parse_json_url(json_url)
            except Exception as ex:
                raise ex
        else:
            raise NotValidResponseException(request.status_code)

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

        except:
            raise NotValidResponseException("Unable to get the json url!")

    def _parse_json_url(self, url: str) -> str:
        """ Method for retreiving video's json data 
            Json data can be available in the "json_data" class property.

            Exception: NotValidResponseException is raised is status code is different than 200.
        """
        request = requests.get(url)

        if request.status_code == 200:
            return json.loads(request.content)
        else:
            raise NotValidResponseException(request.status_code)
