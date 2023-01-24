from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Notes

class NotesListView(ListView):
    template_name = 'notes/notes_list.html'
    model = Notes
    context_object_name = 'notes'

class NotesDetailView(DetailView):
    template_name = 'notes/notes_detail.html'
    model = Notes
    context_object_name = 'note'

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    try:
        note = Notes.objects.get(pk = pk)
    except Notes.DoesNotExist:
        raise Http404('Note does not exist')
    return render(request, 'notes/notes_detail.html', {'note':note})


