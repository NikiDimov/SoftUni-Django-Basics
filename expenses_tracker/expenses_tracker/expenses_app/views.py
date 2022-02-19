from django.shortcuts import render, redirect

from expenses_tracker.expenses_app.forms import CreateProfileForm, CreateExpenseForm, EditExpenseForm, \
    DeleteExpenseForm, EditProfileForm, DeleteProfileForm
from expenses_tracker.expenses_app.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]


def show_index(request):
    user = get_profile()
    if not user:
        return redirect('create profile')
    expenses = Expense.objects.all()
    budget_left = user.budget - sum([expense.price for expense in expenses])
    context = {
        'expenses': expenses,
        'user': user,
        'budget_left': budget_left,
    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateExpenseForm()
        context = {'form': form}
        return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditExpenseForm(instance=expense)
        context = {'form': form, 'expense': expense}
        return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteExpenseForm(instance=expense)
        context = {'form': form, 'expense': expense}
        return render(request, 'expense-delete.html', context)


def profile_page(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    total_items = len(expenses)
    budget_left = profile.budget - sum(e.price for e in expenses)
    context = {
        'profile': profile,
        'total_items': total_items,
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()
        context = {
            'form': form,
            'no_profile': True,
        }
        return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditProfileForm(instance=profile)
        context = {'form': form}
        return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)
        context = {'form': form}
        return render(request, 'profile-delete.html', context)

