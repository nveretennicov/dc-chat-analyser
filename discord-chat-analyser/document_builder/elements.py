from dataclasses import dataclass

class Element:
    pass

@dataclass
class Header(Element):
    text: str
    level: int = 1

@dataclass
class Paragraph(Element):
    text: str

@dataclass
class Image(Element):
    src: str
    width: str = "100%"

@dataclass
class PageBreak(Element):
    pass