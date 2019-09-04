#ifndef __MIDI_H__
#define __MIDI_H__

/*	MIDI HEADER CHUNK
 *
 *	header ::	identifies the type of chunk --> 'Mthd'
 *
 *	chunklen ::	the number of bytes comprising the data (always 6 for header)
 *
 *	format :: 	specifies how many MIDI track chunks there are and how they are to be played
 *	0 -> file contains just a single MTrk chunk that can contain multi-channel MIDI data
 *	1 -> file contains two or more MTrk chunks that are to be played simultaneously
 *	2 -> file contains two or more Mtrk chunks that are to be played independently
 *
 *	ntracks :: 	the number of MTrk chunks
 *
 *	tickdiv ::	specifies the timing interval to be used and whether timecode or metrical
 *				timing is to be used
 */
typedef struct {
	uint32_t header;
	uint32_t chunklen;
	uint16_t format;
	uint16_t ntracks;
	uint16_t tickdiv;

} MIDI_HEADER_CHUNK;

typedef struct {
	uint32_t header;
	uint32_t chunklen;
	uint8_t * data;
} MIDI_TRACK_CHUNK;

typedef struct {
	uint8_t delta [4];		// up to 4 bytes for the delta time in tickdivs since previous event
	uint8_t message [3];	// 3 bytes make up the midi event
} MIDI_EVENT;

typedef struct {

	uint8_t note;

} MIDI_EVENT_CHANNEL;

uint32_t create_midi_file(NOTE_NODE * list);

uint32_t calculate_track_chunklen(NOTE_NODE * list);

MIDI_EVENT create_track_event(NOTE * event);

void create_track_chunk(NOTE_NODE * list, MIDI_TRACK_CHUNK * chnk);

uint32_t add_event_to_track_chunk(NOTE toadd, MIDI_TRACK_CHUNK * chnk);

uint32_t write_header_chunk(MIDI_HEADER_CHUNK chnk);

uint32_t write_track_chunk(MIDI_TRACK_CHUNK chnk);

uint32_t compute_delta_time(uint32_t tickdiv);

uint32_t file_open(char * filename);

uint32_t file_close();


#endif /* __MIDI_H__ */
