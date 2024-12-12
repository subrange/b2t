class Token:
    def __init__(self,typ,val,pos):
        self.typ=typ
        self.val=val
        self.pos=pos

    def __repr__(self):
        return f"Token({self.typ},{repr(self.val)},{self.pos})"