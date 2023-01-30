from django.urls import path
from app23 import views
urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('student',views.student,name='student'),
    path('teacher',views.teacher,name='teacher'),
    path('studreg',views.studreg,name='studreg'),
    # path('bookdetail',views.book_detail,name='bookdetail'),
    path('fine',views.pay_fine,name='fine'),
    path('teachreg',views.teach_reg,name='teachreg'),
    path('studpending',views.studpending,name='studpending'),
    path('teachpending',views.teachpending,name='teachpending'),
    path('approvedstud',views.approvedstud,name='approvedstud'),
    path('stud_approve/<int:reg_id>/',views.stud_approve,name='stud_approve'),
    path('stud_reject/<int:reg_id>/',views.stud_reject,name='stud_reject'),
    path('approvedteach',views.approvedteach,name='approvedteach'),
    path('teach_approve/<int:reg_id>/',views.teach_approve,name='teach_approve'),
    path('teach_reject/<int:reg_id>/',views.teach_reject,name='teach_reject'),
    path('studdelete/<int:reg_id>/',views.stud_delete,name='studdelete'),
    path('teachdelete/<int:reg_id>/',views.teach_delete,name='teachdelete'),
    path('book',views.book,name='book'),
    path('viewbook',views.viewbook,name='viewbook'),
    path('admin_request',views.admin_request,name='admin_request'),
    path('viewstud',views.viewstud,name='viewstud'),
    path('teach_book',views.teach_book,name='teach_book'),
    path('pay_fine',views.pay_fine,name='pay_fine'),
    path('viewfine',views.viewfine,name='viewfine'),

]