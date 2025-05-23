document.addEventListener("DOMContentLoaded", () => {
  const loadMoreBtn = document.getElementById("load-more-btn");
  const columns = Array.from(
    document.querySelectorAll(".col-md-4.animate-box")
  );

  let colIndex = 0;

  if (!loadMoreBtn || !columns.length) return;

  loadMoreBtn.addEventListener("click", () => {
    const nextPage = loadMoreBtn.dataset.page || 2;

    fetch(`/load-more-images/?page=${nextPage}`, {
      headers: { "x-requested-with": "XMLHttpRequest" },
    })
      .then((res) => res.json())
      .then((data) => {
        data.images.forEach((imgObj) => {
          const figure = document.createElement("figure");

          const link = document.createElement("a");
          link.className = "d-block mb-4";
          link.href = imgObj.image_url;
          link.setAttribute("data-fancybox", "images");
          link.dataset.caption = `Image #${imgObj.id}`;

          const img = document.createElement("img");
          img.className = "img-fluid";
          img.src = imgObj.image_url;
          img.alt = "Gallery Image";

          link.appendChild(img);
          figure.appendChild(link);

          columns[colIndex].appendChild(figure);
          colIndex = (colIndex + 1) % columns.length;
        });

        if (window.Fancybox) {
          Fancybox.bind("[data-fancybox='images']");
        }

        if (data.has_next) {
          loadMoreBtn.dataset.page = data.next_page;
        } else {
          loadMoreBtn.remove();
        }
      })
      .catch((err) => console.error("Load-more error:", err));
  });
});
