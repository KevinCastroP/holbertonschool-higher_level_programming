#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 *insert_node - insert a node
 *@head: the head
 *@number: the number
 *Return: the pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *l = *head;
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;
	if (l && newnode->n < l->n)
	{newnode->next = l;
		*head = newnode;
		return (newnode);
	}
	else if (!l)
	{newnode->next = NULL;
		*head = newnode;
		return (newnode);
	}
	while (l != NULL)
	{
		if (l->n < number && l->next && l->next->n > number)
		{newnode->next = l->next;
			l->next = newnode;
			return (newnode);
		}
		else if (l->n == number)
		{newnode->next = l->next;
			l->next = newnode;
			return (newnode);
		}
		else if (l->n < number && !l->next)
		{newnode->next = l->next;
			l->next = newnode;
			return (newnode);
		}
		l = l->next;
	}
	free(newnode);
	return (NULL);
}
