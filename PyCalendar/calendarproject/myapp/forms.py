from django import forms

class EntryForm(forms.Form):
	name = forms.CharField(max_length=100)
	# Time
	date = forms.DateTimeField()
	# mm/dd/yyyy
	description = forms.CharField(widget=forms.Textarea)
	# what's going on for that specific time?