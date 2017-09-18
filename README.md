# WhatsappStatistics
Application to obtain statistics about users, messages, photos, gifs... from a whatsapp conversation file

## Requirements

- Python 2.7 (not tested on python3, at least the prints should be modified)

## Execution

To execute, type from a terminal, in the main folder:
```
python src/whatsapp_file_processor.py
```
The default chat file placement is in _data/input.txt_

In case that you want to use your file without the need to move it to that folder and change the name, you can specify it's path as an argument like this:
```
python src/whatsapp_file_processor.py --input-file='your_file_path'
```
