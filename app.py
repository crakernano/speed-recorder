import sched, time
from main import main
from datetime import datetime

def app():
    s = sched.scheduler(time.time, time.sleep)

    programador = sched.scheduler()
    comienzo = time.time()
    print('COMIENZO:', datetime.now())

    programador.enter(3600, 1, main)
    programador.run()

    print('FINAL   :', datetime.now())

try:
    while True:
        app()

except KeyboardInterrupt:
    print("Bye!")
    raise SystemExit
