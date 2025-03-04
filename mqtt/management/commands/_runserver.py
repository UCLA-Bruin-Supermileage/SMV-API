import atexit
import signal
import sys
from django.core.management.commands.runserver import BaseRunserverCommand

from mqtt.helper import CLIENT
class Command(BaseRunserverCommand):
    help = 'Execute custom logic when the server is stopping.'
    print('1')

    def __init__(self, *args, **kwargs):
        atexit.register(self._exit)
        signal.signal(signal.SIGINT, self._handle_SIGINT)
        print('hello')
        super(Command, self).__init__(*args, **kwargs)
    def _exit(self):
        # Your custom logic to be executed when the server is stopping
        print("Server is stopping. Execute custom logic here.")
        CLIENT.loop_stop()
    def _handle_SIGINT(signal, frame, self):
        self._exit()
        sys.exit(0)