#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - checks whether there's a loop in a list
  * @list: list  to be checked
  *
  * Return: 0 if no cycle, 1 if cycle is present
  */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;
	slow_ptr = malloc(sizeof(listint_t));
		if (!slow_ptr)
			return (0);
	fast_ptr = malloc(sizeof(listint_t));
		if (!fast_ptr)
			return (0);
	slow_ptr = list;
	fast_ptr = list;

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{	slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (slow_ptr == fast_ptr)
			return (1);
	}
	return (0);
}
