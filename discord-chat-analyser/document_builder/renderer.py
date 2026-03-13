from document_builder.elements import Header, Paragraph, Image, PageBreak

class Renderer:
    
    @staticmethod
    def render_elements(elements):
        body = ""
        for element in elements:
            body += Renderer.render(element)
        return body

    @staticmethod
    def render(element):
        if isinstance(element, Header):
            return f'<h{element.level} class="header level-{element.level}">{element.text}</h{element.level}>'

        if isinstance(element, Paragraph):
            return f'<p class="paragraph">{element.text}</p>'

        if isinstance(element, Image):
            return f'<img class="image" src="{element.src}" style="width:{element.width};"/>'

        if isinstance(element, PageBreak):
            return '<div class="page-break"></div>'
        
        return ""