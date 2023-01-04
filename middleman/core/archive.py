import enum
from internetarchive import get_item, upload
from retry import retry
from core.worker import worker
import time
import random


class FileCodes(enum.Enum):
    text = '00'
    presentation = '01'
    audio = '02'
    worksheet = '03'
    misc = '11'


class Archive:
    identifier = ''
    kwargs = dict()

    def __init__(self):
        self.String1 = "Hello"
        self.String2 = "World"

    def fulfillment(self):

        def parser():
            collection = worker.push_list_0th(self)

            print(len(worker.get_list(self)))
            c = (str(collection['collection']))
            t = (str(collection['title']))
            m = (str(collection['mediatype']))
            f = (str(collection['file']))

            md = {'collection': c, 'title': t, 'mediatype': m}
            access = "d1xxwWokX0GARijy"
            secret = "bjhwf9nkP4RGz1vO"

            self.kwargs = dict(
                files=['files/' + f],
                metadata=md,
                access_key=access,
                secret_key=secret,
                verbose=True)

            getRand = random.getrandbits(128)
            fmtRand = int(str(getRand)[0:6])
            self.identifier = 'ilivenicely_{0}{1}'.format(FileCodes.text.value, fmtRand)
            discharge(self.identifier, **self.kwargs)

        @retry(tries=5, delay=30, backoff=2)
        def discharge(identifier: str, **kwargs):
            r = upload(identifier, **kwargs)
            print(r[0].status_code)
            if int(r[0].status_code) == 200:
                worker.pop_list_0th(self)
                if len(worker.get_list(self)) != 0:
                    parser()
                    # time.sleep(1)
                else:
                    print("zero files in list")

            return "ultraman"

        parser()
