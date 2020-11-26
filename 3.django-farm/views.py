class FarmListView(generic.ListView):
    model = Farm
    paginate_by = 25
    template_name = 'farm/list.html'
    context_object_name = 'farms'
    queryset = Farm.objects.all()


class FarmDetailView(generic.DetailView):
    model = Farm