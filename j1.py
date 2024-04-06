import jinja2
environment = jinja2.Environment()
template = environment.from_string("Hello, {{ name }}!")
print(template.render(name="World"))

# The core component of Jinja is the Environment() class. 
# In this example, you create a Jinja environment without any arguments. 
# Later you’ll change the parameters of Environment to customize your environment. 
# Here, you’re creating a plain environment where you load the string "Hello, {{ name }}!" as a template.