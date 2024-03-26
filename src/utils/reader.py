from typing import Any
import xmltodict


class XmlReader:
    _dict: dict[str, Any]

    def __init__(self, str) -> None:
        self._dict = xmltodict.parse(str, process_comments=True)

    def get_header(self) -> dict[str, Any]:
        return self._dict["ACES"]["Header"]

    def get_apps(self) -> dict[str, Any]:
        apps = self._dict["ACES"]["App"]
        if type(apps) == dict:
            apps = [apps]
        return apps

    def get_digital_file_informations(self) -> dict[str, Any]:
        digital_file_informations = self._dict["ACES"]["DigitalAsset"][
            "DigitalFileInformation"
        ]
        if type(digital_file_informations) == dict:
            digital_file_informations = [digital_file_informations]
        return digital_file_informations
