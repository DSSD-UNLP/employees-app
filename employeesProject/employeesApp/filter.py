class EmployeeFilter(object):
    def __init__(self, queryset, request):
        self.queryset = queryset
        self.request = request
        self.valid_orders = ['firstname', 'surname', 'email']

    def employees(self):
        order = 'firstname'
        if self.request.GET.get('order') != None:
            tmp_order = self.request.GET.get('order')
            if tmp_order in self.valid_orders:
                order = tmp_order
        if self.request.GET.get('firstname') != None:
            self.queryset = self.queryset.filter(firstname__contains = (self.request.GET.get('firstname')).strip())
        if self.request.GET.get('surname') != None:
            self.queryset = self.queryset.filter(surname__contains = (self.request.GET.get('surname')).strip())
        if self.request.GET.get('email') != None:
            self.queryset = self.queryset.filter(email__contains = (self.request.GET.get('email')).strip())
        if self.request.GET.get('type') != None:
            self.queryset = self.queryset.filter(employeeType = (self.request.GET.get('type')).strip())
        return self.queryset.order_by(order)

class TypeFilter(object):
    def __init__(self, queryset, request):
        self.queryset = queryset
        self.request = request

    def types(self):
        if self.request.GET.get('name') != None:
            self.queryset = self.queryset.filter(name__contains = (self.request.GET.get('name')).strip())
        if self.request.GET.get('description') != None:
            self.queryset = self.queryset.filter(description__contains = self.request.GET.get('description'))
        return self.queryset.order_by('name')