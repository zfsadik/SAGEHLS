# Handler functions for specific node types
def handle_function_definition(node, source_code, depth):
    indent = '  ' * depth
    # print(f'{indent}FunctionDefinition')
    # Process return type
    return_type_node = node.child_by_field_name('type')
    if return_type_node:
        handle_node(return_type_node, source_code, depth + 1)
    # Process function name
    declarator_node = node.child_by_field_name('declarator')
    if declarator_node:
        # handle_node(declarator_node, source_code, depth + 1)
        handle_node(declarator_node, source_code, depth )
    # Process function body
    body_node = node.child_by_field_name('body')
    if body_node:
        # print(f'{indent}Body:')
        traverse(body_node, source_code, depth + 1)
        

def handle_function_declarator(node, source_code, depth):
    indent = '  ' * depth
    function_name = node.child_by_field_name('declarator').text.decode('utf-8')
    
    parameters_node = node.child_by_field_name('parameters')
    if parameters_node and parameters_node.text.decode('utf-8') != '()':
        parameter_types = []
        for param in parameters_node.children:
            if param.type == 'parameter_declaration':
                param_type = param.child_by_field_name('type').text.decode('utf-8')
                parameter_types.append(param_type)
        print(f'FuncName: {function_name}, {indent}Params: {", ".join(parameter_types)}')
    else:
        print(f'{indent}FuncName: {function_name}')
def handle_parameter_declaration(node, source_code, depth):
    indent = '  ' * depth
    param_text = node.text.decode('utf-8')
    print(f'{indent}Parameter: {param_text}')

def handle_declaration(node, source_code, depth):
    indent = '  ' * depth
    var_type = node.child_by_field_name('type').text.decode('utf-8')
    # var_name = node.child_by_field_name('declarator')
    # print(var_name)
    # print(f'{indent}DeclarationStatement')
    if node.child_by_field_name('declarator').type == 'function_declarator':
        # handle_function_declarator(node.child_by_field_name('declarator'), source_code, depth)
        traverse(node, source_code, depth)
    else:
        print(f'{indent}VarTyp: {var_type} ')

# def handle_expression_statement(node, source_code, depth):
#     indent = '  ' * depth
#     # print(node.text.decode('utf-8'))
#     expression = node.child(0)
#     if expression.type == 'call_expression':
#         function_name = expression.child_by_field_name('function').text.decode('utf-8')
#         # print(f'{indent}ExpressionStatement')
#         # print(f'{indent}FuncCall: {function_name}')
#         arguments_node = expression.child_by_field_name('arguments')
#         arguments = ""
 
#         if arguments_node:
#             arguments = arguments_node.text.decode('utf-8').strip()
#             # Check if the argument is empty string
#             if arguments == "()":
#                 arguments = ""
#         print(f'{indent}FuncCall: {function_name}, Args: {arguments}')
    
#     elif expression.type == 'assignment_expression':
#         left = expression.child_by_field_name('left').text.decode('utf-8')
#         right = expression.child_by_field_name('right').text.decode('utf-8')
#         # print(f'{indent}ExpressionStatement')
#         print(f'{indent}Asgnmnt: {left}= {right}')
    
#     elif expression.type == 'update_expression':
#         handle_update_expression(expression, source_code, depth)

def handle_if_statement(node, source_code, depth):
    indent = '  ' * depth
    condition = node.child_by_field_name('condition').text.decode('utf-8')
    print(f'{indent}IfStmt: Contn: {condition}')
    consequence_node = node.child_by_field_name('consequence')
    if consequence_node:
        print(f'{indent} Then:')
        # for child in consequence_node.children:
        #     print(child.type)

        traverse(consequence_node, source_code, depth + 1)
    alternative_node = node.child_by_field_name('alternative')
    if alternative_node:
        print(f'{indent} Else:')
        traverse(alternative_node, source_code, depth + 2)

def handle_update_expression(node, source_code, depth):
    indent = '  ' * depth

    print(f'{indent}Operation: {node.text.decode("utf-8")}')
    
def handle_preproc_include(node, source_code, depth):
    indent = '  ' * depth
    # Extract the text of the include directive
    path = node.child_by_field_name('path').text.decode('utf-8')
    print(f'{indent}IncludeDirective: {path}')

def handle_for_statement(node, source_code, depth):
    indent = '  ' * depth
    # print(f'{indent}ForStmt:')
    intializer_text = ""
    condition_text = ""
    update_text = ""
    
    # Extract and print the initializer
    initializer_node = node.child_by_field_name('initializer')
    if initializer_node:
        # print(f'{indent}Initializer: {initializer_node.text.decode("utf-8")}')
        intializer_text = initializer_node.text.decode("utf-8")
        
    
    # Extract and print the condition
    condition_node = node.child_by_field_name('condition')
    if condition_node:
        condition_text = source_code[condition_node.start_byte:condition_node.end_byte].strip()
        # print(f'{indent}Condition: {condition_text}')

    
    # Extract and print the update expression
    update_node = node.child_by_field_name('update')
    if update_node:
        update_text = source_code[update_node.start_byte:update_node.end_byte].strip()
        # print(f'{indent}Update: {update_text}')
    
    print(f'{indent}ForStmt-> init: {intializer_text}, cond: {condition_text}, updt: {update_text}')
    # Extract and print the body of the for loop
    body_node = node.child_by_field_name('body')
    
    if body_node:
        # print(f'{indent}Body:')
        handle_node(body_node, source_code, depth + 1)
        # traverse(body_node, source_code, depth + 1)


def handle_while_statement(node, source_code, depth):
    indent = '  ' * depth
    # print(f'{indent}WhileStatement:')
    
    # Extract and print the condition
    condition_node = node.child_by_field_name('condition')
    
    condition_text = source_code[condition_node.start_byte:condition_node.end_byte].strip()
    print(f'{indent}WhileStmt Cond: {condition_text}')
    
    # Extract and print the body of the while loop
    body_node = node.child_by_field_name('body')
    if body_node:
        print(f'{indent} Body:')
        traverse(body_node, source_code, depth + 2)


def handle_update_expression(node, source_code, depth):
    indent = '  ' * depth
    print(f'{indent}Update: {node.text.decode("utf-8")}')


def handle_return_statement(node, source_code, depth):
    indent = '  ' * depth
    
    
    
    if node.child_by_field_name('identifier'):
        identifier_node = node.child_by_field_name('identifier')
        print(f'{indent}Return: {identifier_node.text.decode("utf-8")}')
    elif not node.child_by_field_name('call_expression'):
        print(f'{indent}Return: {node.text.decode("utf-8")}')
    
    else:
        print(f'{indent}Return:')
        traverse(node, source_code, depth + 1)
    
    # if expression_node:
    #     expression_text = source_code[expression_node.start_byte:expression_node.end_byte].decode('utf-8').strip()
    #     print(f'{indent}Value: {expression_text}')
    # else:
    #     print(f'{indent}Value: None')

def handle_call_expression(node, source_code, depth):
    indent = '  ' * depth
    # print(f'{indent}CallExpression:')
    
    # Extract and print the function being called
    function_node = node.child_by_field_name('function')
    if function_node:
        function_text = source_code[function_node.start_byte:function_node.end_byte].strip()
        print(f'{indent}Function: {function_text}')
    
    # Extract and print the arguments
    arguments_node = node.child_by_field_name('arguments')
    if arguments_node:
        print(f'{indent}Arguments: {arguments_node.text.decode("utf-8")}')
        
def handle_preproc_def(node, source_code, depth):
    # print(depth)
    indent = '  ' * depth
    # print(f'{indent}Define:')
    
    # Extract and print the macro name
    macro_name_node = node.child_by_field_name('name')
    macro_name = macro_name_node.text.decode('utf-8')
       
    
   
    macro_value_node = node.child_by_field_name('value')

    macro_value = macro_value_node.text.decode('utf-8')
    
    print(f'{indent}Define: {macro_name}{macro_value}')
       
def handle_preproc_call(node, source_code, depth):
    indent = '  ' * depth

    arguments_node = node.child_by_field_name('argument')
    if arguments_node:
        print(f'{indent}PrePocCall {arguments_node.text.decode("utf-8")}')
        

def handle_switch_statement(node, source_code, depth):
    indent = '  ' * depth
    print(f'{indent}SwitchStatement:')
    
    # Extract and print the condition
    condition_node = node.child_by_field_name('condition')
    if condition_node:
        condition_text = source_code[condition_node.start_byte:condition_node.end_byte].strip()
        print(f'{indent}Condition: {condition_text}')
    
    # Extract and print the body of the switch statement
    body_node = node.child_by_field_name('body')
    if body_node:
        # print(f'{indent}Body:')
        for child in body_node.children:
            if child.type in ['case_statement', 'default_statement']:
                print(f'{indent}For {child.child_by_field_name('value').text.decode('utf-8') if child.child_by_field_name('value') else ''}:')
                traverse(child, source_code, depth + 2)

def handle_call_expression(expression, source_code, depth):
    indent = '  ' * depth
    function_node = expression.child_by_field_name('function')
    if function_node:
        function_name = source_code[function_node.start_byte:function_node.end_byte].strip()
        arguments_node = expression.child_by_field_name('arguments')
        arguments = ""
        if arguments_node:
            arguments = source_code[arguments_node.start_byte:arguments_node.end_byte].strip()
            # Check if the argument is an empty string
            if arguments == "()":
                arguments = ""
        print(f'{indent}FuncCall: {function_name}, Args: {arguments}')
def handle_assignment_expression(expression, source_code, depth):
    indent = '  ' * depth
    left_node = expression.child_by_field_name('left')
    right_node = expression.child_by_field_name('right')
    if left_node and right_node:
        left = source_code[left_node.start_byte:left_node.end_byte].strip()
        right = source_code[right_node.start_byte:right_node.end_byte].strip()
        print(f'{indent}Asgnmnt: {left} = {right}')
def handle_update_expression(expression, source_code, depth):
    indent = '  ' * depth
    operator = source_code[expression.start_byte:expression.end_byte].strip()
    if '++' in operator:
        print(f'{indent}Increment: {operator}')
    elif '--' in operator:
        print(f'{indent}Decrement: {operator}')


def handle_node(node, source_code, depth):
    handlers = {
        'function_definition': handle_function_definition,
        'function_declarator': handle_function_declarator,
        'parameter_declaration': handle_parameter_declaration,
        'declaration': handle_declaration,
        # 'expression_statement': handle_expression_statement,
        'if_statement': handle_if_statement,
        'update_expression': handle_update_expression,
        # 'preproc_include': handle_preproc_include,
        'for_statement': handle_for_statement,
        'return_statement': handle_return_statement,
        'call_expression': handle_call_expression,
        # 'preproc_def': handle_preproc_def,
        # 'preproc_call': handle_preproc_call,
        'switch_statement': handle_switch_statement,
        'while_statement': handle_while_statement,
        'call_expression': handle_call_expression,
        'assignment_expression': handle_assignment_expression,
        'update_expression': handle_update_expression,


       
        # Add more handlers as needed
    }
    handler = handlers.get(node.type)
    if handler:
        handler(node, source_code, depth)
    else:
        # Default action for unhandled node types
        traverse(node, source_code, depth)
        

# Generic traversal function
def traverse(node, source_code, depth=0):
    for child in node.children:
        # print(child.type)
        handle_node(child, source_code, depth)