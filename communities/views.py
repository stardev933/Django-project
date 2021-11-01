#####################################
# dj default imports
#####################################
from django.contrib.auth.decorators import login_required

#####################################
# HTML routing imports
#####################################
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

#####################################
# Messages
#####################################
from django.contrib import messages

#####################################
# Necessary models
#####################################

from .models import Post

#####################################
# Necessary forms
#####################################
from .forms import PostForm
#####################################
# Outside imports
#####################################
from django.utils import timezone

@login_required
def viewIndex(request):
	querysetLastFivePosts = Post.objects.all()

	context = {
		"qsetLastFivePosts":querysetLastFivePosts,
	}
	return render(request,'communities/index.html',context = context)

@login_required
def viewCreatePost(request):
	modelPost = Post()

	formPostForm = PostForm(instance=modelPost)

	if request.method == "POST":

		# fill with post data
		formPostForm = PostForm(request.POST)

		modelCreatedPost = formPostForm.save(commit=False)

		formPostForm = PostForm(request.POST)

		if formPostForm.is_valid():
			# save the object
			user = request.user

			modelCreatedPost.author = user

			modelCreatedPost.save()

			# show message that post created
			messages.success(request, "Post created.")

			# redirect
			return redirect('communities:index')
	
	context = {
		"formPostForm":formPostForm,
	}
	return render(request, 'communities/create_post.html',context)


	