---
title: 2020 CV (Notes for Final）

---

# 2020 CV (Notes for Final）
[先前期中共筆](https://hackmd.io/eG2UKqDdSQuXyTlB9uFPVQ)
[去年共筆](https://hackmd.io/UhyNov3ASWm6DdsFvIUcwQ)
## 備註(更)
*    ==助教研究部分，外國人助教的投影片沒有整理方法、步驟和結果，若有人知道怎麼寫可以補上，特別是「結果」我有點不知道怎麼寫比較好==

*    ==名詞解釋尚未補上「應用」，<>代表不確定要寫什麼==

*    編輯權限為「所有人」皆可編輯，任何人都可以參與共筆。
*    ==關於「助教說可能會考的區塊」部分，助教說會跟老師說建議考以下區塊，但確切的題目內容還是看老師==

## TOC
[TOC]





## Ch7 Conditioning and Labeling
### 助教說可能會考的區塊
**(真的只是可能而已)**
投影片右上角寫"Test"的部分
![test](https://i.imgur.com/wMrEA1O.png)
Order
![](https://i.imgur.com/jnQNAXO.png)

### 名詞解釋
*    conditioning:(調節/潤飾)
內容：
Conditioning is based on a model that suggests that the observed image is composed of an informative pattern modified by uninteresting variations that typically add to or multiply the informative pattern.
在具有眾多pattern的影像中，也就是在informative的影像中，我們想要知道特定的pattern，因此要將informative image uninteresting pattern，去除其他干擾
調節是基於一個模型的，該模型表明觀察到的影像由訊息模式組成，該訊息模式由通常不會增加或增加訊息模式的無趣變化所修飾。
基於模型指出觀測到的影像會由一些帶有訊息的pattern組成(informative pattern)，而這些帶有訊息的pattern，可以經由在informative pattern加上uninteresting variation
目的：
==去除無用的資訊、雜訊==
應用：
降躁、影像銳利化、背景均一化
*    labeling:(標記)
內容：
Labeling is based on a model that suggests that the informative pattern has structure as a spatial arrangement of events, each spatial event being a set of connected pixels.
基於一個模型，該模型表明訊息模式具有事件空間排列的結構，每個空間事件都是一組相連的像素。
==針對像素進行標籤==
目的：
==讓電腦能夠透過學習來認知影像中的物件==
應用：
閥值化、邊緣檢測、自駕車、機器人、相片搜尋、影片檢索、商品搜尋、辨識影像中的各種物體、thresholding、edge detection、corner finding

*    Noise cleaning: 
雜訊去除以鄰域==空間的連貫性==和==鄰域pixel值均勻性==為基礎，用image上其他更相關的pixel值做替換，或通過鄰域中的其他像素進行平均或平滑過的值做取代。
>Using neighborhood spatial coherence and neighborhood pixel value homogeneity as its basis for removing noise data. The noise data is replaced by some spacial coherent data or smoothed according to the neighborhood data.


*    Zero-crossing edge detector:
一種邊緣檢測，能檢測拉普拉斯算子的值穿過零的位置，即拉普拉斯算子改變符號的點.
通常落於閉合輪廓上(closed contour)
https://homepages.inf.ed.ac.uk/rbf/HIPR2/zeros.htm

*    Median root: 
一直重複做median filter會得到一個最後不會再改變的結果稱為 median root


*    k-nearest neighbor average:
將附近的所有像素值與中心像素值進行比較。 最接近的k個像素值用於確定最終值，在這種情況下為這些k個像素的平均值。

*    Outlier or peak noise:
離群值(峰值雜訊)，一個像素，其像素值與其相鄰像素值明顯不同，像素值會被隨機雜訊替換。 
>The value of the pixel at this position is simply replaced by a random noise value typically having little to do with the underlying pixel’s value.
A pixel that has a value awkwardly different from its neighbors.

*    Order Statistic Neighborhood Operators
將鄰域像素排序後所設計的鄰域運算子
如Median Operator
    

*    Digital edge：一條影像上的邊界，左右兩側的pixel value 明顯不同（灰階值有明顯的變化的地方）

*    Edge : 亮度有突然的抬升或下降。

![](https://i.imgur.com/awYBsvG.png =500x300)

* Step edge：階梯邊緣(步邊)的展示就是影像亮度明暗的不連續。（灰階明暗變化明顯且不連續）
a discontinuity in ==the magnitude== of the image intensity.

* Roof edge：屋頂邊緣的展示就是影像亮度的第一個偏差中的不連續性。（影像灰階強度一階導數不連續）
discontinuity in the ==first derivative== of the image intensity.
* Line edge：兩個彼此靠近的step edge。（兩側明暗變化明顯的邊緣）
Line edge comprises  ==two step edges that are close together==.
*    Sobel Edge Detector（gradient detector）
![](https://i.imgur.com/Axxt23i.png =300x)

Laplacian透過計算二次微分通過零點(Zero Crossing)觀念來判定。
Sobel使用的則是Gradient methods。

*    Line segment (線段)
可以被描述成一個拉長的矩形，其內部有一致的灰階值，被另一個擁有不同灰階值區域區隔開來。

*    SNR
![](https://i.imgur.com/TSgfeAX.png =300x150)

*    salt and pepper noise
![](https://i.imgur.com/gcIM6QJ.png =300x150)

##### A Statistical Framework for Noise Removal
>Masks for different assumptions[color=#f7f302]

1.假設這張影像的雜訊是隨機而且不相關的
參數: $\alpha, \beta$
![](https://i.imgur.com/B1csgkG.png)

2.假設這張影像的雜訊是有相關性的，且相關性是$ρ^n$，n> 1，n代表的是距離 
參數: $\rho$
![](https://i.imgur.com/TZfIoMQ.png)



##### ==**TEST**== Noise Removal(Methods)
>偵測並替換noise pixels，以下共十種方法[color=#f7f302]
0. 變數定義
![](https://i.imgur.com/CErKp7K.png =300x200)
$\hat{\sigma}^2 = \frac{1}{N-1}\sum_{n=1}^N(x_n-\hat{\mu})^2$

==non-order statistic neighborhood operators==
1. Outlier Removal:
假如 $y - \hat{\mu}$ < 門檻值，則輸出 y, 保持中心值值不變
假如 $y -\hat{\mu}$ >= 門檻值，表示 y 是 outlier, 用 $\hat{\mu}$ 取代之
$\begin{equation}
    Z =
     \begin{cases}
        y & \text{if}\ \ |y-\hat{\mu}| < \theta \\
        \hat{\mu} & \text{else}
     \end{cases}
\end{equation}$


2. contrast-dependent outlier removal
相依對比的離群值移除
$\begin{equation}
    Z =
     \begin{cases}
        y & \text{if}\ \ \frac{|y-\hat{\mu}|}{|\hat{\sigma}|} < \theta \\
        \hat{\mu} & \text{else}
     \end{cases}
\end{equation}$

3. smooth replacement(convex combination of input and mean)
中心pixel和$\mu$做線性組合。
Two special cases: 
$K = 0 \Rightarrow Z = \hat{\mu}$
$K = \infty \Rightarrow Z = y$
$\begin{equation}
    Z = \frac{\frac{|y-\hat{\mu}|}{|\hat{\sigma}|}}{\frac{|y-\hat{\mu}|}{|\hat{\sigma}|}+K}\hat{\mu} + \frac{K}{\frac{|y-\hat{\mu}|}{|\hat{\sigma}|}+K}y
\end{equation}$

4. K-nearest Neighbor 像素值最接近中心值的k個neighbor取平均
average of k-nearest neighbors

5. Gradient Inverse Weighted
Step1：g(r’, c’, r, c)  = neighbor距離參考點(中心點)的倒數，來當作weight(center delete)
Step2：加總所有的weight
Step3：除中心點外的其他權重矩陣元素為W(r’, c’, r, c)，8個加權係數之和為1/2   (建立標準化的權重矩陣W作為平滑的mask)
Step4：原像素f分別與w相應位置上的權重相乘，積之和就是中心點的平滑輸出。
(下面的step2公式有點怪跟圖對不上，應該就按照圖就好了，如果出這應該算有點爭議)
![](https://i.imgur.com/H269FEd.png =300x200)

==order statistic neighborhood operators==
6. Median Operator
排序過後的鄰域中的median數值代替中心數值 
effective for impulsive noise(salt and pepper)
![](https://i.imgur.com/jqKCiZx.png =150x50)

7. Running Median Filter
Q : 四分位差距
![](https://i.imgur.com/bNu72EX.png =300x150)

8. Trimmed-Mean Operator
不使用前k和後k次序統計，只用中心N-2k的加權平均數
![](https://i.imgur.com/wUTgYCi.png =350x150)


9. Midrange operator
最亮+最暗/2
僅在雜訊分佈輕而平滑時較有效率，否則此方法不適用於大部分的情況
![](https://i.imgur.com/fTcMRA5.png =350x150)

10. Sigma Filter
僅在兩個sigma間隔內取平均值
![](https://i.imgur.com/3gfU8Sp.png =350x100)


#### Sharpening
1. Unsharp masking
從每個像素中減去鄰域平均值，然後縮放數值。
效果：產生的影像，雖然更清晰，可能是一個較不准確的影像。
$Z_{sharpened}$ = s * [y - k$\hat{\mu}$]
2. Extreme Sharpening
輸出值是鄰域的最小值或最大值與中心像素值之間的接近值。也就是說看中心pixel值離鄰域的極大值或極小值這兩種極值，哪個極值較近就當作輸出。
效果： 讓intensity強的pixel 更強(intensity亮度、強度)讓intensity弱的pixel 更弱
![](https://i.imgur.com/AzMR80Y.png =300x)

Edge Detection

數字邊緣是兩個像素之間的邊界，當兩個像素的亮度值”明顯不同”時就是邊緣。目的是要找出灰階中有劇烈變化的邊界

- Roberts Operator
![](https://i.imgur.com/CYYnJK6.png)

- Prewitt edge detector
![](https://i.imgur.com/EL3J9t1.png)

- Sobel Operator


Properties

==Four important properties an edge operator might have==:
準確估計梯度的大小
準確估計梯度的方向
準確估計step edge 的對比性
準確估計step edge 的方向性

gradient direction: used for edge organization, selection, linking.

False-alarm rate : 假警報 把不是邊的pixel判定成是邊的pixel
Misdetection rate :  誤檢率 明明是邊上的pixel卻判定成不在邊上



Common Masks to calculate Laplacian
![](https://i.imgur.com/s3usxLD.png)
Minimum variance: 
2, -1, 2
-1, -4, -1,
2, -1, 2



## Ch8 The Facet Model(小平面模型)

### 助教說可能會考的區塊

考8-2 ~ 8-3 (8-4)

### 名詞解釋

- Facet model:
可以將圖像視為基礎連續體或分段連續灰階強度表面，其中包括分段常數（平面小平面模型)，分段線性（傾斜小平面模型），分段二次和分段三次。  
>Images can be thought of as an underlying continuum or piecewise continuous gray level intensity surface, which includes piecewise constant (flat facet model), piecewise linear (sloped facet model), piecewise quadratic and piecewise cubic.

- peak noise pixel
尖端雜訊像素，灰階值意義上和鄰居不一樣(略顯突兀的感覺)
*    gradient-based edge detection
high values in first partial derivative (sharp discontinuities)

- Iterated Facet Model
1. 可以被分割成許多相連區域
2. 每一個都符合特定的灰階和形狀限制
facets:image spatial domain partitioned into connected regions
facets:satisfy certain gray level and shape constraints
facets:gray levels as polynomial function of row-column coordinates

*    Shape region constraint: 
各個小平面必須是平滑形狀($k*k$ blocks of pixels)

*    Region gray level constraint: 
Gray levels in each facet must be a polynomial function of row-column coordinates.
每一個小平面的座標(R, C)必須是多項式方程式(facet model)
Output 會是最小 variance 
並具有最小的residual error

- Gradient-Based Facet Edge Detection https://i.imgur.com/Lvo1V8W.png
梯度邊界偵測就是找一階偏微分的值很大的地方（明顯的不連續）
- Bayesian Approach to Gradient Edge Detection
G代表gradient
![](https://i.imgur.com/Lvo1V8W.png)
- directional derivative
rate of change in the given direction
應用：Directional Derivative Edge Finder
- Integrated Directional Derivative Gradient Operator
透過對一階方向導數做方形(square area)積分，來量測積分方向導數的強度
- corner detection algorithm
![](https://i.imgur.com/zSAew2y.png =500x300)


- corner points
A corner can be defined as the intersection of two edges.
求出一對圖片的位移向量
角落的2條件:有邊出現、明顯邊方向的變化
目的：可以從影像中提取的其他類的特徵包括角、孔和地形標記(峰、脊和谷)。
應用：空照圖偵測建築物
#### topography

define 

$𝜆_1$ is second directional derivative in $𝜔^{(1) }$direction.
$𝜆_2$ is second directional derivative in $𝜔^{(2) }$direction.
$\omega^{(1)}$: 二階方向導數具有最大強度的單位方向向量(vector)
$\omega^{(2)}$: 正交於$\omega^{(1)}$的向量(vector)


*    Peak
![](https://i.imgur.com/uyr9rVo.png)


*    Pit
![](https://i.imgur.com/VxEmQwQ.png)


*    Ravine(Valley)
灰階值比 neighbors 低的 connected sequence of pixels
深谷發生在灰階值比鄰居低
![](https://i.imgur.com/Uv0Fy8t.png)

*    Ridge
灰階值比 neighbors 高的 connected sequence of pixels
山脊發生在灰階值比鄰居高


![](https://i.imgur.com/MzgrN5q.png)

*    Saddle
![](https://i.imgur.com/WrMVK8w.png)


*    Flat
![](https://i.imgur.com/30f0wRd.png)


*    Hillside
A hillside point is anything not covered by previous categories.


### 8.2 Relative Maxima
須滿足以下兩條件
*    first derivative zero 一階微分為零
*    second derivative negative 二階微分為負

#### How to solve
Step1:Given one-dimensional observation sequence $f_1,f_2,f_3,...,f_N$

Step2:定義group(window) size = 2k+1

Step3:最小化$\epsilon_n^2=\sum_{m=-k}^{k}{(\hat{c}m^2+\hat{b}m+\hat{a}-f_{n+m})^2}$，對應的三個參數$\hat{c},\hat{b},\hat{a}$
>最小化 即 一階微分=0
>
![](https://i.imgur.com/pTEt5jb.png =200x)


Step4:檢驗relative maxima

![](https://i.imgur.com/g4plla8.png  =300x100)

#### Example
請看ppt，總之就是上面的step1~step4


### 8.3 Sloped Facet Parameter and Error Estimation


#### How to solve
Step1:
Define $g(r,c)$ image function, assume the given pixel is (0,0)
$g(r,c)=\alpha r + \beta c + \gamma + \eta(r,c)$
![](https://i.imgur.com/Uywjqvb.png)

Step2:
最小化
$\epsilon^2=\sum_{r\in R}\sum_{c\in C}(\hat{\alpha} r + \hat{\beta} c + \hat{\gamma}-g(r,c))^2$，求三個參數$\hat{\alpha},\hat{\beta},\hat{\gamma}$
![](https://i.imgur.com/bLLfIn4.png =150x150)

Step3:
根據image求$g(r,c)$，並計算error
$\epsilon^2=\sum_{r\in R}\sum_{c\in C}(\epsilon(r,c))^2$

Step4:
$\sigma^2 = \frac{\epsilon^2}{[(\sum_{r}\sum_{c}1) - 3]}$

![](https://i.imgur.com/bioiVyE.png =300x150)
(這公式好像有點怪，$\epsilon^2$，上方是11.19，圖中下方是$11.19^2$)
(這樣應該算有爭議(?))
(之前我下課問過助教，他說是下面數字錯了)
#### Example
請看ppt: p.45 ~ p.58
註: 助教註解有說，可能就考跟example一樣的(可能數字不改&附公式)


### 8.4 Facet-Based Peak Noise Removal
step1: 用8.3方法(去掉中心點)，算出$\epsilon^2跟\hat{\alpha},\hat{\beta},\hat{\gamma}$
step2 t-test
![](https://i.imgur.com/lv6b8hH.png =150x80)
if t >𝑇_(#𝑁−3, 𝑝) then g(0,0) = $\hat{\gamma}$
else pass(代表g(0,0)不是peak noise)

## Ch9 Texture
### 助教說可能會考的區塊
1. Introduction : 9.1
2. Application : 9.16 ~ 9.18
3. Texture Analysis Issues(p.21)投影片

### 名詞解釋
*    Autocorrelation function
Autocorrelation function is a feature that describes the size of gray level primitives

*    texture edgeness
根據每單位面積的邊緣度來構思紋理。


*    Vector Dispersion
將紋理劃分為互斥的鄰域 (每個平面最像，相互之間error最小的區域)，以鄰域灰階值來為每個鄰域fit傾斜平面


*    Coarseness: 
粗紋理，具有很小的方差，並且分佈僅隨距離而略有變化。

*    Fractal
Fractal 碎形，一種自然的現象或是數學運算使圖像在不同 scale 上 recursive 畫出相同的 pattern
重複劃出相同的圖案
這一類recursive的動作畫出的pattern我們稱為fractal

*    Relative Maxima and Relative Minima
![](https://i.imgur.com/8QVZO5A.png)

*    tangent line
切線，指的是一條剛好觸碰到曲線上某一點的直線。更準確地說，當切線經過曲線上的某點（即切點）時，切線的方向與曲線上該點的方向是相同的。


*    granularity(顆粒度)
![](https://i.imgur.com/xwQCBsT.png)
    一張binary image F 透過
    直徑為d的structure element opening 後佔整體的比例
    Image 經過直徑為d的structure element  Opening  後
    表示會留下顆粒度比d還要大的部分
    再用1去扣掉，表示比d還小的部分
    顆粒度小的(fine) 曲線比較快達到100% (畫圖)
    反之 曲線比較平緩達到100%
*    AutoRegresssion Models
使用附近pixel對目前像素的值進行線性估計

*    Discrete Marcov Random Fields
每個像素的值是其附近值與相關noise的線性組合

*    Mosaic model: 
包括2個步驟：首先將平面細分為單元，然後為每個單元分配屬性值。 
#### 9.1 Introduction
*    Texture
==A set texels occurring in some regular or repeated pattern.==
Described by 
>-  type of primitives
>- number of primitives
>- spatial organization or layout

應用:

*    Texel(Texture element)
==Texel是可以透過重新排列組合，組成Texture的單位==
應用:


*    Texture Primitive
==texture內 相同類型 相同屬性的小單位==
E.g Simplest primitive: pixel with gray level attribute
>Connected set of pixels characterized by attribute set.


#### Texture Analysis Issues
Pattern recognition: 
Given textured region, ==determine the class== the region belongs to.

Generative model: 
Given textured region, ==determine a description or model== for it.

Texture segmentation: 
Given image having many textured areas, ==determine boundaries==.

9.2 & 9.3 co-occurrence  -> 顆粒大小
9.4 autocorrelation  -> 顆粒、隨機性
9.5 digital transform methods  -> 方向、顆粒
9.6 texture energy (convolution) -> segmentation
9.7 texture edgeness -> Edge的粗細、方向
9.8 vector dispersion  -> 粗糙、平坦
9.9 relative extrema density  -> 顆粒
9.10 mathematical morphology -> 顆粒、碎形
9.11 ~ 9.13 autoregression, Markov random field, random mosaic models -> 係數推測


#### Application
*    Texture Segmentation
紋理分割是將圖像分成具有不同紋理的區域，包含相似的像素組。
有很多不同方法如使用texture energy的方式或深度學習

*    Synthetic Texture Image Generation
步驟0：輸入樣本紋理(sample texture)
步驟1：從原始紋理樣本圖像中選擇一個區域作為初始區域。
步驟2：在原始圖像中找到邊緣相似的區域。
步驟3：將其粘貼到結果圖像上。
步驟4：返回步驟2並重複。

        *    Step0 : Input sample texture
        *    Step1: Choose a region from the original texture sample image as the initial region.
        *    Step2: Find the region with the similar edges in the original image.
        *    Step3: Paste it on the result image.
        *    Step4: Back to Step2 and repeat.
*    Shape from Texture
使用圖像紋理的gradient來估計3D物體的表面方向

## Ch10 Image Segmentation
### 助教說可能會考的區塊
1. 10.2.1 k-means clustering
2. 10.2.3 thresholding
3. 10.6 Split and Merge

### 名詞解釋
*    image segmentation
將圖片劃分成一組不重疊的區域，而這些分割區域的聯集是整個圖片
partition of image into set of non-overlapping regions union of segmented regions is the entire image



*    Label標記：
獨特的名字或是索引。作為具有潛在目標區域的辨識碼
A pixel whose value is in the ith interval is labeled with index i.

*    Connected Component連通元件：
Connected components, in a 2D image, are connected region of pixels with the same value or label.


*    Recursive histogram-directed spatial clustering.
![](https://i.imgur.com/6mVbZEJ.png =x500)


*    LANDSAT image
consists of seven separate images called bands

*    Single-Linkage Region Growing
將每個像素視為Graph中的節點，將具有足夠相似屬性的相鄰像素透過arc連接
regard each pixel as node in graph
neighboring pixels with similar enough properties: joined by an arc

*    Hybrid-Linkage Region Growing
將屬性向量分配給每個像素，建立相似度。並使用edge detector判斷將non-edge的相鄰相似像素用arc連接。
屬性向量：取決於像素的K x K鄰域

*    Centroid-Linkage Region Growing
1.以某種預定的方式掃描圖像，例如左右，上下。
2.將像素值與已經存在相鄰segment平均值進行比較。
3.如果和平均值足夠接近，則將像素添加到segment中，並更新segment的平均值。
4.如果兩個區域的均值足夠接近，則將兩個區域合併，並將像素添加到合併的區域。
5.如果沒有相鄰區域具有足夠接近的均值，則建立一個新的segment。

*    Combined Centroid-Hybrid Linkage
Centroid-linkage for only non-edge pixels
Region growing is not permitted across edge pixels

*    Clustering
1.在模式識別(pattern recognition)中，這是將一組模式向量劃分為子集的過程。
2.將具有相似屬性的項目分組到一個子集中。
1. In pattern recognition, it is the process of partitioning a set of pattern vectors into subsets.
2. Grouping items with similar properties together into a subset.

*    measurement space
待分群的指定特徵代表的空間

*    Spatial Clustering
Simultaneously combining clustering in measurement space with a spatial region growing

*    k-means
Algorithm
1.Randomly initialize cluster centers $U_1 ... U_K$
2.Determine points in each cluster:
For each point x, find the closest Ui; put x into cluster i
3.Given points in each cluster, solve for Ui:
Set Ui to be the mean of points in cluster i
4.If any Ui has changed, repeat Step 2.

*    Local Histogram thresholding
先將影像切分塊，再求出各塊的 histogram 後做 interpolation。

*    High Laplacian Magnitude thresholding
先利用 Laplacian Magnitude 找出邊界後，僅求出邊界附近的 histogram 來分群。

*    Minimized Busyness thresholding
場景為被雜訊干擾的影像，計算整張影像有幾趴的 pixel 的數值與鄰域門檻值不一致。

*    Version 1: Split and Merge(Original Approach)
步驟：
1.以整個圖像作為初始segment
2.如果細分的同質性不夠，請連續將其每個細分細分為四分之一。
3.合併方法從初始分割開始，然後連續合併足夠相似的區域。
Steps:
1.Begins with the entire image as the initial segment
2.Successively splits each of its current segments into quarters if the segment is not homogeneous enough.
3.A merging method starts with an initial segmentation and successively merges regions that are similar enough.
        *    homogeneous enough:
        *    Max – min(極值差異)
        *    Variance(變異數)
        
*    Version 2: Split and Merge (Horowitz and Pavlidis (1976))
1.使用Quadtree作為資料結構，root為整張影像
2.segmentation用cutset表示(root與leaves分開的最小節點集)
3.merge包括從cutset中刪除四個節點並將其替換為其父節點。
4.split包括從cutset中刪除一個節點，並用其四個子節點替換它
5.在split and merge之後，執行Final Grouping，該過程可以合併在cutset中找到的相鄰無關塊。


*    Thresholding(Kohler 1981)
        *    Objective: Maximize ($\frac{C(T)}{\#E(T)}$)
        *    Define $E(T)$:edges detected by a threshold $T$
        *    $E(T)=\{[(i,j),(k,l)]\}$
                *    1.pixels(i,j) and (k,l) are neighbors
                *    2.$min\{I(i,j),I(k,l))\}$ $\leq$ $T$ < $max\{I(i,j),I(k,l))\}$
![](https://i.imgur.com/ZjJIcni.png =x100)


## Ch11 Arc Extraction and Segmentation
### 助教說可能會考的區塊
11.2 Extracting Boundary Pixels from a Segmented Image
11.3 Linking One-Pixels-Wide Edges or Lines

### 名詞解釋
*    grouping:
內容：
The grouping operation identifies the events by collecting together or identifying maximal connected sets of pixels participating in the same kind of event.
==把標籤值相同或相近的區塊圈選出來==
分組操作通過收集在一起或識別參與相同類型事件的最大像素連接集來識別事件。
分組前：像素；分組後：像素集
目的：
有利於將群組化後的資訊進行一些計算
應用：
segmentation分割、edge linking邊緣鏈接
*    extracting:
內容：
The extracting operation computes for each group of pixels a list of its properties.
example properties: centroid, orientation, area, spatial moments
==提取操作：為每組像素計算其屬性列表。==
針對群組化後的資訊進行一些計算，算出一些能代表群組特性的數值，例如：標準差、平均值等
目的：
==把觀察物區塊標明出來，並且得到夠多的資訊以理解觀察物。==
應用：
解析質心、orientation方向、面積、空間矩

*    Junction:
Point where lines, arcs, segments meet.

*    Border Tracking Algorithm
An algorithm that follows the border of a segmented image to extract boundary pixels.
Input: symbolic image（label好背景與區域的的Image）
Output: a clockwise ordered list of the coordinates of its border pixels
In one left right, top bottom scan through the image
During execution, there are 3 sets of regions: current, past, future
> 遇到一個Label，如果他的鄰居有在chainset的尾巴，就加進chainset，如果沒有就新增一個chainset，最後把同個label的chainset都連起來。

*    Linking One-Pixel-Wide Edges or Lines
tracking symbolic edge (line) segments
input: symbolic image (1 for edge, 0 for non-edge)
pixeltype:
        *    isolated point
        *    starting point on new segment
        *    interior pixel of an old segment
        *    ending point of an old segment
        *    junction
        *    corner
> 如果鄰居中沒有屬於某一個segment，則新增一個segment。
> 如果鄰居中有屬於某一個segment，則視為同一個segment。
> 如果鄰居中有兩個分別屬於不同segment，視為joint，作為兩個segment的end
> 如果pixeltype是cornor時，視為該segment的end


*    Arc segmentation
partition extracted digital arc sequence into digital arc subsequences (each is a maximal sequence that can fit a straight or curveline) 

*    Simple Arc Segment
Arcs segment that is a straight line segment or one that is a curved-arc segment containing no straight-line segments.

*    Breakpoint Optimization
移動arc sequence的斷點以產生更好的segment。 重複執行以下操作，直到沒有任何改善：移位奇數點，看最大誤差是否減小，如果是，則繼續移位，否則嘗試移位偶數點。
>Shifting the breakpoints of the arc sequence to produce a better arc segmentation. Repetitively do the following until no improvement:
Shift the odd number points and see if the maximum error is reduced, if yes then keep the shift, otherwise try shifting the even number points.


*    Iterative endpoint fit and split
內容與目的：透過設定distance threshold $d^*$，和解$d_m=max\{d_i\}$來將arc sequence分割成筆直的subsequence
應用：

*    Tangential angle deflection
內容與目的：識別兩個線段相交並形成角度的位置來分割arc sequence。
應用：

*    Uniform bounded-error approximation
將arc sequence做最大分割，這些點的點偏離線段擬合不超過給定值（邊界誤差）。
>Segmenting the arc sequence into maximal pieces whose points deviate from a
line-segment fit by no more than a given amount (bounded-error).

*    Isodata segmentation
決定line-fit參數，然後將每個點歸類到cluster whose line fit closest to the point

*    Split and merge(For arc)
第一：將弧分成幾段，誤差足夠小
第二：合併接續(successive)的分段，如果合併後的分段具有足夠小的誤差
第三：嘗試調整斷點以獲得更好的細分
重複：直到所有三個步驟都沒有進一步的變化


*    Hough transform
內容與目的：在灰階圖中偵測直線和曲線的方法，會透過accumulator array 來計算
應用：偵測道路線

*    curvature
![](https://i.imgur.com/g8gA17p.png)
Δs : the change in arc length
Δθ : the change in tangent angle 


## 助教們研究

### 1.Vehicle License Plate Recognition with Deep Learning
![](https://i.imgur.com/QS9Rmdk.png)

### 2.Label Optical Character Recognition.
![](https://i.imgur.com/CZtBP6i.png)

### 3.Time of Flight Camera Calibration
![](https://i.imgur.com/iFwf5wh.png)

### 4.Solder Quality Analysis
![](https://i.imgur.com/8fUvFmG.png)
考試答案
方法：
學習式向量量化神經網路 + 查找表
步驟：4個灰度曲線圖→學習式向量量化神經網路→5個曲線類別→查找表→3個錫球品質類別
結果：
錫球被分類為：錫球量過多、錫球量正常或錫球量不足


### 5.Noise Reduction for Enhancing Speech Quality And Intelligibility
>外國人助教是說寫三種model其中一個就可以，但不知道改考卷的助教是否是他，所以不清楚寫多細才可以全拿。[color=#ba44e5]

Methods: Deep Denoising AutoEncoder (DDAE)
Steps: input speech  => FFT => speech enhancement (DDAE) => enhanced speech => calculate spectral difference => DDAE => IFFT => final enhanced speech
Results: input noisy speech to enhanced speech

#### Methods:
There are three methods to do noise reduction
1.Noise Reduction Using Two Stages Deep Learning Model
2.Specialized Speech Enhancement Model Selection Based on Learned Non-Intrusive Quality Assessment Metric
3.Speech Enhancement based on Denoising Autoencoder with Multi- branched Encoders

#### Steps:
Each figure corresponds to different methods

##### 1
![](https://i.imgur.com/f0ThhJL.png)
![](https://i.imgur.com/MCQbPhY.png)

##### 2
![](https://i.imgur.com/X1nNbXx.png)

##### 3
![](https://i.imgur.com/5u5t2QC.png)

#### Results
2. 
    - Performance on WSJ dataset 
    - Test data were injected by 4 unseen noises
    - Performance improved in terms of PESQ and STOI metrics

## Bonus
Is text or joke more important?
ans:笑話比本文重要！
>貌似是每年都會有的bonus ：https://www.pttweb.cc/bbs/NTU-Exam/M.1578382932.A.CA6

Please write the Chinese name of Professor Chiou-Shann Fuh.
ans: 傅楸善

猴子在開飛機

What's Professor Chiou-Shann Fuh's pet phrase? (a) 酷斃了Cool (b) 帥呆人Handsome (c\) 好極了Good (d)棒透了Awesome

(c\)

Please translate "To err is human, to forgive divine." into Chinese.
人非聖賢，孰能無過

Please translate "塞翁失馬，焉知非福" into English.
Sometimes misfortune is a blessing in disguise.

## 考古
### 108

(1)conditioning
(2)labeling
(3)extremum sharpening
(4)Sobel edge detector
(5)facet model
(6)directional derivative
(7)corner detection algorithm
(8)tangent line
(9)fractal
(10)Hough transform
(11)border-tracking algorithm
(12)iterative endpoint fit and split
(13)tangential angle deflection
(14)breakpoint optimization

2.(6%) Please list at least 3 noise removal methods and equations using
neighborhood operators.

3.(6%) Please describe the method, steps, and results of Super Resolution and
Point Spread Function Inverse Filtering for X-Ray Images

4.(6%) Consider the following 3X3 region:
r/c     -1      0       1
-1      3       5       9
0       4       7       7
1       0       3       7
The sloped facet is given by α^r + β^c + γ^ . What are the values of
estimated parameters α^, β^, γ^?
Hint:


5.(6%) Please describe the method, steps, and results of Hand Gesture
Recognition with 3D Camera.

6.(6%) Please list three issues of the texture analysis and give a detailed
description for each issue.

7.(6%) Please show the steps of the synthetic texture image generation, that is, how you can generate new texture images using one original texture image.

8.(6%) Please describe the method, steps, and results of Driver Drowsiness
Detection.

9.(6%) Please list at least three image segmentation methods and explain in
detail

10.(6%) Please calculate the average contrast (C(T)/#E(T)) of all edges.

T=50
[45, 110]
[33,88]
[15, 65]
[45, 115]
[0, 225]

11.(6%) Please describe the method, steps, and results of Filtered Back
Projection for X-Ray Images

12.(6%) Please fit the best straight line L: y=mx+b for the given data points.(圖片省略，但其三點分別為：(1, 3), (2, 2), (3, 1))

13.(6%) Please describe the method, steps, and results of Medical Image
Segmentation for Pancreas Cancer.

Bonus
14.(2%) Please write the Chinese name of Professor Chiou-Shann Fuh.
15.(2%) What's Professor Chiou-Shann Fuh's pet phrase? (a) 酷斃了Cool (b) 帥呆人Handsome (c) 好極了Good (d)棒透了Awesome
16.(2%) Is text or joke more important?
17.(2%) Please translate "To err is human, to forgive divine." into Chinese.
18.(2%) Please translate "塞翁失馬，焉知非福" into English.