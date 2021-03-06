# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Question(Document):

	def validate(self):
		self.check_at_least_one_option()
		self.check_minimum_one_correct_answer()

	def check_at_least_one_option(self):
		if len(self.options) <= 1:
			frappe.throw(_("A question must have more than one options"))
		else:
			pass

	def check_minimum_one_correct_answer(self):
		correct_options = [option.is_correct for option in self.options]
		if bool(sum(correct_options)):
			pass
		else:
			frappe.throw(_("A qustion must have at least one correct options"))

	def get_answer(self):
		options = self.options
		answers = [item.name for item in options if item.is_correct == True]
		if len(answers) == 0:
			frappe.throw("No correct answer is set for {0}".format(self.name))
			return None
		elif len(answers) == 1:
			return answers[0]
		else:
			return answers