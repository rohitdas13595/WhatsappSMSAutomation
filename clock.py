from datetime import datetime
from msg import send_notice


from apscheduler.schedulers.blocking import BlockingScheduler




sched = BlockingScheduler()

# Schedule send_notice to be called every two hours
sched.add_job(send_notice, 'interval', seconds=20)

sched.start()
