from django.shortcuts import render

def render_template_example(request):
    data = { 
            "field": "field_data",
            "nested": {
                "data1": "nested_data1",
                "data2": "nested_data2",
            }
        }
    return render(request, 'test.html', data)



