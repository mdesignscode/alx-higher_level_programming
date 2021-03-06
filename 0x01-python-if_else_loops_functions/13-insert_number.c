#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: linked list.
 * @number: linked list data.
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new_node;

	/* creating new node */
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	/* adding node to beginning of list */
	temp = *head;

	if (!*head || temp->n > number)
	{
		new_node->next = temp;
		*head = new_node;
		return (*head);
	}

	/* adding node to sorted list */
	while (temp->next && temp->next->n < number)
		temp = temp->next;

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
