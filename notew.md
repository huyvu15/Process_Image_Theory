# Note

# Thresholding(ngưỡng)
Là phương pháp đơn giản nhất để phân loại hình ảnh. Tạo ngưỡng giúp cô lập các phần tử và được sử dụng trong phát hiện đối tượng, nhận dạng khuông mặt và các đối tượng khác

Nó hoạt động tốt nhất trong các hình ảnh thang độ xám có độ tương phản cao

Để ngưỡng hình ảnh màu trước tiên chúng ta phải chuyển chúng sang thang độ xám

# Filters
tất cả hình ảnh đều được xác định bởi các cạnh(khung)

- 1 thuật toán phát hiện cạnh là Sobel, là 1 gói trong sckit-learn

Quy trình: nếu ảnh có màu thì chuyển nó sang màu xám


Module bộ lọc:

- Gaussian smoothing:làm mờ ảnh và loại bỏ nhiễu

# Contrast enhancement
Độ tương phản của 1 hình ảnh có thể coi là thước đo phạm vi hoạt động của nó hoặc "độ lan rộng" của biểu đồ nó.

Độ tương phản là sự khác biệt tối đa giữa cường độ điểm ảnh tối đa và tối thiểu

Khi cải thiện độ tương phản các chi tiết sẽ rõ ràng hơn

Hình ảnh có độ tương phản thấp có sự khác biệt nhỏ giữa các giá trị pixel tối và sáng

Thường bị lệch sang phải(chủ yếu là ánh sáng), bên trái (khi chủ yếu là tối), hoặc nằm ở xung quanh giữa(chủ yếu là màu xám)

Các loại cân bằng biểu đồ:

> Histogram equalization(tiêu chuẩn)

> Adaptive histogram equalization(thích ứng)

> Constract Limited Adaptive Histogram Equallization(CLAHE-Hạn chế)

Phương pháp AHE là một biến thể của histogram equalization thông thường nhưng được áp dụng theo cách linh hoạt hơn. Thay vì sử dụng một phân phối cố định cho toàn bộ ảnh, AHE chia ảnh thành các phần nhỏ và áp dụng histogram equalization trên từng phần riêng biệt.

# Morphology(hình thái học)
Các vùng nhị phân được tạo bằng cách tạo ngưỡng đơn giản có thể bị nhiễu do nhiễu và kết cấu hình ảnh

CÁc hoạt động hình thái cơ bản:

> Dilation(Giãn nở): thêm pixels vào ranh giới của các đối tượng trong 1 ảnh

> Erosion(Xói mòn): Loại bỏ pixels trên ranh giới của các đối tượng

## Structuring element: là 1 hình ảnh nhị phân nhỏ được sử dụng để thăm dò hình ảnh đầu vào


# Image restoration

Việc khôi phúc những ảnh bị hỏng gọi là inpainting