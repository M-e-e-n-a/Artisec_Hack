from flask import Flask
import datetime

app = Flask(__name__)


def exp_note(generation_time):
    gt=generation_time
    current_time=datetime.datetime.now()
    prompt_datetime= gt + datetime.timedelta(seconds=3)
    expiry_datetime=gt+datetime.timedelta(seconds=6)

    if prompt_datetime<current_time:
        prompt = f"Coupon expires soon on {expiry_datetime}"
    else:
        prompt = "its working"

    return prompt


@app.route('/')
def index():
    ct=datetime.datetime.now()
    return exp_note(ct)


if __name__ == '__main__':
    app.run()