urlpatterns = [
    path('farms', FarmListView.as_view(), name='farm-list'),
    path('farms/<int:pk>', FarmDetailView.as_view(), name='farm-details'),
]