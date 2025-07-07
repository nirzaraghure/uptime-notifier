import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# 👇 Replace this with your website or backend URL
url = "https://antiq-frontend.onrender.com"  

# 👇 Enter your Gmail and app password
sender_email = "nehaghure5@gmail.com"  
receiver_email = "nirzaraghure5@gmail.com"
email_password = "rmgi csuf rbgv badg"  # Use Gmail App Password 

def send_alert(message):
    subject = "🔴 ALERT: Website Down"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, email_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("✅ Alert sent!")
    except Exception as e:
        print("❌ Failed to send email:", e)

def check_website():
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            send_alert(f"❌ Site returned status {response.status_code} at {datetime.now()}")
        else:
            print(f"[{datetime.now()}] ✅ Site is up. Status: {response.status_code}")
    except requests.RequestException as e:
        send_alert(f"❌ Website is DOWN! Error: {e} – Time: {datetime.now()}")

if __name__ == "__main__":
    check_website()
