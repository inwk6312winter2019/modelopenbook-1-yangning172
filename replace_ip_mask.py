def replace_ip_mask(a1,a2,a3,n1,n2,n3,file1,file2):
    f1 = open(file1)
    f2 = open(file2)
    a1 = '192'
    a2 = '172'
    a3 = '10'
    n1 = '255.255.0.0'
    n2 = '255.255.255.0'
    n3 = '255.0.0.0'
    for line in f1:
    if s1 in line:
      newline = line.replace(s1,s3)
      if net1 in line:
        newline = newline.replace(net1,net3)
      elif net2 in line:
        newline = newline.replace(net2,net3)
      f2.write(newline)
    elif s2 in line:
      newline = line.replace(s2,s3)
      if net1 in line:
        newline = newline.replace(net1,net3)
      elif net2 in line:
        newline = newline.replace(net2,net3)
      f2.write(newline)
    else:
      f2.write(line)

      
    
