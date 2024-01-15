class TV():
    def __init__(self, namn, kanal = 55, volym = 3):
        self.namn = namn
        self.kanal = kanal
        self.volym = volym

    def __str__(self):
        return ("%s \nSound volume: %s \nChannel: %s" % (self. namn, self.kanal, self.volym))

    def hojVolym(self):
        if self.volym >= 10:
            self.volym = 10
        else:
            self.volym += 1

    def sankVolym(self):
        if self.volym <= 0:
            self.volym = 0
        else:
            self.volym -= 1

    def bytKanal(self, kanal):
        self.kanal = kanal