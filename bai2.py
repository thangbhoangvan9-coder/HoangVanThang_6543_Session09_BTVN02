# danh sách express_orders thay đổi GE100-FAST được chèn vào đầu 
#  Sau khi dùng insert(), index đã thay đổi nên: express_orders[1] đang là "GE101" chứ không phải "GE102-WRONG".
# "GE102-WRONG" đang nằm ở index = 2
# dòng sau không xóa đúng đơn hàng bị hủy vì : pop(3) xóa phần tử theo index. Nếu index thay đổi sau các thao tác trước đó thì có thể xóa nhầm phần tử khác.
# xóa đúng đơn hàng "GE103-CANCEL" dùng: express_orders.remove("GE103-CANCEL")
# pop() không truyền index sẽ: Lấy phần tử cuối cùng đồng thời xóa phần tử đó khỏi danh sách
# dòng sau lấy sai đơn hàng đang giao vì : pop() mặc định lấy phần tử cuối danh sách. Nếu đơn hàng đang cần giao là đơn đầu tiên thì dòng này sẽ lấy sai.
# lấy đơn hàng đầu tiên trong danh sách ra để giao, cần viết:
# Muốn chương trình cho ra kết quả đúng, cần sửa lại những dòng: express_orders[1] = "GE102-UPDATED", express_orders.pop(3), current_order = express_orders.pop()

express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]
express_orders.append("GE104")
express_orders.insert(0, "GE100-FAST")
express_orders[2] = "GE102-UPDATED"
express_orders.remove("GE103-CANCEL")
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)