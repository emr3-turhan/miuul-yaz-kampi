Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@emr3-turhan 
o-emre-turhan
/
g211210012-bsm104-project
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
g211210012-bsm104-project/Sehrim.html
@o-emre-turhan
o-emre-turhan hakkimda_indexhtml_olarak_degistirildi
Latest commit d8981e9 on 12 May
 History
 1 contributor
360 lines (342 sloc)  13.8 KB

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="css/Sehrim.css" />
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css"
    />
    <script
      src="https://kit.fontawesome.com/fcd5fc05d9.js"
      crossorigin="anonymous"
    ></script>
    <title>Şehrim</title>
  </head>
  <body>
    <!--  -->
    <!-- Navigasyon Barı -->

    <nav class="navbar navbar-expand-lg bg-info navbar-dark py-3 fixed-top">
      <div class="container">
        <a
          href="index.html"
          class="navbar-brand mb-0"
          style="font-size: 20pt; font-weight: bold"
          ><i class="fa-solid fa-mountain"></i><i> Kayseri'yi Tanıyalım</i></a
        >
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navmenu"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navmenu">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a href="index.html" class="nav-link"
                ><i class="fa-solid fa-circle-user"></i> Hakkımda</a
              >
            </li>
            <li class="nav-item">
              <a href="Ozgecmis.html" class="nav-link"
                ><i class="fa-solid fa-address-card"></i> Özgeçmiş</a
              >
            </li>
            <li class="nav-item">
              <a href="Sehrim.html" class="nav-link"
                ><i class="fa-solid fa-city"></i> Şehrim</a
              >
            </li>
            <li class="nav-item">
              <a href="Takimimiz.html" class="nav-link"
                ><i class="fa-regular fa-futbol"></i> Takımımız</a
              >
            </li>
            <li class="nav-item">
              <a href="IlgiAlanlarim.html" class="nav-link"
                ><i class="fa-solid fa-chess"></i> İlgi Alanlarım</a
              >
            </li>
            <li class="nav-item">
              <a href="Iletisim.html" class="nav-link"
                ><i class="fa-solid fa-address-book"></i> İletişim</a
              >
            </li>
            <li class="nav-item">
              <a href="Login.html" class="nav-link"
                ><i class="fa-solid fa-arrow-right-to-bracket"></i> Login</a
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Slider -->
    <section id="learn" class="p-5 bg-light">
      <div class="container bg-info sinir-bukucu">
        <div class="row align-items-center justify-content-between">
          <div
            id="carouselExampleCaptions"
            class="carousel slide"
            data-bs-ride="carousel"
          >
            <div class="carousel-indicators">
              <button
                type="button"
                data-bs-target="#carouselExampleCaptions"
                data-bs-slide-to="0"
                class="active"
                aria-current="true"
                aria-label="Slide 1"
              ></button>
              <button
                type="button"
                data-bs-target="#carouselExampleCaptions"
                data-bs-slide-to="1"
                aria-label="Slide 2"
              ></button>
              <button
                type="button"
                data-bs-target="#carouselExampleCaptions"
                data-bs-slide-to="2"
                aria-label="Slide 3"
              ></button>
              <button
                type="button"
                data-bs-target="#carouselExampleCaptions"
                data-bs-slide-to="3"
                aria-label="Slide 4"
              ></button>
            </div>
            <div class="carousel-inner">
              <div class="carousel-item active">
                <a href="Erciyes.html"
                  ><img
                    src="img/erciyes.jpg"
                    class="d-block w-100 p-3"
                    alt="erciyes-foto"
                  />
                </a>

                <div
                  class="carousel-caption d-none d-md-block bg-info"
                  style="border-radius: 16px"
                >
                  <h5>Erciyes'te Kayak Başkadır</h5>
                  <p>
                    Kış aylarında birçok turist tarafından tercih edilen Erciyes
                    Dağı.
                  </p>
                </div>
              </div>
              <div class="carousel-item">
                <a href="Manti.html"
                  ><img
                    src="img/manti.jpg"
                    class="d-block w-100 p-3"
                    alt="erciyes-foto"
                  />
                </a>

                <div
                  class="carousel-caption d-none d-md-block bg-info"
                  style="border-radius: 16px"
                >
                  <h5>Kayseri Mantısıyla Çok Ünlüdür</h5>
                  <p>
                    Bir kaşıkta 40 mantı olduğu rivayet edilen Kayseri Mantısı
                  </p>
                </div>
              </div>
              <div class="carousel-item">
                <a href="Medrese.html"
                  ><img
                    src="img/medrese.jpg"
                    class="d-block w-100 p-3"
                    alt="erciyes-foto"
                  />
                </a>

                <div
                  class="carousel-caption d-none d-md-block bg-info"
                  style="border-radius: 16px"
                >
                  <h5>Gevher Nesibe Medresesi Şehrin Bir Değeridir</h5>
                  <p>
                    Anadolu’nun ilk uygulamalı tıp medresesi olma özelliğine
                    sahiptir.
                  </p>
                </div>
              </div>
              <div class="carousel-item">
                <a href="Kale.html"
                  ><img
                    src="img/kale.jpg"
                    class="d-block w-100 p-3"
                    alt="erciyes-foto"
                  />
                </a>

                <div
                  class="carousel-caption d-none d-md-block bg-info"
                  style="border-radius: 16px"
                >
                  <h5>Şehrin Tam Merkezinde Yer Alan Kayseri Kalesi</h5>
                  <p>
                    Tedbir amaçlı yapılmış olup şehrin içinde Kayseri surları ve
                    kalesi geniş bir alana sahiptir.
                  </p>
                </div>
              </div>
            </div>
            <button
              class="carousel-control-prev"
              type="button"
              data-bs-target="#carouselExampleCaptions"
              data-bs-slide="prev"
            >
              <span
                class="carousel-control-prev-icon bg-info"
                style="border-radius: 6px"
                aria-hidden="true"
              ></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button
              class="carousel-control-next"
              type="button"
              data-bs-target="#carouselExampleCaptions"
              data-bs-slide="next"
            >
              <span
                class="carousel-control-next-icon bg-info"
                style="border-radius: 6px"
                aria-hidden="true"
              ></span>
              <span class="visually-hidden">Next</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Bilgi -->

    <article class="blog-post bg-light pb-5">
      <div class="container">
        <div class="bg-info sinir-bukucu">
          <h2 class="blog-post-title p-3">Kayseri Şehir Rehberi</h2>

          <p class="p-3">
            M.Ö. 4000 yıllarına kadar uzanan bir tarihe sahip Kayseri, Orta
            Anadolu'nun en önemli ticaret ve sanayi merkezlerinden biridir.
            Ticaretin yanında tarım da kentin sosyal ve ekonomik refahı için
            hayati bir öneme sahiptir. Kayseri son dönemde yapılan yatırımlar
            ile ülke genelinde mobilya sektörüne yön veren bir merkez halini
            almıştır.
          </p>
        </div>
        <div class="bg-dark sinir-bukucu">
          <h2 class="blog-post-title p-3 text-light">Gezilebilecek Yerler</h2>

          <p class="p-3 text-light">
            Erciyes Dağı, Selçuklu İmparatorluğu döneminden kalma camiler,
            medreseler, kümbetler, dini mekânlar, hanlar, hamamlar, bedestenler
            kentin başlıca tarihi değerleridir
          </p>
          <p class="p-3 text-light">
            Erciyes Kayak Merkezi Kayseri'deki en önemli turistik mekândır.
            Erciyes sönmüş bir yanardağ olup 3.916 m yüksekliğindedir ve Orta
            Anadolu'nun en yüksek dağıdır. Burada kayak yapmanın dışında
            dağcılık da oldukça gelişmiştir. Erciyes Dağı sahip olduğu
            platolarla yazın göz alıcı doğal bir güzelliğe bürünür. Zengin doğal
            güzellikleriyle Erciyes doğa turizmi için de elverişli bir yerdir.
          </p>
          <p class="p-3 text-light">
            Rafting için elverişli olan Zamanta Nehri şehrin diğer bir turistik
            harikasıdır. Trekking ve dağ yürüyüşlerine imkân sağlayan Kayseri,
            Sultan Sazlığı Kuş Cenneti ile ziyaretçilerine doğayla iç içe, güzel
            fırsatlar sunar. Elverişli doğa şartlarının yarattığı doğa hayatı,
            doğa turizminin gelişmesine büyük katkı sağlamaktadır.
          </p>
        </div>
        <div class="bg-info sinir-bukucu">
          <h2 class="blog-post-title p-3">Kültür ve Eğlence</h2>

          <p class="p-3">
            El sanatları şehir kültürünün en önemli parçasıdır. Taş ve ahşap
            işlemeler, halı ve kilim dokumacılığı şehirde oldukça yaygındır.
            Yüzyıllar öncesine ait tarihi evler, şehrin mimari yapısını
            oluştururken kent kültürüne de önemli katkılarda bulunmaktadır.
          </p>
          <p class="p-3">
            Kayseri'de çok yönlü ve hareketli bir eğlence hayatından bahsetmek
            zor olsa da barlar, kafeler, yüzme havuzları, doğa yürüyüşleri ve
            turları şehrin eğlenmek için sunmuş olduğu başlıca alternatiflerdir.
            Özellikle kaplıcalar, şelaleler gibi doğal güzelliklerin varlığı
            ziyaretçilere doğayla bütünleşme fırsatı verir
          </p>
        </div>
        <div class="bg-dark sinir-bukucu">
          <h2 class="blog-post-title p-3 text-light">Yeme İçme</h2>

          <p class="p-3 text-light">
            Un ve et, Kayseri mutfağının en önemli iki malzemesidir. Geleneksel
            Türk mutfağının dışında yöresel yemekler de ön plana çıkmıştır.
          </p>
          <p class="p-3 text-light">
            Mantı, Kayseri'nin en ünlü yemeğidir. Pazarlarda da satılan mantının
            evlerde yapılması ve yenmesi çok daha yaygındır. Kayseri'de yaklaşık
            36 çeşit mantı bulunmaktadır. En yaygın mantı çeşidi et ile
            yapılanıdır. Pastırma ve sucuk adeta Kayseri ile özdeşleşmiştir.
          </p>
          <p class="p-3 text-light">
            Aşmakarna kentin diğer bir popüler yemeğidir. Makarnası, eriştesi ve
            çorbası yapılmaktadır. Su böreği en çok pişirilen börek çeşididir.
            Ayrıca güveç de çok rağbet gören ve sıklıkla pişirilen bir yemektir.
            Hisarcık ve Talas ilçelerinde yerel lezzetlerin sunulduğu birçok
            restoran mevcuttur. Develi ilçesine giderseniz Cıvıklı pidesini
            tatmayı ihmal etmeyin.
          </p>
        </div>
        <div class="bg-info sinir-bukucu">
          <h2 class="blog-post-title p-3">Tatlılar</h2>

          <p class="p-3">
            Kayseri zengin bir tatlı menüsüne sahiptir. Oklava baklava, gül
            baklavası, kamış baklavası en muşhur olanlarındandır. Ayrıca üzüm ve
            dut pekmezi, incir dolması yine bilinen tatlı yiyecekler arasında
            sayılabilir.
          </p>
        </div>
        <div class="bg-dark sinir-bukucu">
          <h2 class="blog-post-title p-3 text-light">Alışveriş</h2>

          <p class="p-3 text-light">
            Halılarıyla ünlü Kayseri'nin, Yahyalı ve Bünyan halıları en
            önemlileridir. Ziyaretçilerin şehirden ayrılmadan önce mutlaka
            alması gerekenlerdir. Ayrıca Kayseri’ye gelindiğinde şehrin her
            yanındaki dükkanlardan bol miktarda pastırma ve sucuk alınabilir.
            Modern alışveriş merkezleri Kayseri Park, İpek Saray, Almer ve
            Kaseria’da birçok ünlü markayı ve kış sporları ile ilgili
            malzemeleri bulmak mümkündür.
          </p>
        </div>
      </div>
    </article>

    <!-- Footer -->

    <footer class="p-2 bg-info text-white text-center position-relative">
      <div class="container">
        <p class="lead">
          Copyright &copy; Emre Turhan</p>
          <a href="#" class="position-absolute bottom-0 end-0 p-2">
            <i class="bi bi-arrow-up-circle h1 text-dark"></i>
          </a>
        </p>
      </div>
    </footer>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
You have no unread notifications
