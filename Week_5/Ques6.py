import textwrap

text = """    
        This is an indented paragraph.
            It has inconsistent indentation.
        Let's remove all indentation!
"""
dedented_text = textwrap.dedent(text)

print("Text after removing indentation:\n")
print(dedented_text)
