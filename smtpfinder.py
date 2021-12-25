import os, re, time

searchwords = ["TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "$account_sid", "$auth_token", "$twilio_number", "Vonage\Client", "nexmo/laravel", "nexmo/client"]

def findaws(path, nicehost):
    if not ".git" in str(path):
        if not "smtpfinder.py" in str(path):
            with open(path, "r", errors="ignore", encoding='utf8') as file:
                lines = file.readlines()
                for line in lines:
                    awshost = re.findall("email-smtp[.][a-z0-9_-]{8,10}[.]amazonaws[.]com", line)
                    for host in awshost:
                        with open("results.txt", "a", encoding='utf8') as output:
                            output.write(path + " : " + str(host) + "\n")
                            print(f"[{nicehost}] SMTP found")

def findawscreds(path, nicehost):
    if not ".git" in str(path):
        if not "smtpfinder.py" in str(path):
            with open(path, "r", errors="ignore", encoding='utf8') as file:
                lines = file.readlines()
                for line in lines:
                    usernames = re.findall("AKIA[A-Z0-9]{16}", line)
                    for user in usernames:
                        with open("results.txt", "a", encoding='utf8') as output:
                            output.write(path + " : " + str(user) + "\n")
                            print(f"[{nicehost}] SMTP found")


def findother(path, nicehost):
    if not ".git" in str(path):
        if not "smtpfinder.py" in str(path):
            with open(path, "r", errors="ignore", encoding='utf8') as file:
                lines = file.readlines()
                for line in lines:
                    otherhost = re.findall("mail[.][a-z0-9\-]{4,15}[.][a-z.]{2,6}", line)
                    for host in otherhost:
                        if not "example" in host:
                            if not "gmail" in host:
                                if not "google" in host:
                                    if not "mail.com" in host:
                                        if not "settings" in host:
                                            if not "mail.html" in host:
                                                if not "template" in host:
                                                    if not "addons" in host:
                                                        with open("results.txt", "a", encoding='utf8') as output:
                                                            output.write(path + " : " + str(host) + "\n")
                                                            print(f"[{nicehost}] SMTP found")

def findknow(path, nicehost):
    if not ".git" in str(path):
        if not "smtpfinder.py" in str(path):
            with open(path, "r", errors="ignore", encoding='utf8') as file:
                lines = file.readlines()
                for line in lines:
                    knowsmtp = re.findall("smtp\.sendgrid\.net|smtp\.mailgun\.org|smtp-relay\.sendinblue\.com|email-smtp\.(us|eu|ap|ca|cn|sa)-(central|(north|south)?(west|east)?)-[0-9]{1}\.amazonaws.com|smtp.tipimail.com|smtp.sparkpostmail.com|nexmo_key|nexmo_secret|smtp.deliverabilitymanager.net|smtp.mailendo.com|mail.smtpeter.com|mail.smtp2go.com|smtp.socketlabs.com|secure.emailsrvr.com|mail.infomaniak.com|smtp.pepipost.com|smtp.elasticemail.com|smtp25.elasticemail.com|pro.turbo-smtp.com|smtp-pulse.com|in-v3.mailjet.com", str(line))
                    for smtps in knowsmtp:
                        with open("results.txt", "a", encoding='utf8') as output:
                            output.write(path + " : " + str(smtps) + "\n")
                            print(f"[{nicehost}] SMTP found")

def findsms(path, nicehost):
    if not ".git" in str(path):
        if not "smtpfinder.py" in str(path):
            with open(path, "r", errors="ignore", encoding='utf8') as file:
                lines = file.readlines()
                for line in lines:
                    for word in searchwords:
                        if word in str(line):
                            with open("results.txt", "a", encoding='utf8') as output:
                                output.write(path + " : " + str(word) + "\n")
                                print(f"[{nicehost}] SMS found")

def finder(root, nicehost):
    for root, dirs, files in os.walk(root):
        for f in files:
            path = os.path.join(root, f).replace("\\", "/")
            if not ".git" in str(path):
                if not "zip" in str(path) and not "rar" in str(path) and not "png" in str(path) and not "jpg" in str(path) and not "pdf" in str(path):
                    #findaws(path, nicehost)
                    #findother(path, nicehost)
                    findknow(path, nicehost)
                    findawscreds(path, nicehost)
                    findsms(path, nicehost)
