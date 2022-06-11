from django.shortcuts import render

# Create your views here.
def counter(request):
    ct = request.session.get('count', 0)
    new_count = ct +1
    request.session['count'] = new_count
    return render(request, "counter/count.html",{'new_count':new_count})