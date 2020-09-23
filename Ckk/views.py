from django.shortcuts import render
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'Ckk/split.html'
    #context_object_name 

    def get_queryset(self):
        """
        Return the last five published questions (not including those set
        to be published in the future.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

        