from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from abc import ABC
from dateutil.parser import parse

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(ABC, Iterable):
    @abstractmethod
    def is_due(self):
        pass


class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text