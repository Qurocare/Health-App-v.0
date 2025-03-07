from flask import Flask, request, jsonify
from score_calculator import calculate_health_score
import smtplib

app = Flask(__name__)

# Admin's email
admin_email = "reshma.qurocare@gmail.com"

# Function to send an email notification
def send_email(subject, body):
    try:
        # Connect to the Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login using your Gmail credentials
        server.login("rshm.jp07@gmail.com", "buhh ohfa ejzl bbcm")  # Use your email and app password here
        # Create the email message
        message = f"Subject: {subject}\n\n{body}"
        # Send the email to the admin
        server.sendmail("rshm.jp07@gmail.com", admin_email, message)
        server.quit()
        print("Critical alert email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/')
def home():
    return 'Welcome to the Health Score App'

@app.route('/calculate_score', methods=['POST'])
def calculate_score():
    # Get data from the POST request
    data = request.json

    # Calculate the health score and alerts
    score_data, alerts = calculate_health_score(data)

    # Check if there are any critical alerts
    critical_alerts = [alert for alert in alerts if "critical" in alert.lower()]

    if critical_alerts:
        # If there are critical alerts, send an email notification to the admin
        subject = "Critical Alert from Health Score App"
        body = (
            f"A critical alert was detected during health score calculation.\n\n"
            f"Details:\nTotal Score: {score_data['total_score']}\n"
            f"Breakdown: {score_data['breakdown']}\n"
            f"Critical Alerts: {', '.join(critical_alerts)}"
        )
        send_email(subject, body)

    # Return the calculated health score, breakdown, and alerts to the user
    return jsonify({
        'total_score': score_data['total_score'],
        'breakdown': score_data['breakdown'],
        'alerts': alerts
    })

if __name__ == '__main__':
    app.run(debug=True)
