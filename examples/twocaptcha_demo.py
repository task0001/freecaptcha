import requests

import freecaptcha


def main() -> None:
    token = freecaptcha.solve(
        "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcyqq8oAAAAAJE7eVJ3aZp_hnJcI6LgGdYD8lge&co=aHR0cHM6Ly8yY2FwdGNoYS5jb206NDQz&hl=en&v=hbAq-YhJxOnlU-7cpgBoAJHb&size=invisible&cb=hbv3ebkuwbsy"
    )

    data = {"siteKey": "6Lcyqq8oAAAAAJE7eVJ3aZp_hnJcI6LgGdYD8lge", "answer": token}

    response = requests.post(
        "https://2captcha.com/api/v1/captcha-demo/recaptcha/verify", json=data
    )

    print(response.json())

    """ Output: 
    {'challenge_ts': '2025-04-05T16:56:44Z',
    'hostname': '2captcha.com',
    'score': 0.1,
    'success': True}
    """


if __name__ == "__main__":
    main()
