from document_builder.renderer import Renderer
from document_builder.theme_manager import ThemeManager
from document_builder.elements import Element, Header, Paragraph, Image, PageBreak


class Document:
    
    def __init__(self):
        self.elements: list[Element] = []

    def add_header(self, text, level=1):
        self.elements.append(Header(text, level))
        return self

    def add_paragraph(self, text):
        self.elements.append(Paragraph(text))
        return self

    def add_image(self, src, width="100%"):
        self.elements.append(Image(src, width))
        return self

    def add_page_break(self):
        self.elements.append(PageBreak())
        return self

    def render_html(self):
        body = Renderer.render_elements(self.elements)
        css = ThemeManager.get_css()

        return f"""
        <html>
        <head>
            <style>{css}</style>
        </head>
        <body>
            {body}
        </body>
        </html>
        """