from jinja2 import Template

tmpl = Template("hello {{ name }}") # 定义模版

ret = tmpl.render(name="jinja2")    # 根据模版生成最终结果

print(ret)