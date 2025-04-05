import requests

import freecaptcha


def main() -> None:
    token = freecaptcha.solve(
        "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfSlMopAAAAABC9hqcNILDbED4TCj1wYHMd9XvV&co=aHR0cHM6Ly93d3cuaHVkc29ucm9jay5jb206NDQz&hl=en&v=hbAq-YhJxOnlU-7cpgBoAJHb&size=invisible&cb=sgkp5zo2xmw"
    )

    params = {"email": "example@gmail.com", "token": token}

    response = requests.get(
        "https://cavalier.hudsonrock.com/api/json/v2/stats/website-results/email",
        params=params,
    )

    print(response.json())

    """ Output:
    {'computer_name': 'ANONYMOUSE (drhum)',
    'date_compromised': '2024-11-15T00:00:00.000Z',
    'message': 'This email address is associated with a computer that was '     
                'infected by an info-stealer, all the credentials saved on this '
                'computer are at risk of being accessed by cybercriminals.',     
    'total_corporate_services': 0,
    'total_user_services': 20}
    """


if __name__ == "__main__":
    main()
