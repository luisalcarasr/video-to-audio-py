# Video to Audio Converter

This Python project aims to provide a simple way to convert video files to audio files. Simply run the `run.sh` script to install the necessary dependencies and execute the program.

## Installation

1. Clone this repository or download the source code.
2. Make sure you have Python installed on your system.
3. Put MP4 files in `assets` folder.
4. Run the `run.sh` script:

    ```bash
    ./run.sh
    ```

This script will install the necessary dependencies using `pip` and then execute the video to audio conversion program.

## Usage

Once you have executed `run.sh`, the program will be ready to use. Simply follow the instructions in the console to convert your video files to audio files.

## Dependencies

The project uses the following Python dependencies:

- `moviepy`: For video file manipulation.
- `ffmpeg`: For video to audio conversion.

These dependencies will be automatically installed during the execution of `run.sh`.

## Notes

- Make sure you have enough disk space to store the generated audio files.
- This program utilizes `ffmpeg`, so ensure you have it installed on your system and accessible from the command line.

## License

This project is licensed under the [MIT License](LICENSE).