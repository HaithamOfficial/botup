import os


class Config(object):
    BOT_TOKEN = os.environ.get("1909762014:AAGvq2FhMWTNrXBhr_SEdabo1rG8y9whWaA", "")

    APP_ID = int(os.environ.get("7046849", 1234))

    API_HASH = os.environ.get("6cd79a0e825e23003e970479c7816e07
", "")

    UPDATES_CHANNEL = os.environ.get("ApkHW", "")
