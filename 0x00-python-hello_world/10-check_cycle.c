#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * find_listint_loop - function to find a loop in a linked list
 * @list: pointer to NULL
 *
 * Return: the address of the node where the loop starts or NULL
 */
int check_cycle(listint_t *list)
{
	listint_t cpy;
	listint_t end;

	if (list)
	{
		end = *list;
		cpy = *list;
		end.next = list->next;
		end.n = 0;
		cpy.n = 0;
		while (end.next)
		{
			end.n = 0;
			cpy.next = list;
			cpy.n = cpy.n + 1;
			for (; list != end.next; end.n = end.n + 1)
				list = list->next;
			if (end.n != cpy.n)
				return (1);
			end.next = list->next;
			list = cpy.next;
		}
	}
	return (0);
}
