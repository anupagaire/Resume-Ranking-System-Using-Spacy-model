import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_top5(to_list):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "resumeranker77@gmail.com"
    password = "wxjg wpfa eqnr eprt"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo() 
        server.starttls(context=context)
        server.ehlo() 
        server.login(sender_email, password)
        for to in to_list:
            message = MIMEMultipart()
            message["Subject"] = "Congratulations on Your High Ranking in Our Recruitment Process"
            message["From"] = sender_email
            message["To"] = to

            body = """\

Dear Sir/Madam,
<br>
We are pleased to inform you that your application has been highly ranked among the candidates we've reviewed. Your qualifications and experience align exceptionally well with our requirements, and we would like to express our appreciation for your interest in our organization.
<br>
As part of the next steps, we will continue reviewing the top-ranked candidates and will reach out to you within the next week to schedule an interview. We recommend that you regularly check both your inbox and spam folder to ensure you don’t miss any communication from us.
<br>
Thank you once again for your application and for your interest in joining our team. We look forward to learning more about your qualifications in the coming stages of the process.\n\n
Sincerely,
<br>
HR team<br>
Resume Ranking and Recommendation Team
            """
            message.attach(MIMEText(body, "html"))

            try:
                server.sendmail(sender_email, to, message.as_string())
                print("Email sent to", to)
            except Exception as e:
                print(f"Error sending email to {to}: {e}")
        print("All emails sent.")

    return "Emails are sent to top5"
