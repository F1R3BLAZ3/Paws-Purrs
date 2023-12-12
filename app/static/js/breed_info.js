// breed_info.js
var currentImageIndex = 0;
var imagesInfo = {{ images_info | tojson | safe }};

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
