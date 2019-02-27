from datetime import datetime

start_time = datetime.now()

with open('prime.txt', 'w') as out:
    out.write(f'{2 ** 82589933 - 1}')

time_elapsed = datetime.now() - start_time

print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
