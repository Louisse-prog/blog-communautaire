from django.shortcuts import render
data=[
    {
        "id":"1",
        "content":"Article 1"
    },
    {
        "id":"2",
        "content":"Article 2"
    },
    ]


#definition des vues

def index(request):
    context={
        "articles":data
    }
    
    return render(request,"index.html",context)


#view detail
def details(request,id):
    article=None
    for i in data:
        if i["id"]==id:
            article=i

    context={
        "article":article
    }
    return render(request,"details.html",context)

   

def search(request):
    q=request.GET.get('q','')
    results=[]

    for article in data:
        if q.lower() in article['content'].lower():
            results.append(article)

    context={
        'query':q,
        'articles':results
    }

    return render(request,'search.html',context)