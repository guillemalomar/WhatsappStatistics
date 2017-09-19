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
## Example outputs
![alt text][logo1]

[logo1]: https://github.com/guillemnicolau/WhatsappStatistics/blob/master/documentation/example_outputs/WhatsappMessagesPerDay.png?raw=true "Messages classified by day hour"

(days are shown in YYMMDD logic)

![alt text][logo2]

[logo2]: https://github.com/guillemnicolau/WhatsappStatistics/blob/master/documentation/example_outputs/WhatsappTimes.png?raw=true "Messages classified by day hour"

![alt text][logo3]

[logo3]: https://github.com/guillemnicolau/WhatsappStatistics/blob/master/documentation/example_outputs/WhatsappMessages.png?raw=true "Messages classified user"

![alt text][logo4]

[logo4]: https://github.com/guillemnicolau/WhatsappStatistics/blob/master/documentation/example_outputs/WhatsappChars.png?raw=true "Total characters in messages classified user"

![alt text][logo5]

[logo5]: https://github.com/guillemnicolau/WhatsappStatistics/blob/master/documentation/example_outputs/WhatsappWord.png?raw=true "Times each user has said a given word"
