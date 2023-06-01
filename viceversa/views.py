from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	number_of_words = len(user_text.split())
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext': user_text, 'reversed_text':reversed_text,
		'number_of_words': number_of_words})