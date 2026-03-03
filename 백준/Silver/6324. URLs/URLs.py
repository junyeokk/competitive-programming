n = int(input())

# ftp://acm.baylor.edu:1234/pub/staff/mr-p
for i in range(n):
    s = input()
    parts_p = s.split("://", 1)
    parts_h = parts_p[1].split("/")
    parts_po = parts_h[0].split(":")
    parts_pa = parts_p[1].split("/")

    protocol = parts_p[0]
    host = parts_po[0]
    if len(parts_po) == 1:
        port = '<default>'
    else:
        port = parts_po[1]
    if len(parts_pa) == 1:
        path = '<default>'
    else:
        path = "/".join(parts_pa[1:])
        if path == '':
            path = '<default>'


    print(f"URL #{i + 1}")
    print("Protocol =", protocol)
    print("Host     =", host)
    print("Port     =", port)
    print("Path     =", path)
    print()