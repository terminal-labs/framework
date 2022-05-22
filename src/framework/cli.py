import time

#from .config import my_version
from .config._build_resources import my_version

import arrow
import click


@click.command()
@click.argument("tz")
@click.option("--repeat", "-r", default=1, type=int)
@click.option("--interval", "-i", default=3, type=int)
def app(tz, repeat=1, interval=3):
    time.sleep(30)
    print(my_version)
