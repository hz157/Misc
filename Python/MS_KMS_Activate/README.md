# KMS Active Script

> run the script with administrator privileges

### Description
This script will activate the system using the KMS server.
 - Support for custom KMS servers
 - Open script source code
 - CMD Execution

#### Online
If you need to connect online, you need to establish a website that can provide JSON files and modify the networkStatus to **"online"**.
> The WEB site needs to provide two files, Key.json and Command.json, and modify the corresponding content in both files (KMS Server Addr)

#### Offline
If you choose to go offline, you need to modify the networkStatus to other content (e.g. offline)
> Need to modify the KMS SERVER in the else branch to KMS Server Addr
``` Python
def config():
    if networkStatus == "online":
        # Online Config
        global KEY_URL, COMMAND_URL, HEADERS
        KEY_URL = "Your Keys JSON URL" # You need Edit this Code
        COMMAND_URL = "Your Commands JSON URL"  # You need Edit this Code
        HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"}
        GetKey()
        GetCommand()
    else:
        # Offline Config
        global KMS_SERVER
        KMS_SERVER = ""  # You need Edit this Code
        ReadFile()
```

### About Key
[Key Management Services (KMS) client activation and product keys](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys)

### Usage
``` powershell
python kms_active.py
```

### Example
![example](https://raw.githubusercontent.com/hz157/Misc/main/Python/MS_KMS_Activate/example.gif)
