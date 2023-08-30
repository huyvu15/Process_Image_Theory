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

## Structuring element: 1 hình ảnh nhị phân nhỏ được sử dụng để thăm dò hình ảnh đầu vào


# Image restoration

Việc khôi phúc những ảnh bị hỏng gọi là inpainting. 

# Segmentation(Phân đoạn hình ảnh)

Mục đích: dùng để phân đoạn hoặc đơn giản hóa, biểu diễn thành 1 thứ gì đó dễ phân tích hơn

Ngưỡng là phương pháp đơn giản nhất để phân đoạn

# Superpixel là 1 nhóm các pixel được kết nối với các màu hoặc có mức xám tương tự nhau

Phân đoạn hình ảnh sử dụng 1 thuật toán quen thuộc trong machine learning: KMeans. Nó nhận tất cả các giá trị pixel của hình ảnh và cố gắng tách chúng thành một số vùng con được xác định trước

# Finding contours(tìm đường viền của 1 đối tượng nào đó)

Đường bao là 1 hình dạng khép kín của các điểm hoặc đoạn thẳng, đại diện cho ranh giới giữa các đối tượng

Khi tìm được hình bao chúng ta có thể tìm được điểm trong mã thông báo domino

Đầu vào cho 1 hàm tìm đường bao là hình ảnh nhị phân, có thể tạo bằng các áp dụng ngưỡng đầu tiên

Các bước tìm 1 đường viền của 1 hình ảnh:

- Nếu có màu hãy chuyển sang thang độ xám

- Áp dụng ngưỡng và lấy hình ảnh nhị phân. Khi có hình ảnh nhị phân, chúng ta có thể gọi hàm find_contours() và đặt giá trị cấp không đổi (0.8)

- Sau khi thực hiện các bước này chúng ta nhận được 1 danh sách đường bao. Mỗi đường bao là 1 dãy hình (n, 2), bao gồm n tọa độ hàng và cột dọc theo đường bao.

- Theo cách này, một đường bao giống như một đường viền, tạo thành nhiều điểm được nối với nhau.

# Edge detection

Tìm hiểu 1 trong những kỹ thuật phát hiện cạnh được sử dụng nhiều nhất: Canny. Đây được coi là phương pháp phát hiện cạnh tiêu chuẩn trong xử lý ảnh, có độ chính xác và thời gian thực hiện tốt hơn Sobel

> Module: feature import canny

Hàm này yêu cầu hình ảnh phải là một mảng 2 chiều, nghĩa là 1 hình ảnh có thang độ xám

Giải thích thuật toán:

> Bước đầu của thuật toán này là áp dụng bộ lọc gaussian để loại bỏ nhiễu

Hiệu ứng bộ lọc được áp dụng trên hình ảnh, vì vậy nó sẽ phát hiện nhiều cạnh hơn. Thông thường để tham số sigma = 0.5

Kết quả thu được khi để sigma là 1 và 0.5

--> nhiều cạnh hơn

# Corners

1 corner có thể định nghĩa là điểm nối của 2 cạnh. Về mặt trực quan nó cũng có thể là điểm nối của các đường viền

Harris Corner Detector là 1 toán tử phát hiện góc được sử dụng rộng rãi trong các thuật toán thị giác máy tính

Sử dụng module: corner_harris trong gói feature

Chức năng này yêu cầu hình ảnh thang độ xám, vì vậy trước tiên chúng ta cần chuyển đổi hình ảnh rgb sang màu xám

Trong phương thức corner_harris tham số min_distance = 5 là khoảng cách tối thiểu giữa các góc là 5 pixel

# Face detection

Để sử dụng tính năng nhận diện khuôn mặt từ mô hình học máy có sẵn skimage. Chúng ta sử dụng class Cascade từ module tính năng

Để áp dụng bộ dò trên hình ảnh chúng ta cần sử dụng phương thức detector_multi_scale từ cùng 1 lớp

--> Nó tạo ra 1 cửa số di chuyển qua hình ảnh đến khi nó tìm thấy thứ tương tự như khuôn mặt người 

Cửa số sẽ có kích thước tối thiểu để phát hiện khuôn mặt nhỏ hoặc ở xa. Tùy chỉnh để tìm đc khuôn mặt lớn hơn

Phương thức này lấy hình ảnh làm tham số đầu vào đầu tiên(ima = image), một hệ tỉ lệ scale_factor = 1.2, step_ratio = 1(để càng cao thì kém quả sẽ kém hơn nhưng tốc độ tìm nhanh), kích thước tối thiểu, tối đa min_size(10, 10), max_size(200, 200)

**Khi in kết quả chúng ta thấy nó là 1 dict trong đó r(row), c(column),...**

# **Lưu ý cuối**

- Có thể sd nhận diện khuôn mặt để sau này làm mờ chúng bằng cách áp dụng bộ lọc gaussian 

- Thậm chí là giảm nhiễu

- Phân loại hình ảnh

**Application:**

Nhận diện khuôn mặt và làm mờ chúng:
```python
for d in detected:
    # Obtain the face cropped from detected coordinates
    face = getFace(d) # trích xuất
```

Đối với mỗi khuôn mặt được phát hiện như là biến d trong danh sách sẽ được phát hiện. Sử dụng các tọa độ để cắt nó ra khỏi hình ảnh(trích xuất)

```python
def getFace(d):
    ''' Extracts the face rectangle from the image using the
    coordinates of the detected.(vẽ 1 hcn xq mặt được phát hiện của hình ảnh)
    '''
    # X and Y starting points of the face rectangle
    x, y = d['r'], d['c']
    # The width and height of the face rectangle
    width, height = d['r'] + d['width'], d['c'] + d['height']
    # Extract the detected face
    face= image[x:width, y:height]
    return face
```

- Lấy r là vị trí hàng của góc trên cùng bên trái của hcn được phát hiện...

Now, Face đã bị cắt khỏi hỉnh ảnh, sử dụng bộ lọc gaussian để làm mờ và làm cho nó không thể hiện ra

```python
# Detect the faces
detected = detector.detect_multi_scale(img=image,
                                       scale_factor=1.2, step_ratio=1,
                                       min_size=(50, 50), max_size=(100, 100))
                                       
# For each detected face
for d in detected:
    # Obtain the face cropped from detected coordinates
    face = getFace(d)
    
    # Apply gaussian filter to extracted face
    gaussian_face = gaussian(face, multichannel=True, sigma=10)
    
    # Merge this blurry face to our final image and show it
    resulting_image = mergeBlurryFace(image, gaussian_face)
```

Hình ảnh kết quả này được gán cho biến gaussian_face 

Bước cuối cùng, chúng ta sẽ hợp nhất khuôn mặt mờ trở lại hình ảnh sử dụng 1 chức năng khác gọi là hợp nhất khuôn mặt mờ(func mergeBlurryFace)

```python
    def mergeBlurryFace(original, gaussian_image, d):
        # X and Y starting points of the face rectangle
        x, y = d['r'], d['c']
        # The width and height of the face rectangle
        width, height = d['r'] + d['width'], d['c'] + d['height']
        original[x:width, y:height] = gaussian_image
        return original
```

Để làm như vậy cần chỉ định lại các điểm X, Y bắt đầu cũng như chiều rộng, chiều cao để cắt lại hình ảnh ban đầu

--> Có thể train lại file xml để nó nhận diện đc khuôn mặt quay trái quay phải, có thể tìm trên mạng

có thể làm tương tự đối với nhận diện xe, bão, sách,...