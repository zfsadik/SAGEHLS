from tree_sitter import Language, Parser
import tree_sitter_languages
from handlers import traverse
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# Load the C++ language
CPP_LANGUAGE = tree_sitter_languages.get_language('cpp')

# Initialize the parser with the C++ language
parser = Parser()
parser.set_language(CPP_LANGUAGE)

# Read the C++ code from a file
with open("temp.cpp", "r", encoding="utf-8") as f:
    cpp_code = f.read()

# Parse the source code
tree = parser.parse(bytes(cpp_code, "utf8"))

# Start traversing from the root node
root_node = tree.root_node
traverse(root_node, cpp_code)