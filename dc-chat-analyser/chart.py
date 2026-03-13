from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from abc import ABC, abstractmethod


class Chart(ABC):

    @property
    @abstractmethod
    def default_save_name(self):
        pass

    def __init__(self, chat):
        self.chat = chat

    @abstractmethod
    def generate_plot(self) -> None:
        pass

    def save_plot(self, save_folder_path, save_name=None) -> Path:
        save_name = self.default_save_name if save_name is None else save_name
        save_path = save_folder_path / (save_name + '.svg')
        plt.savefig(save_path, bbox_inches="tight")
        plt.close()
        return save_path

class MessagePerPersonChart(Chart):
    
    @property
    def default_save_name(self) -> str:
        return "message-per-person"

    def __init__(self, chat):
        super().__init__(chat)

    def generate_plot(self) -> None:
        # Generate data
        sorted_users = sorted(self.chat.users.values(), key = lambda user : user.messages_sent, reverse=True)
        labels = [user.username for user in sorted_users]
        values = [user.messages_sent for user in sorted_users]

        if len(labels) > 10:
            labels = labels[:20]
            values = values[:20]

        # Create chart
        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_title("Messages Sent Per Person")
        ax.set_ylabel("Count")
        ax.tick_params(axis='x', labelrotation=90)

        return self

class MessageFrequencyChart(Chart):

    @property
    def default_save_name(self) -> str:
        return "message-frequency-over-time"

    def __init__(self, chat):
        super().__init__(chat)

    def generate_plot(self) -> None:
        timestamps = [msg.timestamp for msg in self.chat.messages]

        # Convert to datetime objects
        datetimes = [datetime.fromtimestamp(ts) for ts in timestamps]

        # Plot
        fig, ax = plt.subplots(figsize=(12, 8))

        ax.hist(datetimes, bins=100, color='steelblue', edgecolor='none')

        # Format x-axis as readable dates
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        fig.autofmt_xdate()

        ax.set_title('Message Frequency Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Messages')
        plt.tight_layout()

        return self