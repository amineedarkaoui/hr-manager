import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

to_email = "samy82696@gmail.com"
smtp_server = 'smtp.gmail.com'
smtp_port = 465
login = 'amineed98@gmail.com'
password = 'hrvh bvcv eguv zhnc'

def sentiment_color(sentiment):
    return "green" if sentiment == "POSITIVE" else "red"

def send_feedback_email(user, answer1, answer2, answer3, sentiment1, sentiment2, sentiment3):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = user[6]
    msg['To'] = to_email
    msg['Subject'] = f"{user[1]} {user[2]} has sent a new feedback"

    # Attach the body with the msg instance
    body = f"""
        <html>
            <head></head>
            <body>
                <h1>{user[1]} {user[2]}'s feedback</h1>
                <div style="background-color: #f0f0f0; padding: 10px; margin-top: 20px;">
                    <h3>What do you think about the company's work environment?</h3>
                    <p>{answer1}</p>
                    <span style="color:{sentiment_color(sentiment1)};"><i>{sentiment1}</i></span>
                </div>

                </br>

                <div style="background-color: #f0f0f0; padding: 10px; margin-top: 20px;">
                    <h3>What do you think about your salary?</h3>
                    <p>{answer2}</p>
                    <span style="color:{sentiment_color(sentiment2)};"><i>{sentiment2}</i></span>
                </div>

                </br>

                <div style="background-color: #f0f0f0; padding: 10px; margin-top: 20px;">
                    <h3>What do you think about your managers?</h3>
                    <p>{answer3}</p>
                    <span style="color:{sentiment_color(sentiment3)};"><i>{sentiment3}</i></span>
                </div>

                <br>
                <br>

                <p>{user[1]} {user[2]}</p>
                <p>{user[6]}</p>
            </body>
        </html>
    """

    msg.attach(MIMEText(body, 'html'))

    # Create server object with SSL option
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)

    # Perform operations via server
    server.login(login, password)
    text = msg.as_string()
    server.sendmail(user[6], to_email, text)
    server.quit()