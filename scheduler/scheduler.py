import logging
import time

import schedule

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


# schedule.every(1440).minutes.do()

while 1:
    schedule.run_pending()
    time.sleep(1)
