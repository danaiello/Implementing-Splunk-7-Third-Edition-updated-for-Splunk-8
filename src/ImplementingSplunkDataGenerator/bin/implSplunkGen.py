import time
import random
import base64
import hashlib

start = time.time()
m = hashlib.md5()

#run for five minutes
while time.time() < start + 300:
    t = time.strftime('%Y-%m-%dT%H:%M:%S')
    timezone = time.strftime('%z')
    millis = "%.3d" % (time.time() % 1 * 1000)

    #create random values
    level = random.sample(['DEBUG', 'INFO', 'WARN', 'ERROR'], 1)[0]
    message = random.sample(['Don\'t worry, be happy.',
                             'error, ERROR, Error!',
                             'Nothing happened. This is worthless. \
Don\'t log this.',
                             'Hello world.'], 1)[0]

    logger = random.sample(['FooClass',
                            'BarClass',
                            'AuthClass',
                            'LogoutClass',
                            'BarClass',
                            'BarClass',
                            'BarClass',
                            'BarClass'], 1)[0]

    user = random.sample(['bob',
                          'Bobby',
                          'mary',
                          'mary',
                          'linda',
                          'jacky'], 1)[0]

    ip = random.sample(['1.2.3.4',
                        '4.31.2.1',
                        '1.2.3.',
                        '1.22.3.3',
                        '3.2.4.5',
                        '113.2.4.5'], 1)[0]

    req_time = str(int(abs(random.normalvariate(0, 1)) * 1000))
    session_length = str(random.randrange(1, 12240))
    #session_id = base64.b64encode(str(random.randrange(1000000, 1000000000)))
    #session_id = base64.standard_b64encode(bytes(str(random.randrange(123456789,1234567890))))
    m.update(b"a")
    session_id = base64.b64encode(m.digest())
    extra = random.sample(['network=qa',
                           'network=prod',
                           'session_length=' + session_length,
                           'session_id="' + session_id.decode() + '"',
                           'user=extrauser'], 1)[0]

    fields = []
    fields.append('logger=' + logger)
    fields.append('user=' + user)
    fields.append('ip=' + ip)
    fields.append('req_time=' + req_time)
    fields.append(extra)

    fields.pop(random.randrange(0, len(fields)))

    print("%s.%s%s %s %s [%s]" % (t,
                                  millis,
                                  timezone,
                                  level,
                                  message,
                                  ", ".join(fields)))

    time.sleep(random.random())
