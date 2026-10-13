from django.shortcuts import render

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