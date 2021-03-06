import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from mailer.engine import send_all


# allow a sysadmin to pause the sending of mail temporarily.
PAUSE_SEND = getattr(settings, "MAILER_PAUSE_SEND", False)


class Command(BaseCommand):
    help = "Do one pass through the mail queue, attempting to send all mail."

    def handle(self, **kwargs):
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        logging.info("-" * 72)
        # if PAUSE_SEND is turned on don't do anything.
        if not PAUSE_SEND:
            send_all()
        else:
            logging.info("sending is paused, quitting.")
