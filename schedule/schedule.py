import sched, time

s = sched.scheduler(time.time, time.sleep)

def config_schedule():
    s.enter(10, 1, job)
    s.enter(5, 2, job, argument=('positional',))
    s.enter(5, 1, job, kwargs={'a': 'keyword'})

def run_scedule():
    s.run()
