from datetime import datetime
from dateutil.relativedelta import relativedelta

from flask import render_template
from datetime import date
from webapp import app

@app.route('/')
@app.route('/index')
def index():
    wedding = '2019-06-01 14:00:00'

    wedding_date = datetime.strptime(wedding, '%Y-%m-%d %H:%M:%S')

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date_now = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')

    diff = relativedelta(wedding_date, date_now)
    if diff.months == 1:
        m = 'month'
    else:
        m = 'months'

    if diff.days == 1:
        d = 'day'
    else:
        d = 'days'

    if diff.hours == 1:
        h = 'hour'
    else:
        h = 'hours'

    if diff.minutes == 1:
        mi = 'minute'
    else:
        mi = 'minutes'

    if diff.seconds == 1:
        s = 'second'
    else:
        s = 'seconds'

    print(diff)
    return render_template('index.html', title='Home', months = diff.months, m = m, days = diff.days, d = d, hours = diff.hours, h = h, minutes = diff.minutes, mi = mi, seconds = diff.seconds, s = s)
