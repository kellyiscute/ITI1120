class Time(object):
    def __init__(self, hh=0, mm=0, s=0):
        self.hour = hh
        self.minute = mm
        self.second = s

    def set_time(self, hh=12, mm=0, ss=0):
        self.hour = hh % 24 + mm // 60
        self.minute = mm % 60 + ss // 60
        self.second = ss % 60

    def duration(self, t: 'Time'):
        h = t.hour - self.hour
        m = t.minute - self.minute
        s = t.second - self.second
        return Time(h, m, s)

    def __repr__(self):
        return f'{self.hour}:{self.minute}:{self.second}'

    def __eq__(self, other: 'Time'):
        return self.hour == other.hour and self.minute == other.minute and self.second == other.second

    def is_before(self, t: 'Time') -> bool:
        return t.hour < self.hour or t.minute < self.minute or t.second < self.second
