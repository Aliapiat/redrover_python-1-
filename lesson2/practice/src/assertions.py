from http import HTTPStatus

from requests import Response


class Assertions:

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        actual_status_code = response.status_code
        assert actual_status_code == HTTPStatus.OK, f"Unexpected status code: {expected_status_code}, but got {actual_status_code}"

    @staticmethod
    def assert_last_first_name(lst, lst1):
        assert lst == lst1, f"Unexpected full name: {lst1}, but got {lst}"



assertions = Assertions()