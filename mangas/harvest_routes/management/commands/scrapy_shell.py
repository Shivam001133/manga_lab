import logging
import sys
from pathlib import Path

from django.core.management.base import BaseCommand
from scrapy.cmdline import execute
from src.message import logging_message

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Scrape data from given domain"

    def add_arguments(self, parser):
        parser.add_argument(
            "--url",
            "-u",
            dest="url",
            type=str,
            help="This url used to scrape in shell",
        )

    def handle(self, **kwargs):
        url = kwargs["url"]

        logger.info(
            logging_message.MANAGMENT_COMMAND_STARTED.format(
                MESSAGE="Scrapy shell started",
            ),
        )

        sys.path.append(Path.cwd())
        execute(["scrapy", "shell", url])

        logger.info(
            logging_message.MANAGMENT_COMMAND_END.format(MESSAGE="Scrapy shell ended"),
        )
