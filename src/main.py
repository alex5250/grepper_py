import sys
from parse import Parse_From_web
from config import Config
import argparse
config_class=Config()

def parse_website(title,lang):
    parse_from_web=Parse_From_web()

    suffix_url=config_class.get_value_from_config('URL','base_url_suffix')
    element_id=config_class.get_value_from_config('URL','element_id')
    output=parse_from_web.make_search(title,lang,suffix_url,element_id)
    parse_from_web.pretty_Print(output)
pass

chrome_warring=config_class.get_value_from_config('CLI','chrome_installed_warring')
if chrome_warring=="on":
    print("This project relays on Chrome installed on machine. Please install")
    config_class.set_value_from_config("CLI",'chrome_installed_warring','off')
    sys.exit(0)
else:
    print("All fine!")


parser = argparse.ArgumentParser()
parser.add_argument('--title', help='title of the problem')
parser.add_argument('--lang', help='programming language')
args = parser.parse_args()
parse_website(args.title,args.lang)








