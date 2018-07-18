from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'item'

urlpatterns = [
    url(r'^doget/(?P<param1>.*)$', views.doget_execute, name='item_doget'),
    url(r'^red/$', views.showredirect),
    url(r'^red2/$', views.showredirect2),
    url(r'^red3/$', views.showredirect3),
    url(r'^dg/(?P<param1>.*)/$', views.doget_execute, name='doget'),
    url(r'^child/$', views.showchild),
    url(r'^post_e/$', views.dopost_execute, name='post_e'),
    url(r'^input/$', views.show_input),
    url(r'^input_e/$', views.show_inputerr),
    url(r'^$', views.SampleTemplateView.as_view()),
    url(r'^index/$', TemplateView.as_view(template_name='html/index.html')),
    url(r'^list1/$', views.ItemModelListView.as_view()),
    url(r'^list2/$', views.ItemQueryListView.as_view()),
    url(r'^name/([\w-]+)/$', views.ItemNameListView.as_view()),
    url(r'^list/(?P<pk>[\d]+)/$', views.ItemDetailView.as_view()),
    url(r'^form/$', views.dopost_view),
    url(r'^conf/$', views.confirm),
    url(r'^thanks/$', TemplateView.as_view(template_name='html/thanks.html'), name='thanks'),
    url(r'^f_view/$', views.InputFormView.as_view()),
    url(r'^item_f/$', views.ItemFormView.as_view()),
]