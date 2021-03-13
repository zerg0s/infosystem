from localization import Locale


class TestReport:
    TEST = Locale.Test
    YOUR_RESULT = Locale.YourAnswer
    OTHER = "Other"
    __type = str()
    __description = str()

    def __init__(self, type: str, resultString: str):
        self.__type = type
        self.__description = resultString

    def getType(self):
        return self.__type

    def getDescription(self):
        return self.__description

    def setType(self, type: str) -> None:
        self.__type = type

    def setDescription(self, description: str) -> None:
        self.__description = description

    def __getitem__(self, key):
        return self.__type if key == 0 else self.__description

    def __setitem__(self, key, value):
        self.__type == value if key == 0 else self.__description == value
