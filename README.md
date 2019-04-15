# SymphoScriber

## What is Symphoscriber
Symphoscriber is a template matching audio transcriber. The model extracts sheet music and instrument data from an audio file containing sounds from multiple sources with variations. The algorithm ideally will identify the basic sounds of certain instruments (e.g. piano, tuba, violin) and encode the audio in terms of MIDI-like events (instrument, pitch, intensity, duration, for example), vastly reducing the data complexity and producing an easily workable data format as well.

As an example, given a MP3 file of the recording of an orchestra’s performance of some symphony as input, the model outputs some MIDI-like events that contains the sheet music and instrument data from. 
