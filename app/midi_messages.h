

#define NOTE_OFF					0x80
#define NOTE_ON						0x90
#define POLY_AFTERTOUCH				0xA0
#define CONTROL_CHANGE 				0xB0
#define PROGRAM_CHANGE				0xC0
#define CHANNEL_AFTERTOUCH			0xD0
#define PITCH_BEND					0xE0

#define SYSEX						0xF0
#define MIDI_TIMECODE_QRTR_FRAME	0xF1
#define SONG_POSITION				0xF2
#define START						0xFA
#define CONTINUE					0xFB
#define STOP						0xFC
#define ACTIVE_SENSING				0xFE
#define SYSTEM_RESET				0xFF

#define STATUS_BYTE(event, channel) (event | channel)
