f = open('nginx_logs_head.txt', 'r', encoding='utf-8')

# file_data = f.read().splitlines()

# for row in file_data:
#     row = row.strip()
#     print(row)

for row in f.read().splitlines():
    print(row)

print(f.closed)
f.close()
print(f.closed )
