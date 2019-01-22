import stomp
import time

from everett.ext.yamlfile import ConfigYamlEnv
from everett.manager import ConfigManager

config = ConfigManager([
    ConfigYamlEnv('local_config.yaml'),
])

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        for k, v in headers.items():
            print('header: key %s , value %s' % (k, v))
            print('received a message "%s"' % message)
            with open("messages.log", "a") as logfile:
                logfile.write(message)

YOUR_API_KEY_HERE = config('BMRS_API_KEY')
conn = stomp.Connection12(host_and_ports=[('api.bmreports.com', 61613)], use_ssl=True)
conn.set_listener('', MyListener())
conn.start()
conn.connect(YOUR_API_KEY_HERE, YOUR_API_KEY_HERE, True)
conn.subscribe(destination='/topic/bmrsTopic', ack='auto', id='CS_UOB')
while conn.is_connected():
    time.sleep(1)
