#include "lists.h"

/**
 * insert_node - a function that inserts a new node at a given position/index
 * @head: double pointer to the content of the memory pointed to by the pointer
 * held by head
 * @number: value to insert at designated index
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *currentNode;

	if (head == NULL)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	currentNode = *head;
	while (currentNode->next != NULL && number > currentNode->next->n)
		currentNode = currentNode->next;

	newNode->next = currentNode->next;
	currentNode->next = newNode;
	return (newNode);
}

