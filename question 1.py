#Write a Python program to print a given doubly linked list in reverse order.

import math

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def reversePrint(head_ref):
	tail = head_ref

	while (tail.next != None):
		tail = tail.next

	while (tail != head_ref):
		print(tail.data, end = " ")
		tail = tail.prev

	print(tail.data)

def fPrint(head_ref):
	while (head_ref.next != None):
		print(head_ref.data, end = " ")
		head_ref = head_ref.next

	print(head_ref.data)

def push(head_ref, new_data):

	new_node = Node(new_data)

	new_node.data = new_data

	new_node.prev = None

	new_node.next = head_ref

	if (head_ref != None):
		head_ref.prev = new_node

	head_ref = new_node
	return head_ref

if __name__=='__main__':

	head = None

	head = push(head, 20)
	head = push(head, 15)
	head = push(head, 10)
	head = push(head, 5)

	print("Linked List elements are : ")
	fPrint(head)
	print("Linked List elements in reverse order : ")
	reversePrint(head) 
