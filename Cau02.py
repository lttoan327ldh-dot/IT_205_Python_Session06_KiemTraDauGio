
total_faulty_product = 0

while True: 
    faulty_product = int(input("Nhập số lượng hàng lỗi của quầy: "))
    if faulty_product >= 0:
        total_faulty_product += faulty_product
    else :
        print('Chương trình đã thống kê xong')
        break

print(f'Tổng số hàng lỗi thu hồi trong ngày là {total_faulty_product}')


