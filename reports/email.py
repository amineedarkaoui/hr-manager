import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown

to_email = "amine.edarkaoui03@gmail.com"
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
                <p><b>Employee:</b> {user[1]} {user[2]}</p>
                <p><b>Email:</b> {user[6]}</p>
                <h3>What do you think about the company's work environment?</h3>
                <p><b>Feedback 1:</b> {answer1}</p>
                <span style="color:{sentiment_color(sentiment1)};"><i>{sentiment1}</i></span>
                </br>
                <h3>What do you think about your salary?</h3>
                <p><b>Feedback 2:</b> {answer2}</p>
                <span style="color:{sentiment_color(sentiment2)};"><i>{sentiment2}</i></span>
                </br>
                <h3>What do you think about your managers?</h3>
                <p><b>Feedback 3:</b> {answer3}</p>
                <span style="color:{sentiment_color(sentiment3)};"><i>{sentiment3}</i></span>
            </body>
        </html>
    """

    msg.attach(MIMEText(markdown.markdown(body), 'html'))
    msg.attach(MIMEText(body, 'plain'))

    # Create server object with SSL option
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)

    # Perform operations via server
    server.login(login, password)
    text = msg.as_string()
    server.sendmail(user[6], to_email, text)
    server.quit()