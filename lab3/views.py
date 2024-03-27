from django.shortcuts import render



def index(request):
    if request.method == 'POST':
        ignoredChars = '()[]\{\}\\|/*!`<>,.&?:^%$;№#~»«;"\'+=-_—\r\n'
        origText = request.POST['text']
        text = origText
        for i in ignoredChars:
            text = text.replace(i, ' ')
        text = text.lower()
        
        words = text.split(" ")
        words = list(filter(None, words))
        print(words)
    else:
        words = []
        origText = ''
    return render(request, 'html/lab3.html', {'words': words, 'text': origText})