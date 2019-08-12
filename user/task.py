from django.core.mail import EmailMessage
import time

from celery import Celery
app = Celery('user',broker='redis://localhost:6379')


@app.task
def send_email(to_email,message):
    time1 = 1
    while(time1 != 5):
        print("Sending Email ",time1)
        email = EmailMessage('Checking Asynchronous Task', message+" : "+str(time1), to=[to_email])
        email.send()
        time.sleep(1)
        time1 += 1