import argparse
from pathlib import Path
from report_builder import build_and_save_report
import subprocess
import os


BASE_PATH = Path(__file__).resolve().parent.parent

CHAT_LOG_FOLDER_PATH = BASE_PATH / "chat-logs"
CHAT_LOG_FILENAME = "general.json"

REPORT_FOLDER_PATH = BASE_PATH / "reports"
DEFAULT_REPORT_NAME = "chat_log_report"

auth_token = None


class MissingEnvironmentVariable(Exception):
    pass


def get_auth_token_var():
    global auth_token
    auth_token = os.getenv('DISCORD_AUTH_TOKEN')
    if auth_token is None:
        # TODO More description
        raise MissingEnvironmentVariable("DISCORD_AUTH_TOKEN environment variable must be set.")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, help="Name of the final report.", default=None)
    args = parser.parse_args()
    return args

def get_chat_log_path():
    return CHAT_LOG_FOLDER_PATH / CHAT_LOG_FILENAME

def get_channel_to_id_dict():
    args = [
        BASE_PATH / Path('chat-exporter') / Path('DiscordChatExporter.Cli'),
        'dm',
        '-t', auth_token
    ]
    result = subprocess.run(args, capture_output=True, text=True)
    
    channel_to_id = {}
    for line in result.stdout.strip().split('\n'):
        id, channel = line.split(' | ')
        channel_to_id[channel] = id

    return channel_to_id

def choose_option_numbered(choices, prompt):
    # Print all options
    num_to_choice = {}
    for i, choice in enumerate(choices):
        num = i + 1
        num_to_choice[num] = choice
        print(f"[{num}] {choice}")
    print()

    # Keep trying to select valid choice
    while True:
        user_input = input(prompt)
        try:
            chosen_int = int(user_input)
            if chosen_int in range(1, len(num_to_choice) + 1):
                return num_to_choice[chosen_int]
            else:
                print("Choice out of range, try again.")
        except:
            print("Input invalid, try again.")

def download_chat_log(channel_id, channel_name):
    args = [
        BASE_PATH / Path('chat-exporter') / Path('DiscordChatExporter.Cli'),
        'export',
        '-c', channel_id,
        '-t', auth_token,
        '-f', 'Json',
        '-o', CHAT_LOG_FOLDER_PATH / get_log_filename(channel_id, channel_name)
    ]
    subprocess.run(args)

    # TODO: Add error checking

def select_channel_id():
    channel_to_id = get_channel_to_id_dict()
    chosen_channel = choose_option_numbered(channel_to_id.keys(), "Choose channel: ")
    id = channel_to_id[chosen_channel]
    return id, chosen_channel

def get_log_filename(channel_id, channel_name):
    return f"{channel_name}_{channel_id}.json"

def get_channel_source_to_id_dict():
    pass

def select_channel_source():
    channel_source_to_id = get_channel_source_to_id_dict()

def main():
    args = parse_args()
    
    get_auth_token_var()
    
    print("\n-- Chat Log Source --\n")
    

    print("\nFetching available channels...\n")
    channel_id, channel_name = select_channel_id()
    chat_log_path = CHAT_LOG_FOLDER_PATH / get_log_filename(channel_id, channel_name)
    
    # Download log if not already downloaded
    if not chat_log_path.is_file():
        print()
        download_chat_log(channel_id, channel_name)
        print()

    print("\nStarting report generation...")

    report_name = args.name if args.name is not None else channel_name
    build_and_save_report(chat_log_path, REPORT_FOLDER_PATH, report_name)

if __name__ == '__main__':
    main()