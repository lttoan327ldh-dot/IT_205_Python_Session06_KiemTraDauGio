
stock = 100

while True:
    export = int(input('Nhập số lượng muốn xuất: '))
    if export < 0:
        print('Không được nhập số âm vui lòng nhập lại ')
        continue
    if export > stock:
        print('Kho không đủ hàng, vui lòng nhập lại')
        continue
    else:
        stock = stock - export
        print('Xuất kho thành công!')
        print(f'Tồn kho còn lại: {stock}')
        break