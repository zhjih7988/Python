# coding: utf-8

from login.bot import QQBot
from login.plugin import PluginManager

__all__ = (
    "bot"
)

bot = QQBot()
plugin_manager = PluginManager(load_now=False)