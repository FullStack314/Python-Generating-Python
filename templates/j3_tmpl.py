{%- for country in countries -%} 
if {{ country['name'] }}:
    print({{ country['capital'] }})
    return {{ country['capital'] }}
{% endfor %}