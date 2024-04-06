import yaml
from jinja2 import Environment, FileSystemLoader

if __name__ == "__main__":
    # yaml = YAML()
    config_data = yaml.load(open('./j3.yaml'), Loader=yaml.FullLoader)
    # print(config_data)
    
    # Load templates file from templtes folder 
    env = Environment(loader = FileSystemLoader('./templates'),   trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('j3_tmpl.py')
    print(template.render(config_data))