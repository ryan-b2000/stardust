#include <stdbool.h>
#include <stdint.h>
#include "notes.h"

static NOTE_NODE * list_tail;
static NOTE_NODE * list_head;

void note_add_note_to_list(NOTE to_add) {

	// make the new node to the tail of the list and go to it
	list_tail->next = (NOTE_NODE*) malloc (sizeof(NOTE_NODE));
	list_tail = list_tail->next;

	// add the new node items
	list_tail->note.channel = to_add.channel;
	list_tail->note.note = to_add.note;
	list_tail->note.velocity = to_add.velocity;

	list_tail->next = NULL;
}


void get_note_list_head(NOTE_NODE * head) {
	head = list_head;
}

void display_note_list() {

	NOTE_NODE * head = list_head;

	while (head->next != NULL) {
		printf("note: %d ", head->note.note);
		printf("velo: %d ", head->note.velocity);
		printf("chan: %d ", head->note.channel);
		printf("\n");
		head = head->next;
	}
}
