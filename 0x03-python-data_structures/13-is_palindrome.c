#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
/**
  * reverse - reverses singly linked list
  * @head: head of list to be reversed
  *
  * Return: None
*/
void reverse(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *previous;

	previous = NULL;
	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
}

/**
  * compare - compares the items of a list
  * @hr1: head of first half
  * @hr2: head of second
  *
  * Return: 1 if equal, 0 if not
  */
int compare(listint_t *hr1, listint_t *hr2)
{
	listint_t *fh1;
	listint_t *fh2;

	fh1 = hr1;
	fh2 = hr2;

	while (fh1 != NULL && fh2 != NULL)
	{
		if (fh1->n == fh2->n)
		{
			fh1 = fh1->next;
			fh2 = fh2->next;
		}
		else
		{
			return (0);
		}
	}

	if (fh1 == NULL && fh2 == NULL)
		return (1);
	return (0);
}

/**
  * is_palindrome - checks if a singly linked list
  * is a palindrome
  * @head: singly linked list to be checked
  *
  * Return: 1 if palindrome, 0 if not
  */
int is_palindrome(listint_t **head)
{
	listint_t *fast_ptr, *slow_ptr, *p_slow;
	listint_t *middle, *shf;
	int ret;

	slow_ptr = fast_ptr = p_slow = *head;
	middle = NULL;
	ret = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			p_slow = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		if (fast_ptr != NULL)/*fast is not NULL if elements are odd*/
		{
			middle = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		shf = slow_ptr;
		p_slow->next = NULL; /*NULL terminating the first half*/
		reverse(&shf);
		ret = compare(*head, shf);
		reverse(&shf); /*reconstructing original list*/

		if (middle != NULL)/*inserting midnode in odd element case*/
		{
			p_slow->next = middle;
			middle->next = shf;
		}
		else
		{
			p_slow->next = shf;
		}
	}
	return (ret);
}
