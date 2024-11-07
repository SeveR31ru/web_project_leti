from django.shortcuts import redirect, render
from django.views.generic.list import ListView

from web_app.forms import TransmitterForm
from web_app.models import Transmitter


class TransmitterListView(ListView):
    model = Transmitter
    queryset = Transmitter.objects.all()
    context_object_name = "transmitters"
    template_name = "transmitters/transmitter_list.html"


def transmitter_view(request, pk):
    """
    Returns a rendered page with information about a single transmitter.

    Args:
        request (Request): The HTTP request.
        pk (int): The primary key of the transmitter.

    Returns:
        HttpResponse: The rendered page.
    """
    transmitter = Transmitter.objects.get(id=pk)
    return render(
        request, "transmitters/transmitter_view.html", {"transmitter": transmitter}
    )


# CUD transmitter


def add_transmitter(request):
    """
    Returns a rendered page with the form for adding a new transmitter.

    Args:
        request (Request): The HTTP request.

    Returns:
        HttpResponse: The rendered page.
    """
    if request.method == "GET":
        form = TransmitterForm()
        return render(request, "transmitters/add_transmitter.html", {"form": form})
    else:
        form = TransmitterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "transmitters/transmitter_added.html")
        else:
            return render(request, "transmitters/add_transmitter.html", {"form": form})


def change_transmitter(request, pk):
    """
    Returns a rendered page with the form for changing a transmitter.

    Args:
        request (Request): The HTTP request.
        pk (int): The primary key of the transmitter.

    Returns:
        HttpResponse: The rendered page.
    """
    transmitter = Transmitter.objects.get(id=pk)

    if request.method == "GET":
        form = TransmitterForm(instance=transmitter)
        return render(request, "transmitters/change_transmitter.html", {"form": form})
    else:
        form = TransmitterForm(request.POST, instance=transmitter)
        if form.is_valid():
            form.save()
            return render(request, "transmitters/transmitter_changed.html")
        else:
            return render(
                request, "transmitters/change_transmitter.html", {"form": form}
            )


def delete_transmitter(request, pk):
    """
    Returns a rendered page with the form for deleting a transmitter.

    Args:
        request (Request): The HTTP request.
        pk (int): The primary key of the transmitter.

    Returns:
        HttpResponse: The rendered page.
    """
    transmitter = Transmitter.objects.get(id=pk)

    if request.method == "GET":
        return render(
            request,
            "transmitters/delete_transmitter.html",
            {"transmitter": transmitter},
        )
    else:
        transmitter.delete()
        return redirect("transmitter_list")
