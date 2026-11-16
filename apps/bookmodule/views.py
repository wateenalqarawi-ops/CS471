from django.shortcuts import render
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Address, Student, Publisher, Author
from django.db.models import Sum
from django.db.models import Min

# 1. الدالة الخاصة بالصفحة الرئيسية للموقع (Home Page)
def index(request):
    return render(request, "bookmodule/index.html")

# 2. الدالة الخاصة بصفحة عرض قائمة الكتب (List of Books)
def list_books(request):
    return render(request, 'bookmodule/list_books.html')

# 3. الدالة الخاصة بصفحة تفاصيل كتاب محدد (Show One Book)
# تم وضع bookId=1 كقيمة افتراضية لضمان عدم حدوث خطأ عند فتح الصفحة مباشرة
def viewbook(request, bookId=1):
    return render(request, 'bookmodule/one_book.html')

# 4. الدالة الخاصة بصفحة معلومات عنا (About Us)
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})


def links_view(request):
    return render(request, 'bookmodule/links.html')


def text_formatting(request):
    return render(request, 'bookmodule/formatting.html')


def listing_view(request):
    return render(request, 'bookmodule/listing.html')


def tables_view(request):
    return render(request, 'bookmodule/tables.html')


from django.shortcuts import render

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search_view(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): 
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained: 
                newBooks.append(item)
                
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
        
    return render(request, 'bookmodule/search.html')


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def lab8_task1(request):
    books = Book.objects.filter(price__lte=80) # أو باستخدام Q: Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task2(request):
    books = Book.objects.filter(edition__gt=3).filter(Q(title__icontains='co') | Q(author__icontains='co'))
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(~Q(edition__gt=3) & ~Q(title__icontains='co') & ~Q(author__icontains='co'))
    return render(request, 'bookmodule/bookList.html', {'books': books})


def lab8_task4(request):
    books = Book.objects.order_by('title') # أو order_by('-title') للعكس
    return render(request, 'bookmodule/bookList.html', {'books': books})


def lab8_task5(request):
    aggregations = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'aggregations': aggregations})



from .models import Student

def lab8_task7(request):
    students_per_city = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'data': students_per_city})

def lab9_task1(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})


def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})



def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})


from django.db.models import Count, Q

def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4))
    )
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})



def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books_count=Count(
            'book', 
            filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__quantity__gte=1)
        )
    )
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})