# NameDDNS

Dynamic DNS client for [name.com](https://www.name.com).

## How to use

1. Get your API token from [name.com](https://www.name.com/account/settings/api).
2. Get a list of all records for your domain (change example.org to your domain):

    ```[bash]
    curl -u 'username:token' 'https://api.dev.name.com/v4/domains/example.org/records'
    ```

3. Edit the `config.json` file with the required info and run the script.

4. To automate the script add it to crontab or whatever you use to launch scripts every x period of time. (remember to run it from path where config.json is located)

    - If using cron:

        ```[bash]
        crontab -e
        ```

        Insert the following line (changing `path_to_script`) to run it every 2 hours:

        ```[bash]
        0 */2 * * * /usr/bin/python3 path_to_script/nameddns.py &>/dev/null
        ```
