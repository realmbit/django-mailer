import logging

from django.core.management.base import BaseCommand

from mailer.models import Message


class Command(BaseCommand):
    help = "Attempt to resend any deferred mail."

    def handle(self, **options):
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        count = Message.objects.retry_deferred() # @@@ new_priority not yet supported
        logging.info("%s message(s) retried" % count)
