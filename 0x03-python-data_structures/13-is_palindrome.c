#include "lists.h"
bool compareLists(listint_t *head1, listint_t *head2);
void reverse(listint_t **head_ref);

/**
 * reverse - reverses a singly linked list
 * @head_ref: double pointer to head of list
 * Return: void
 */
void reverse(listint_t **head_ref)
{
	listint_t *prev = NULL;
	listint_t *current = *head_ref;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_ref = prev;
}

/**
 * compareLists - compares two listint_t lists
 * @head1: pointer to head of first list
 * @head2: pointer to head of second list
 * Return: 0 if the lists are not the same, 1 if they are the same
 */
bool compareLists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		return (false);
	}

	if (temp1 == NULL && temp2 == NULL)
	return (true);

return (false);
}
/**
 * is_palindrome - checks if a listint_t list is a palindrome
 * @head: double pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head;
	listint_t *second_half, *prev_of_slow_ptr = *head;
	listint_t *midnode = NULL;
	bool res = true;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_of_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		if (fast_ptr != NULL)
		{
			midnode = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		second_half = slow_ptr;
		prev_of_slow_ptr->next = NULL;
		reverse(&second_half);
		res = compareLists(*head, second_half);
		reverse(&second_half);

		if (midnode != NULL)
		{
			prev_of_slow_ptr->next = midnode;
			midnode->next = second_half;
		}
		else
		prev_of_slow_ptr->next = second_half;
	}
	return (res);
}
