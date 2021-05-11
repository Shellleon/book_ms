from django.urls import path

from app01 import views

urlpatterns = [
    # http://127.0.0.1:8000/app01/add_publisher/
    # 增加出版社
    path('add_publisher/', views.add_publisher),
    # 列出所有出版社
    path('publisher_list/', views.publisher_list),
    # 编辑出版社
    path('edit_publisher/', views.edit_publisher),
    # 删除出版社
    path('delete_publisher/', views.delete_publisher),
    # 分页
    # path('book/', views.book,name='book'),
    # path('list/', views.display_obj),

    # 书籍
    # 展示所有数据
    # http://127.0.0.1:8000/app01/book_list/
    path('book_list/', views.book_list),
    path('add_book/', views.add_book),
    path('edit_book/', views.edit_book),
    path('delete_book/', views.delete_book),

    # 作者
    # 展示所有数据
    path('author_list/', views.author_list),
    path('add_author/', views.add_author),
    path('edit_author/', views.edit_author),
    path('delete_author/', views.delete_author),
]
