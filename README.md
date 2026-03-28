# Subtitlesync-CLI

A terminal-based utility designed to adjust the timing of SubRip (.srt) subtitle files. Users often encounter video files where the audio and subtitles are out of sync. This tool allows users to specify an offset in milliseconds (e.g., +2000 for 2 seconds delay or -1500 for 1.5 seconds early) to shift all timestamps within the file at once. It uses regular expressions to parse the timestamp blocks, applies the arithmetic shift, and saves a new synchronized subtitle file without modifying the original. This is a practical, real-world utility for media enthusiasts who manage local movie collections.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
- [Future Work](#future-work)
- [License](#license)

## Installation

```bash
git clone <repo-url>
cd subtitlesync-cli
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Run the main entry point to start Subtitlesync-CLI.

## Project Structure

```
├── cli.py
├── processor.py
├── parser.py
├── time_utils.py
├── exceptions.py
├── requirements.txt
└── README.md
```

## Modules

- **entry_point**: Core module for entry_point functionality.
- **core**: Core module for core functionality.
- **utils**: Core module for utils functionality.

## Future Work

- [ ] Add comprehensive test suite
- [ ] Implement CI/CD pipeline
- [ ] Add Docker support
- [ ] Improve error handling and edge cases
- [ ] Add configuration documentation
- [ ] Performance optimization

## License

This project is licensed under the MIT License.
