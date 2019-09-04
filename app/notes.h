#ifndef __NOTES_H__
#define __NOTES_H__

#include <stdint.h>


typedef struct {
	uint8_t status;
	uint8_t channel;
	uint8_t note;
	uint8_t velocity;
	uint32_t ticks;
} NOTE;

typedef struct {
	NOTE note;
	NOTE_NODE * next;
} NOTE_NODE;


#endif /* __NOTES_H__ */
