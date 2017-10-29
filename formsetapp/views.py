from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.contrib import messages
from .forms import PersonForm
from .models import Person


def person_formset_view(request):

  PersonFormset = formset_factory(PersonForm)

  if request.method == 'POST':
    person_formset = PersonFormset(request.POST)

    if person_formset.is_valid():

      new_people = []

      for  person_form in person_formset:
        name = person_form.cleaned_data.get('name')

        if name:
          new_people.append(Person(name=name))

      try:
        Person.objects.bulk_create(new_people)

        # And notify our users that it worked
        messages.success(request, 'You have updated your people.')

      except: #If the transaction failed
        messages.error(request, 'There was an error saving your people.')
        return redirect(reverse('add-person'))

  else:
    person_formset = PersonFormset()

  context = {
    'person_formset': person_formset 
  }

  return render(request, 'formsetapp/add_person.html', context)

