from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.translation import gettext_lazy as _
from . import forms, models


def index(request):
    return render(request, 'adboard_site/index.html')


@login_required
def adpost_reserve(request, pk):
    adpost = get_object_or_404(models.AdPost, pk=pk)
    error = False
    if adpost.status >= 20:
        error = True
        messages.error(request, _("The item cannot be sold for you at the moment, sorry."))
    if request.user == adpost.owner:
        error = True
        messages.error(request, _("You cannot buy from yourself."))
    if not error:
        adpost.status = models.ADPOST_STATUS.reserved
        adpost.buyer = request.user
        adpost.save()
        messages.warning(request, _("The item was reserved for you and the seller will contact you to arrange the sale."))
    return redirect('adpost_detail', adpost.pk)


@login_required
def adpost_sell(request, pk):
    adpost = get_object_or_404(models.AdPost, pk=pk)
    if request.user == adpost.owner and adpost.status == 20 and adpost.buyer:
        adpost.status = models.ADPOST_STATUS.sold
        adpost.save()
        messages.success(request, _("Sold!"))
    else:
        messages.error(request, _("Error confirming item sale."))
    return redirect('adpost_detail', adpost.pk)


@login_required
def adpost_reject(request, pk):
    adpost = get_object_or_404(models.AdPost, pk=pk)
    if request.user == adpost.owner and adpost.status == 20 and adpost.buyer:
        adpost.status = models.ADPOST_STATUS.active
        adpost.save()
        messages.info(request, _("Offer rejected, continueing sale!"))
    else:
        messages.error(request, _("Error confirming item sale rejection."))
    return redirect('adpost_detail', adpost.pk)


class AdPostList(generic.ListView):
    model = models.AdPost
    template_name = 'adboard_site/adpost_list.html'


class AdPostDetail(generic.DetailView):
    model = models.AdPost
    template_name = 'adboard_site/adpost_detail.html'


class AdPostCreate(LoginRequiredMixin, generic.CreateView):
    model = models.AdPost
    form_class = forms.AdPostForm
    template_name = 'adboard_site/adpost_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.status = models.ADPOST_STATUS.new
        return super().form_valid(form)


class AdPostEdit(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = models.AdPost
    form_class = forms.AdPostUpdateForm
    template_name = 'adboard_site/adpost_create.html'

    def test_func(self):
        return self.get_object().owner == self.request.user and \
            (self.get_object().status < 20 or \
                (self.get_object().status > 30 and self.get_object() < 99)
            )
