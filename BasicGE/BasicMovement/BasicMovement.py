# coding= utf-8


class BasicMovement (object):

    def move(self, dx, dy):
        if dx != 0:
            self.rect.centerx += dx
        if dy != 0:
            self.rect.centery += dy
        return (dx, dy)