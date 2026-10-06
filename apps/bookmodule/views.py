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