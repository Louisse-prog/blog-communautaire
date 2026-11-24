from django.shortcuts import render
data=[
    {
        "id":"1",
        "title":"Pourquoi apprendre à programmer en 2026?",
        "content":"Apprendre à programmer en 2026 reste essentiel pour superviser l'IA, concevoir des systèmes fiables et résoudre des problèmes complexes que les outils automatisés ne gèrent pas seuls",
        "category":"Technologie"
    },
    {
        "id":"2",
        "title":"Les 5 langages de programmation à découvrir",
        "content":"",
        "category":"Développement"
    },
    {
        "id":"3",
        "title":"Comment organiser efficacement ses études?",
        "content":"",
        "category":"Education"
    },
    {
        "id":"4",
        "title":"L'intelligence artificielle va-t-elle remplacer les développeurs?",
        "content":"",
        "category":"Technologie"
    },
    {
        "id":"5",
        "title":"Pourquoi lire les livres est-il important?",
        "content":"",
        "category":"Culture"
    },
    {
        "id":"6",
        "title":"Les avantages de l'entrepreunariat chez les jeunes",
        "content":"",
        "category":"Entrepreunariat"
    },
    {
        "id":"7",
        "title":"Comment créer son premier site web?",
        "category":"Développement"
    },
    {
        "id":"8",
        "title":"Le basketball Africain est-il en pleine évolution?",
        "content":"",
        "category":"Sport"
    },
    {
        "id":"9",
        "title":"5 habitudes pour améliorer sa productivité",
        "content":"",
        "category":"Développement personnel"
    },
    {
        "id":"10",
        "title":"Pour quoi apprendre l'anglais aujourd'hui?",
        "content":"",
        "category":"Education"
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
        if q.lower() in article['title'].lower():
            results.append(article)

    context={
        'query':q,
        'articles':results
    }

    return render(request,'search.html',context)