stock = int(input(' Nhập số lượng tồn kho của sản phẩm: '))
if stock < 0:
    print('Số lượng sản phẩm phải lớn hơn 0')
if stock >= 50:
    print('Tình trạng: Hàng đầy kho')
elif stock >= 10:
    print('Tình trạng: Mức an toàn')
else:
    print('Tình trạng: Sắp hết hàng, cần nhập thêm')

