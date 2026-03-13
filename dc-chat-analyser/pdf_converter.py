from weasyprint import HTML

def save_document(document, save_name, save_path, asset_path='.'):
    print("Rendering document HTML...")
    html = document.render_html()
    
    print("Converting to pdf...")
    HTML(string=html, base_url=asset_path).write_pdf(f"{save_path / save_name}.pdf")