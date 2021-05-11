from django.shortcuts import render, redirect
from app01 import models

# Create your views here.
# 分页
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger


# 图书分页
# def display_obj(request):
#     # 惰性查询
#     book_obj_list = models.Book.objects.all()
#     # 得到paginator对象(data列表,每页5个数据)
#     page_obj = Paginator(book_obj_list, 5)
#     print('数据总数', page_obj.count)
#     print('总页数', page_obj.num_pages)
#     print('页码列表', page_obj.page_range)
#
#     page1 = page_obj.page(1)
#     for i in page1:
#         print(i)
#     print(page1.object_list)
#     page2 = page_obj.page(2)
#
#     print(page2.has_previous())
#     print(page2.has_next())
#     print(page2.next_page_number())
#     print(page2.previous_page_number())
#
#     # 从查询字符串中得到具体的页码(一般从1开始)
#     page_num = request.GET.get('page', 1)  # 得到默认的当前页   # 取出具体的某一页数据
#     # cur_page = request.GET.get('page')  # 得到默认的当前页   # 取出具体的某一页数据
#
#     try:
#         current_page_num = int(page_num)
#         # 获取当前页的数据对象page_of_books
#         page_num_data = page_obj.page(current_page_num)
#     except PageNotAnInteger:
#         current_page_num = 1
#         page_num_data = page_obj.page(current_page_num)
#     except EmptyPage:
#         current_page_num = page_obj.num_pages
#         page_num_data = page_obj.page(current_page_num)
#     except Exception:
#         current_page_num = 1
#         page_num_data = page_obj.page(current_page_num)
#
#     book_objs = page_num_data
#     # return render(request, 'index.html', locals())
#     return render(request, 'index.html',
#                   {"book_objs": book_objs,
#                    "current_page_num": current_page_num,
#                    "page_obj": page_obj})


# publisher view
def add_publisher(request):
    """
    添加出版社
    :param request: POST请求
    :return: 出版社页面
    """
    if request.method == "POST":
        publisher_name = request.POST.get('name')
        publisher_address = request.POST.get('address')
        # 保存到数据库中
        models.Publisher.objects.create(name=publisher_name, address=publisher_address)
        return redirect("/app01/publisher_list")
    return render(request, "add_publisher.html")


def publisher_list(request):
    # 获取所有数据
    publisher_list = models.Publisher.objects.all()
    return render(request, "publisher_list.html", {"publisher_obj_list": publisher_list})


def edit_publisher(request):
    if request.method == "POST":
        # 1.获取表单提交过来的数据
        id = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        # 根据id 去数据库查找对象
        publisher_obj = models.Publisher.objects.get(id=id)
        # 修改数据
        publisher_obj.name = name
        publisher_obj.address = address
        publisher_obj.save()
        # 重定向到出版社列表
        return redirect('/app01/publisher_list/')

    elif request.method == "GET":
        # 获取id
        id = request.GET.get('id')
        # 去数据库中查找相应的数据
        publisher_obj = models.Publisher.objects.get(id=id)
        publisher_obj_list = models.Publisher.objects.all()

        # 返回页面
        return render(request, "edit_publisher.html",
                      {"publisher_obj": publisher_obj,
                       "publisher_obj_list": publisher_obj_list})


def delete_publisher(request):
    # 获取要删除的出版社id
    id = request.GET.get('id')
    # 根据id删除数据库中的记录
    models.Publisher.objects.filter(id=id).delete()
    return redirect("/app01/publisher_list/")


# # book view
# def book_list(request):
#     # 获取图书信息
#     book_obj_list = models.Book.objects.all()
#     # 将数据返回到页面上
#     return render(request, "book_list.html", {"book_obj_list": book_obj_list})
# book view
def book_list(request):
    book_obj_list = models.Book.objects.all()
    # 得到paginator对象(data列表,每页5个数据)
    page_obj = Paginator(book_obj_list, 5)
    print('数据总数', page_obj.count)
    print('总页数', page_obj.num_pages)
    print('页码列表', page_obj.page_range)

    page1 = page_obj.page(1)
    for i in page1:
        print(i)
    print(page1.object_list)
    page2 = page_obj.page(2)

    print(page2.has_previous())
    print(page2.has_next())
    print(page2.next_page_number())
    print(page2.previous_page_number())

    # 从查询字符串中得到具体的页码(一般从1开始)
    page_num = request.GET.get('page', 1)  # 得到默认的当前页   # 取出具体的某一页数据
    # cur_page = request.GET.get('page')  # 得到默认的当前页   # 取出具体的某一页数据

    try:
        current_page_num = int(page_num)
        # 获取当前页的数据对象page_of_books
        page_num_data = page_obj.page(current_page_num)
    except PageNotAnInteger:
        current_page_num = 1
        page_num_data = page_obj.page(current_page_num)
    except EmptyPage:
        current_page_num = page_obj.num_pages
        page_num_data = page_obj.page(current_page_num)
    except Exception:
        current_page_num = 1
        page_num_data = page_obj.page(current_page_num)

    book_objs = page_num_data
    # return render(request, 'index.html', locals())
    return render(request, 'book_list.html',
                  {"book_objs": book_objs,
                   "current_page_num": current_page_num,
                   "page_obj": page_obj})


"""
django 使用ORM插入数据,提示
Cannot assign "1": "B" must be a "xxxx类" instance.

这是因为使用了外键导致的，
如果使用了外键，先实例化外键查询，然后在插入的表里面放入实例化后的外键连接

# 解决方案
# 先实例化外键查询
book_publisher_name = models.Publisher.objects.get(id=1)
# 保存到数据库中
models.Book.objects.create(publisher=book_publisher_name)

"""


# 添加图书方法一
# def add_book(request):
#     if request.method == "POST":
#         book_name = request.POST.get('name')
#         book_price = request.POST.get('price')
#         book_inventory = request.POST.get('inventory')
#         book_sale_num = request.POST.get('sale_num')
#         # 进行出版社名称的处理（需要先实例化外键）
#         # book_publisher_name= models.Book.publisher
#         book_publisher_name = models.Publisher.objects.get(id=1)
#         # book_publisher_name=request.POST.get('publisher')
#         # 保存到数据库中
#         models.Book.objects.create(name=book_name, price=book_price,
#                                    inventory=book_inventory,
#                                    sale_num=book_sale_num,
#                                    publisher=book_publisher_name)
#
#         return redirect("/app01/book_list/")
#     return render(request, "add_book.html")

# 添加图书方法二
def add_book(request):
    if request.method == "POST":
        # 1.获取前端提交过来的内容
        name = request.POST.get('name')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        sale_num = request.POST.get('sale_num')
        publisher_id = request.POST.get('publisher_id')
        # 2.将数据保存到数据库中
        models.Book.objects.create(name=name, price=price,
                                   inventory=inventory,
                                   sale_num=sale_num,
                                   publisher_id=publisher_id)
        # 3.重定向到图书列表页面
        return redirect("/app01/book_list/")
    else:
        # 获取所有出版社
        publisher_obj_list = models.Publisher.objects.all()

        return render(request, "add_book.html", {"publisher_obj_list": publisher_obj_list})


def edit_book(request):
    if request.method == "GET":

        # 1.首先获取id，get请求
        id = request.GET.get('id')
        # 2.在数据库中查找相应的数据
        book_obj = models.Book.objects.filter(id=id).first()
        # 3.查找所有出版社
        publisher_list = models.Publisher.objects.all()
        # 返回页面
        # book_obj相当于将图书数据渲染到前端
        # publisher_list相当于将所有出版社数据渲染到前端
        return render(request, "edit_book.html",
                      {"book_obj": book_obj, "publisher_list": publisher_list})
    else:
        # 获取前端提交的数据
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        sale_num = request.POST.get('sale_num')
        publisher_id = request.POST.get('publisher_id')
        # 2.查询数据库进行更新
        models.Book.objects.filter(id=id).update(name=name, price=price,
                                                 inventory=inventory,
                                                 sale_num=sale_num,
                                                 publisher_id=publisher_id)
        # 重定向到book_list
        return redirect("/app01/book_list")


def delete_book(request):
    # 首先获取id，get请求
    id = request.GET.get('id')
    # 删除数据
    models.Book.objects.get(id=id).delete()
    # 返回重定向
    return redirect("/app01/book_list")


# author view
# def author_list(request):
#     """
#     展示作者列表
#     :param request:
#     :return:
#     """
#     # 获取所有作者信息
#     ret_list = []  # 新建作者对应图书的列表
#     # 从数据库中获取作者的所有信息
#     author_obj_list = models.Author.objects.all()
#     for author_obj in author_obj_list:
#         # 获取所有书籍信息
#         book_obj_list = author_obj.book.all()
#         res_dict = {}  # 新建作者对象字典
#         # 给字典赋值
#         res_dict['author_obj'] = author_obj
#         res_dict['book_list'] = book_obj_list
#         # 将res_dict 添加到 ret_list中
#         ret_list.append(res_dict)
#     # 返回响应
#     return render(request, "author_list.html", {"ret_list": ret_list})


# 作者分页
def author_list(request):
    # 获取所有作者信息
    ret_list = []  # 新建作者对象信息列表
    # 惰性查询
    author_obj_list = models.Author.objects.all()
    for author_obj in author_obj_list:
        # 获取所有书籍信息
        book_obj_list = author_obj.book.all()
        res_dict = {}  # 新建作者对象字典
        # 给字典赋值
        res_dict['author_obj'] = author_obj
        res_dict['book_list'] = book_obj_list
        # 将res_dict 添加到 ret_list中
        ret_list.append(res_dict)
    # ret_list = [{'author_obj':author_obj,'book_list':book_obj_list},res_dict[1]...]

    # 分页
    # 得到 page_obj 对象(data列表,每页5个数据)
    # page_obj = Paginator(ret_list, 5)
    page_obj = Paginator(author_obj_list, 5)
    # print(page_obj)
    # print('数据总数', page_obj.count)
    # print('总页数', page_obj.num_pages)
    # print('页码列表', page_obj.page_range)
    #
    # page1 = page_obj.page(1)
    # for i in page1:
    #     print(i)
    # print(page1.object_list)
    # page2 = page_obj.page(2)
    #
    # print(page2.has_previous())
    # print(page2.has_next())
    # print(page2.next_page_number())
    # print(page2.previous_page_number())

    # 从查询字符串中得到具体的页码(一般从1开始)
    page_num = request.GET.get('page', 1)  # 得到默认的当前页   # 取出具体的某一页数据

    try:
        current_page_num = int(page_num)
        # 获取当前页的数据对象page_of_books
        page_num_data = page_obj.page(current_page_num)
    except PageNotAnInteger:
        current_page_num = 1
        page_num_data = page_obj.page(current_page_num)
    except EmptyPage:
        current_page_num = page_obj.num_pages
        page_num_data = page_obj.page(current_page_num)
    except Exception:
        current_page_num = 1
        page_num_data = page_obj.page(current_page_num)

    author_objs = page_num_data
    return render(request, 'author_list.html',
                  {"ret_list":ret_list,
                   #
                   "author_objs": author_objs,
                   })
    # return render(request, 'author_list.html',
    #               {"author_objs": author_objs,
    #                "current_page_num": current_page_num,
    #                "page_obj": page_obj,
    #                "ret_list":ret_list})


def add_author(request):
    if request.method == "GET":
        # 1.获取所有图书
        book_obj_list = models.Book.objects.all()
        print(book_obj_list)
        # 2.返回页面
        return render(request, "add_author.html", {"book_obj_list": book_obj_list})
    else:  # POST
        # 1.获取数据
        name = request.POST.get('name')
        email = request.POST.get('email')
        book_ids = request.POST.getlist('books')
        # 2.新建数据，写入数据库
        author_obj = models.Author.objects.create(name=name, email=email)  # 创建对象
        author_obj.book.set(book_ids)  # 设置关系
        # 3.重定向到列表页面
        return redirect('/app01/author_list/')


def edit_author(request):
    if request.method == "GET":
        # 获取id
        id = request.GET.get('id')
        # 获取对象和所有图书
        author_obj = models.Author.objects.get(id=id)
        book_obj_list = models.Book.objects.all()
        # 将所有数据渲染回页面
        return render(request, "edit_author.html",
                      {"author_obj": author_obj, "book_obj_list": book_obj_list})
    else:
        # 保存修改的数据
        # 1.获取数据
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        book_ids = request.POST.getlist('books')
        # 根据id查找对象，并修改
        author_obj = models.Author.objects.filter(id=id).first()
        author_obj.name = name
        author_obj.email = email
        author_obj.book.set(book_ids)  # 设置字段关联（作者id和book_id的关联关系）
        author_obj.save()
        # 重定向到作者列表
        return redirect("/app01/author_list/")


def delete_author(request):
    # 1.获取id
    id = request.GET.get('id')
    # 删除作者
    models.Author.objects.filter(id=id).delete()
    # 重定向到作者列表
    return redirect("/app01/author_list/")
