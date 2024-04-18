import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import ssl
from env import PASSWORD

# Function to read log file and check for error patterns
def monitor_log_file(log_file_path, error_patterns):
    with open(log_file_path, 'r') as file:
        for line in file:
            for pattern in error_patterns:
                if re.search(pattern, line):
                    send_alert_email(pattern, line)

# Function to send alert email
def send_alert_email(error_pattern, log_line):
    # Email configuration
    sender_email = 'rish061321@gmail.com'
    receiver_email = 'rishipjn24@gmail.com'
    password = PASSWORD

    # Create message
    message = MIMEMultipart()
    print(message)
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Web Server Error Alert'

    # Body of the email
    body = f"Error pattern detected: {error_pattern}\nLog Line: {log_line}"
    message.attach(MIMEText(body, 'plain'))


    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        print("connected succesfully")
        server.login(sender_email, password="gfqmgzagkmlwmbkm")
        print("login success")
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Mail sent")

# Main function
def main():
    # Log file path
    log_file_path = '/var/log/apache2/error.log'

    # Error patterns to watch for
    error_patterns = [
        r'File does not exist',
        r'shutting down'
    ]

    # Monitor log file indefinitely
    while True:
        monitor_log_file(log_file_path, error_patterns)
        # Check log file every 60 seconds
        time.sleep(10)

if __name__ == "__main__":
    main()
