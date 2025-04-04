import json
import re
from urllib.parse import urlencode
from urllib.request import urlopen

from yarl import URL

__all__ = ("reCAPTCHAV3Solver",)


class reCAPTCHAV3Solver:
    @staticmethod
    def solve(anchor_url: str) -> str:
        """Solves a reCAPTCHA V3 challenge and returns the token.

        Args:
            anchor_url (str): The anchor url, can be found in DevTools by searching "anchor" and copying the URL.

        Raises:
            ValueError: Something went wrong when parsing responses from reCAPTCHA API.
        Returns:
            str: The solved captcha token.
        """
        with urlopen(anchor_url) as anchor_request:
            anchor_response = anchor_request.read().decode()

        recap_token = re.search(
            r'id="recaptcha-token"\s*value="(.*?)"', anchor_response
        )

        if not recap_token:
            raise ValueError("Unable to parse token from anchor response")

        parsed_url = URL(anchor_url, encoded=True)
        anchor_data = parsed_url.query

        site_key = anchor_data.get("k")

        data = {
            **anchor_data,
            "reason": "q",
            "c": recap_token.group(1),
            "chr": "",
            "vh": "",
            "bg": "",
        }

        with urlopen(
            f"https://www.google.com/recaptcha/api2/reload?k={site_key}",
            data=urlencode(data).encode("utf-8"),
        ) as reload_request:
            reload_response = reload_request.read().decode("utf-8")

        try:
            reload_data = json.loads(reload_response[5:])
            token = reload_data[1]
        except (json.decoder.JSONDecodeError, IndexError):
            raise ValueError("Unable to parse token from reload response")

        return token