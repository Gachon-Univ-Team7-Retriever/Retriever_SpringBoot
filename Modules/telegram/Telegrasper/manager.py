import asyncio
import typing

from . import (ConnectMethods, ChannelMethods, TelegramBaseManager)


class TelegramManager(ConnectMethods, ChannelMethods, TelegramBaseManager):
    pass