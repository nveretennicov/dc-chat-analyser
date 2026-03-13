import shutil
from pathlib import Path
import chart
from pdf_converter import save_document
from chat_log_parser import ChatLogParser
from chat_data import Chat
from document_builder.document import Document


def prepare_folder(path : Path) -> None:
    shutil.rmtree(path, ignore_errors=True)
    path.mkdir()

def build_and_save_report(chat_log_path: Path, output_path: Path, report_name: str) -> None:
    report_folder_path = output_path / report_name
    asset_path = report_folder_path / "assets"
    
    prepare_folder(report_folder_path)
    prepare_folder(asset_path)

    print("Parsing chat log...")
    
    chat = ChatLogParser.build_chat_object(chat_log_path)

    print("Building report HTML...")

    document = build_report_document(chat, asset_path)
    save_document(document, report_name, report_folder_path, asset_path)

    print(f"Report has been saved at\n{report_folder_path}/{report_name}.pdf")

def build_report_document(chat : Chat, asset_path : Path) -> Document:
    document = (
        Document()
        .add_header("Chat Log Report", 1)

        .add_header("Overview", 2)
        .add_paragraph(f"""Total messages sent: {len(chat.messages)}""")

        .add_page_break()

        .add_header("Most Active Users")
        .add_image(
            chart.MessagePerPersonChart(chat)
            .generate_plot()
            .save_plot(asset_path)
        )
        
        .add_page_break()

        .add_header("Chat Frequency Over Time", 2)
        .add_image(
            chart.MessageFrequencyChart(chat)
            .generate_plot()
            .save_plot(asset_path)
        )
    )

    return document