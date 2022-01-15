# NameDDNS

Dynamic DNS client for [name.com](https://www.name.com).

## How to use

- Get your API token from [name.com](https://www.name.com/account/settings/api).
- Get a list of all records for your domain (change example.org to your domain):

    ```[bash]
    curl -u 'username:token' 'https://api.dev.name.com/v4/domains/example.org/records'
    ```

- Edit the config.json file with the required info and run the script.

- To automate the script add it to crontab or whatever you use (remember to run it from path where config.json is located):

    ```[bash]
    crontab -e
    ```

    Insert the following line to run it every 3 hours:

    ```[bash]
    0 */3 * * * /usr/bin/python /path/to/script/nameddns.py
    ```
