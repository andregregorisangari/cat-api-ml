# Bangkit-Machine-Learning

The source code of machine learning model's API of SnapCat in order to complete Bangkit Capstone Project

![Cover Readme API ML](https://github.com/alfarissss/snapcat-ml-api/assets/134893804/b0365706-085e-4098-9b39-ce65332caca0)


# API URL
Example :
- https://snapcat-image.example/prediction

# Dataset Reasource
- [Kaggle](https://www.kaggle.com/datasets/shawngano/gano-cat-breed-image-collection/data)
- We also try to make data augmentation using python in local folder so the image can bigger than dataset from kaggle. [GoogleDrive](https://drive.google.com/drive/folders/19ix5COwJvpmAMcWRIXlZrXCngih-ts7s?usp=sharing)

# API Endpoint
|   Endpoint   |   Method  | Body Sent (JSON) |                    Description                     |
|   :------:   | :-------: | :--------------: | :------------------------------------------------: |
|      /       |    GET    |       None       |          HTTP GET REQUEST Testing Endpoint         |
| /prediction  |    POST   | file: Image file |        HTTP POST REQUEST Prediction Endpoint       |


# The flow of Machine Learning Service
![flowchart snapcat-ml-api](https://github.com/alfarissss/snapcat-ml-api/assets/134893804/199f4181-bcef-4ea2-80c0-bfcd931fd95c)


# How to run this Flask app
- Clone this repo
- Open terminal and go to this project's root directory
- Type `python -m venv .venv` and hit enter
- In Linux, type `source .venv/bin/activate`
- In Windows, type `.venv\Scripts\activate`
- Type `pip install -r requirements.txt`
- Serve the Flask app by typing `flask run`
- It will run on `http://127.0.0.1:5000`

# How to predict image with Postman
- Open Postman
- Enter URL request bar with `http://127.0.0.1:5000/prediction`
- Select method POST
- Go to Body tab and select form-data
- Change key from form-data with file (it must be named `file`)
- Input the image that you want predict as a value of the key
- Send the request

![image](https://github.com/alfarissss/snapcat-ml-api/assets/134893804/8d790a17-5cdb-4d8f-bac5-4daced1b1789)

![image](https://github.com/alfarissss/snapcat-ml-api/assets/134893804/6f84e930-2fe6-4d19-a08e-b977ed5e5096)


## Architecture of SSD EfficientnetB0 for Cat Breeds Detection
![image](https://github.com/alfarissss/snapcat-ml-api/assets/134893804/3a9aefe9-ee82-4caf-a8eb-7bcd8c1bc3f1)


# References
- Karlita, T., Choirunisa, N. A., Asmara, R., & Setyorini, F. (2022). Cat Breeds Classification Using Compound Model Scaling Convolutional Neural Networks. Dalam Proceedings of the International Conference on Applied Science and Technology on Social Science 2021 (iCAST-SS 2021) (hlm. 909-914). Atlantis Press. DOI: 10.2991/assehr.k.220301.150 [Atlantis Press](https://www.atlantis-press.com/proceedings/icast-ss-21/125971139)
- Mingxing, T. and Quoc, V. L. (2020) “EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks.” [arXiv](https://arxiv.org/abs/1905.11946)
- Oriza Sativa Fiojati, Nani Mintarsih, & Yuli Maharetta Arianti. (2023). PERBANDINGAN ALGORITMA EFFICIENTNETB0 DAN INCEPTIONV3 DALAM KLASIFIKASI CITRA JENIS ANJING. Jurnal Ilmiah Teknik, 2(2), 12–16. [JUIT](https://doi.org/10.56127/juit.v2i2.677)
- K. O. Lauw, L. W. Santoso, and R. Intan, “Identifikasi Jenis Anjing Berdasarkan Gambar Menggunakan Convolutional Neural Network Berbasis Android,” Jurnal Infra, vol. 8, no. 2, pp. 37–43, 2020. [Jurnal Infra](http://publication.petra.ac.id/index.php/teknik-informatika/article/view/10496)
- S. Khatri, A. Rajput, S. Alhat, V. Gursal, and J. Deshmukh, “Image-Based Animal Detection and Breed Identification Using Neural Networks”.[Google Scholar](https://scholar.archive.org/work/3chjbze37bebrgiub3yrn2clmq/access/wayback/http://jst.org.in/wp-content/uploads/2020/09/16.-Image-Based-Animal-Detection-and-Breed-Identification-Using-Neural-Networks.pdf)
- Sihombing, O., & Natsir, M. (2019). Implementasi Metode Dempster-Shafer dalam Sistem Pakar Pendiagnosa Kerusakan Sepeda Motor. Informatika Mulawarman: Jurnal Ilmiah Ilmu Komputer, 14(1). DOI: 10.30872/jim.v14i1.1443[Semantic Scholar](https://www.semanticscholar.org/paper/Implementasi-Metode-Dempster-Shafer-dalam-Sistem-Sihombing-Natsir/d4274d87bc86bb56f2888fe8ac02193de24a439e)
- Dennis-Bryan, K. (2013). The Complete Cat Breed Book: Choose the Perfect Cat for You [Academia.edu](https://www.academia.edu/50650306/The_Complete_Cat_Breed_Book_Choose_the_Perfect_Cat_for_You)
