import pandas as pd
import subprocess

codes_df = pd.read_csv('merged_output.csv')

# Add new column to store the AST

codes_df['hls_ast'] = None

for i in range(len(codes_df)):
    # Print the index and flash on the same line
    print(f"\rIndex: {i}", end="")

    code = codes_df.iloc[i]['hls_code']
    print(code)
    with open("temp.cpp", "w", encoding="utf-8") as f:
        f.write(code)
    
    # Generate the AST with code_parser.py and capture the output but dont print it
    output = subprocess.run(['python3', 'code_parser.py'],capture_output=True, text=True)
    ast = output.stdout

    codes_df.at[i, 'hls_ast'] = ast 

    # delete the temp.cpp file
    subprocess.run(['rm', 'temp.cpp'])
    

codes_df.to_csv('merged_output_ast.csv', index=False)

    