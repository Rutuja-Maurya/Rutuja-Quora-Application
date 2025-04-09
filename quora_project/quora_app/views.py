from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login
from django.http import JsonResponse, HttpResponseForbidden
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Registration successful! Welcome to Quora Clone.')
        return response

@login_required
def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions': questions})

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, 'Your question has been posted successfully!')
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})

@login_required
def edit_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if question.author != request.user:
        return HttpResponseForbidden("You don't have permission to edit this question.")
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your question has been updated successfully!')
            return redirect('question_detail', pk=pk)
    else:
        form = QuestionForm(instance=question)
    
    return render(request, 'edit_question.html', {
        'form': form,
        'question': question
    })

@login_required
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if question.author != request.user:
        return HttpResponseForbidden("You don't have permission to delete this question.")
    
    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Your question has been deleted successfully!')
        return redirect('home')
    
    return render(request, 'delete_question.html', {'question': question})

@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
    
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            messages.success(request, 'Your answer has been posted successfully!')
            return redirect('question_detail', pk=pk)
    else:
        form = AnswerForm()
    
    return render(request, 'question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

@login_required
def edit_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if answer.author != request.user:
        return HttpResponseForbidden("You don't have permission to edit this answer.")
    
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your answer has been updated successfully!')
            return redirect('question_detail', pk=answer.question.pk)
    else:
        form = AnswerForm(instance=answer)
    
    return render(request, 'edit_answer.html', {
        'form': form,
        'answer': answer
    })

@login_required
def delete_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if answer.author != request.user:
        return HttpResponseForbidden("You don't have permission to delete this answer.")
    
    question_pk = answer.question.pk
    if request.method == 'POST':
        answer.delete()
        messages.success(request, 'Your answer has been deleted successfully!')
        return redirect('question_detail', pk=question_pk)
    
    return render(request, 'delete_answer.html', {'answer': answer})

@login_required
def like_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
        liked = False
    else:
        answer.likes.add(request.user)
        liked = True
    
    return JsonResponse({
        'liked': liked,
        'like_count': answer.like_count()
    })

@login_required
def get_likers(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    return JsonResponse({
        'likers_text': answer.get_likers()
    })
