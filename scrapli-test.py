from scrapli.driver.core import IOSXEDriver

my_device = {
    "host": "10.10.10.1",
    "auth_username": "cisco",
    "auth_password": "cisco123",
    "auth_strict_key": False
}

conn = IOSXEDriver(**my_device)
conn.open()
response = conn.send_command("show run")
print(response.result)