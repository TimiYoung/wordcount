from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

def home(request):
    if request.method=='GET':
        return render(request,'home.html')
    else:
        text = request.POST.get('text', '')
        total_count = len(text)
        print(text)
        word_dict = {}
        for word in text:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1

        dict_word = sorted(word_dict.items(), key=lambda w: w[1], reverse=True)

        return render(request, 'count.html', {'count': total_count, 'text': text, 'worddict': dict_word})

def about(request):
    return render(request,'about.html')
