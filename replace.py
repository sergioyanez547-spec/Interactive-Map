import sys

file_path = r'c:\Users\Isaac\OneDrive\Exercises\paginaBoot\css\styles.css'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace hex primary (orange) with teal
text = text.replace('#f4623a', '#6fb995')
text = text.replace('#F4623A', '#6fb995')

# Replace RGB primary
text = text.replace('244, 98, 58', '111, 185, 149')

# Replace hex darker hover
text = text.replace('#c34e2e', '#599477')
text = text.replace('#C34E2E', '#599477')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Colors replaced successfully in css/styles.css')
