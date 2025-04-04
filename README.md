
# freecaptcha

A simple and free reCAPTCHA V3 bypass.

### Disclaimer!

freecaptcha **only works on reCAPTCHA V3**!

## Installation

Install freecaptcha from PyPI

```bash
pip install freecaptcha
```

## Usage/Examples

```python
from freecaptcha import reCAPTCHAV3Solver

token = reCAPTCHAV3Solver.solve("ANCHOR URL FOR YOUR SITE")

# Use token within your HTTP request
```


## How To Find Anchor URL

1. Navigate to your target website in your browser.
2. Open Developer Tools (CTRL + I).
3. Navigate to the 'Network' tab.
4. Perform the captcha.
5. Search for the 'anchor' request.
6. Copy the request URL.

## Authors

- [@task0001](https://www.github.com/task0001)

