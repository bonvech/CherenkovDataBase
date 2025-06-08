import json
import plotly.graph_objects as go
import plotly.utils
from django.db.models import Count, F
from django.shortcuts import render
from .forms import HistogramForm
from .models import Event


def histogram(request):
    form = HistogramForm(
        request.GET
        if 'colname' in request.GET else
        {name: field.initial for name, field in HistogramForm.base_fields.items()}
    )
    form_ok = form.is_valid()
    colname = form.cleaned_data['colname']
    context = {
        'colname': colname,
        'form': form,
    }
    if form_ok:
        query = Event.objects
        if form.cleaned_data['height_from'] is not None:
            query = query.filter(height__gte=form.cleaned_data['height_from'])
        if form.cleaned_data['height_to'] is not None:
            query = query.filter(height__lte=form.cleaned_data['height_to'])
        pts = list(query.values_list(colname, flat=True))
        if pts:
            fig = go.Figure(
                data=go.Histogram(
                    x=pts,
                    nbinsx=16,
                ),
            )
            fig.update_layout(
                title='Histogram',
                xaxis_title=colname,
                yaxis_title=None,
                bargap=0.125,
                bargroupgap=0.125,
            )
            context['graph_json'] = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render(request, 'che/histogram.html', context)


def index(request):
    return render(request, 'che/index.html')
