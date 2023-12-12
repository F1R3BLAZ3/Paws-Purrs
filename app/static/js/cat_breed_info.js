// this is for the cat_breed_info.html

var currentImageIndex = 0;
var imagesInfo = JSON.parse("{{ images_info| tojson | safe }}");

function openModal(index) {
  var modal = document.getElementById("myModal");
  var modalImg = document.getElementById("img01");

  modal.style.display = "block";
  currentImageIndex = index >= 0 && index < imagesInfo.length ? index : 0;
  modalImg.src = imagesInfo[currentImageIndex].url;
}

function closeModal() {
  document.getElementById("myModal").style.display = "none";
}

function changeImage(offset) {
  currentImageIndex += offset;
  if (currentImageIndex < 0) {
    currentImageIndex = imagesInfo.length - 1;
  } else if (currentImageIndex >= imagesInfo.length) {
    currentImageIndex = 0;
  }
  document.getElementById("img01").src = imagesInfo[currentImageIndex].url;
}

function nextImage() {
  changeImage(1);
}

var prevBreedId = "{{ prev_breed_id }}";
var nextBreedId = "{{ next_breed_id }}";

var prevImage = document.querySelector(".navigation a:first-child img");
var nextImage = document.querySelector(".navigation a:last-child img");

prevImage.addEventListener("click", function () {
  if (prevBreedId) {
    window.location.href =
      "{{ url_for('get_cat_breed_info', breed_id=prevBreedId) }}";
  }
});

nextImage.addEventListener("click", function () {
  if (nextBreedId) {
    window.location.href =
      "{{ url_for('get_cat_breed_info', breed_id=nextBreedId) }}";
  }
});
