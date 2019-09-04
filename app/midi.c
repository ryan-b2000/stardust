#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

#include "error.h"
#include "notes.h"
#include "midi.h"
#include "midi_messages.h"

#define MIDI_HEAD_CHUNK_ID ((0x4D << 24) | (0x54 << 16) | (0x68 << 8) | (0x64))
#define MIDI_TRACK_CHUNK_ID ((0x4D << 24) | (0x54 << 16) | (0x72 << 8) | (0x6B))


uint32_t fd_midifile;


uint32_t create_midi_file(NOTE_NODE * notelist) {

	NOTE_NODE * list = sourcelist;
	MIDI_TRACK_CHUNK trkchnk;
	MIDI_HEADER_CHUNK hdrchnk;
	char filename[] = "midfile.mid";
	uint32_t status;

	// Create/Open the MIDI file
	status = file_open(filename);
	if (status < 0) {

	}

	// Create and write the header chunk
	hdrchnk.header = MIDI_HEAD_CHUNK_ID;	// header chunk ID 'Mthd'
	hdrchnk.chunklen = 6;					// header always 6 bytes long
	hdrchnk.tickdiv = 96;					// 96 ppqn
	hdrchnk.ntracks = 1;					// 1 midi track
	hdrchnk.format = 0;						// 1 simultaneous midi track

	write_header_chunk(hdrchnk);

	// Create and write the meta chunk
	create_meta_chunk(&trkchnk);
	write_meta_chunk(trkchnk);

	// Create and write the event chunk
	create_event_chunk(list);
	write_event_chunk(notelist, trkchnk);

	status = file_close();
	if (status < 0) {

	}

	return ERROR_NONE;
}


void create_track_chunk(NOTE_NODE * list, MIDI_TRACK_CHUNK * trkchnk) {


	uint8_t status;

	uint32_t bytecount = 0;
	NOTE_NODE * temp;
	MIDI_EVENT event;

	// Calculate the number of bytes needed
	bytecount = calculate_track_chunklen(list);

	// Allocate the track chunk memory
	trkchnk->data = (uint8_t*) malloc (sizeof(uint8_t) * bytecount);
	memset(trkchnk->data, '\0', bytecount);

	// Configure the header
	trkchnk->header = MIDI_TRACK_CHUNK_ID;
	trkchnk->chunklen = bytecount;

	// Fill in the chunk data
	chnkptr = trkchnk->data;
	temp = list;
	while (temp != NULL) {

		event = create_track_event(temp->note);

		temp = temp->next;
	}


}


MIDI_EVENT create_track_event(NOTE * note) {

	uint32_t ii;
	uint32_t delta = 0;
	uint8_t * chnkptr;
	MIDI_EVENT event;

	// clear the delta entries
	memset(event.delta, 0, 4);

	// fill in the delta time
	delta = compute_delta_time(note->ticks);
	event.delta[0] = delta;
	event.delta[1] = (delta >> 8) & 0xFF;
	event.delta[2] = (delta >> 16) & 0xFF;
	event.delta[3] = (delta >> 24) & 0xFF;

	// fill in the event information
	event.message[0] = note->status | note->channel;
	event.message[1] = note->note;
	event.message[2] = note->velocity;

	return event;
}

uint32_t calculate_track_chunklen(NOTE_NODE * list) {
	NOTE_NODE * temp;
	uint32_t status;
	uint32_t eventcount = 0;
	uint32_t bytecount = 0;

	// Calculate the number of bytes needed
	temp = list;
	while (temp != NULL) {
		++eventcount;

		// allocate event bytes
		status = temp->note.status;
		if (status == NOTE_ON || status == NOTE_OFF || status == POLY_AFTERTOUCH || status == CONTROL_CHANGE)
			bytecount += 3;
		if (status == CHANNEL_AFTERTOUCH || status == PITCH_BEND || status == PROGRAM_CHANGE)
			bytecount += 2;

		// allocate tickdiv bytes
		if (temp->note.ticks < 128)
			bytecount += 1;
		else if (temp->note.ticks < 256)
			bytecount += 2;
		else if (temp->note.ticks < 384)
			bytecount += 3;
		else
			bytecount += 4;

		temp = temp->next;
	}
	printf("Midi events: %d - bytes: %d\n", eventcount, bytecount);

	return bytecount;
}

uint32_t file_open(char * filename) {

	uint32_t status;

	fd_midifile = fopen(filename, O_WRONLY | O_CREAT, 066);
	if (fd_midifile < 0) {
		printf("Error opening file.\n");
		return ERROR_FAIL;
	}

	return ERROR_NONE;
}

uint32_t file_close() {

	uint32_t status;

	status = fclose(fd_midifile);
	if (status < 0) {
		printf("Error closing file.\n");
		return ERROR_FAIL;
	}

	return ERROR_NONE;
}

uint32_t add_event_to_track_chunk(NOTE toadd, MIDI_TRACK_CHUNK * chnk) {



	return ERROR_NONE;
}


uint32_t write_header_chunk(MIDI_HEADER_CHUNK chnk) {

	return ERROR_NONE;
}

uint32_t write_track_chunk(MIDI_TRACK_CHUNK chnk) {

	return ERROR_NONE;
}
