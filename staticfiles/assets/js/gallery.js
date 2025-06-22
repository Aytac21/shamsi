document.addEventListener("DOMContentLoaded", () => {
  const loadMoreBtn = document.getElementById("load-more-btn");
  const columns = Array.from(
    document.querySelectorAll("#gallery-container .col-md-4.animate-box")
  ).filter((col) => !col.classList.contains("section-head"));

  if (!loadMoreBtn || !columns.length) {
    console.log("Load more button or columns not found");
    return;
  }

  // Gallery'deki mevcut resim sayısını hesapla
  let globalImageCounter = document.querySelectorAll(".gallery-figure").length;
  console.log(`Initial image count: ${globalImageCounter}`);

  loadMoreBtn.addEventListener("click", (e) => {
    e.preventDefault();

    const nextPage = parseInt(loadMoreBtn.dataset.page) || 2;
    console.log(`Loading page: ${nextPage}`);

    loadMoreBtn.style.opacity = "0.5";
    loadMoreBtn.style.pointerEvents = "none";

    fetch(`/load-more-images/?page=${nextPage}`, {
      method: "GET",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",
      },
    })
      .then((res) => {
        console.log(`Response status: ${res.status}`);
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        console.log("Received data:", data);

        if (data.error) {
          throw new Error(data.error);
        }

        if (!data.images || data.images.length === 0) {
          throw new Error("No images received");
        }

        data.images.forEach((imgObj, index) => {
          const figure = document.createElement("figure");
          figure.className = "gallery-figure";

          const link = document.createElement("a");
          link.className = "d-block mb-4";
          link.href = imgObj.image_url;
          link.setAttribute("data-fancybox", "images");
          link.dataset.caption = `Gallery Image ${
            globalImageCounter + index + 1
          }`;

          const frameDiv = document.createElement("div");
          frameDiv.className = "gallery-frame";

          const img = document.createElement("img");
          img.className = "img-fluid gallery-img";
          img.src = imgObj.image_url;
          img.alt = `Gallery Image ${globalImageCounter + index + 1}`;
          img.loading = "lazy";

          // Resim yükleme hatası kontrolü
          img.onerror = function () {
            console.error(`Failed to load image: ${imgObj.image_url}`);
            this.src = "/static/images/placeholder.jpg"; // Placeholder image
          };

          frameDiv.appendChild(img);
          link.appendChild(frameDiv);
          figure.appendChild(link);

          // Resmi uygun kolona ekle
          const columnIndex = (globalImageCounter + index) % 3;
          if (columns[columnIndex]) {
            columns[columnIndex].appendChild(figure);
          }
        });

        globalImageCounter += data.images.length;
        console.log(`New image count: ${globalImageCounter}`);

        // Fancybox'ı yeniden başlat
        if (typeof jQuery !== "undefined" && jQuery.fancybox) {
          jQuery('[data-fancybox="images"]').fancybox({
            // Fancybox ayarları
            loop: true,
            buttons: ["zoom", "share", "slideShow", "fullScreen", "close"],
            animationEffect: "fade",
            transitionEffect: "slide",
          });
        }

        // Daha fazla sayfa var mı kontrol et
        if (data.has_next && data.next_page) {
          loadMoreBtn.dataset.page = data.next_page;
          loadMoreBtn.style.opacity = "1";
          loadMoreBtn.style.pointerEvents = "auto";
        } else {
          console.log("No more pages, removing button");
          loadMoreBtn.remove();
        }
      })
      .catch((err) => {
        console.error("Load-more error:", err);
        loadMoreBtn.style.opacity = "1";
        loadMoreBtn.style.pointerEvents = "auto";

        // Kullanıcıya daha anlamlı hata mesajı göster
        let errorMessage = "Rəsimləri yükləyərkən xəta baş verdi.";
        if (err.message.includes("404")) {
          errorMessage = "Daha fazla resim bulunamadı.";
        } else if (err.message.includes("500")) {
          errorMessage = "Sunucu hatası oluştu.";
        }

        alert(errorMessage);
      });
  });
});
