import requests

import freecaptcha


def main() -> None:
    token = freecaptcha.solve(
        "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LcVYwIqAAAAAL0eGyLRnmbBmqUmjix5uAeRIrle&co=aHR0cHM6Ly9uZXh0Y2FwdGNoYS5jb206NDQz&hl=en&v=hbAq-YhJxOnlU-7cpgBoAJHb&size=invisible&cb=yae8qzyvlosc"
    )

    data = {
        "siteKey": "6LcVYwIqAAAAAL0eGyLRnmbBmqUmjix5uAeRIrle",
        "gRecaptchaResponse": token,
    }

    response = requests.post(
        "https://next.nextcaptcha.com/api/captcha-demo/recaptcha_v2/verify", json=data
    )

    print(response.json())

    """ Output:
    {'challenge_ts': '2025-04-05T17:05:20Z',
    'hostname': 'nextcaptcha.com',
    'score': 0,
    'success': True}
    """


if __name__ == "__main__":
    main()
