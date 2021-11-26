# YOLOV4 Custom Object Detector Google Colab 

Bu yazıda kendi nesne tanıma modelimizi eğitmeyi anlatacağım. Ben kendime nesne olarak Boston Dynamics’in Spot robotunu seçtim.
İlk olarak Darknet’i bilgisayarımıza indirmekle başlayacağız. Öncelikle git installer’ı indireceğiz. Bu şekilde github üzerinden dosya indirme işlemini kolaylıkla gerçekleştireceğiz.
Bu adrese giderek kullandığımız işletim sistemine uygun olanı seçip indiriyoruz. İndirilen dosyaya tıklayarak kurulumunu tamamladıktan sonra bilgisayarımın istediğim konumunda yeni bir klasör açıp isimlendiriyorum. Sonrasında klasörün içerisine girip sağ tıklayarak ‘Git Bash Here’ seçeneğine tıklıyorum, açılan pencerede
git clone https://github.com/AlexeyAB/darknet komutunu yazarak enter’a basıyorum.

Yükleme tamamlandıktan sonra Darknetin Makefile dosyasını not defteriyle açarak şu düzenlemeleri yapıyorum:

GPU, CUDNN ve OPENCV satırlarını 1 yapıyorum.
