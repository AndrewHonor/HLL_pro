@use_args({"first_name": fields.Str(required=False), "last_name": fields.Str(required=False),
           "search": fields.Str(required=False)}, location='query')
def get_students(request, params):
    students = Student.objects.all()
    search_fields = ["first_name", "last_name", "email"]

    for key, value in params.items():
        if key == "search":
            query = Q()
            for field in search_fields:
                query |= Q(**{f"{field}__contains": value})
            students = students.filter(query)
        else:
            students = students.filter(**{key: value})
    return render(request, template_name='students/list.html', context={'students': students})
