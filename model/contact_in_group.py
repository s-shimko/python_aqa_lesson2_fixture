from sys import maxsize

class ContactInGroup:

    def __init__(self, id=None, group_id=None):
        self.id = id
        self.group_id = group_id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


    def __repr__(self):
        return "%s: %s " % (self.id, self.group_id)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.group_id == other.group_id