# NameDDNS

Dynamic DNS script for [name.com](https://www.name.com) written in Python. It uses the [NameAPI](https://www.name.com/api) to update the IP address of a dns record.

## How to use

1. Get your API token from [nameAPI](https://www.name.com/account/settings/api).
2. Get a list of all records for your domain (change example.org to your domain):

    ```[bash]
    curl -u 'username:token' 'https://api.dev.name.com/v4/domains/example.org/records'
    ```

3. User the `recordparser.py` script to fill `config.json` or manually edit the file.

4. To automate the script add it to crontab or whatever you use to launch scripts every x period of time. (remember to run it from path where config.json is located)

    - If using cron:

        ```[bash]
        crontab -e
        ```

        Insert the following line (changing `path_to_script`) to run it every 2 hours:

        ```[bash]
        0 */2 * * * /usr/bin/python3 path_to_script/nameddns.py &>/dev/null
        ```

-------------------------------------------------------------------------------------------------------------------------------------------------
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=LZDKH4PL5Z3XN&source=url)
