import enum
import pathlib


class Filenames(enum.Enum):
    cfg_file = str(pathlib.Path(__file__).parent.resolve()) + "\\config.json"
    test_file_alerts = str(pathlib.Path(__file__).parent.resolve()) + "\\test_file_alerts.json"
    test_file_frames = str(pathlib.Path(__file__).parent.resolve()) + "\\test_file_frames.json"
