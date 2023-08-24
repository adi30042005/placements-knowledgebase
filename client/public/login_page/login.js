const inputs = document.querySelectorAll(".input-field");
const toggle_btn = document.querySelectorAll(".toggle");
const main = document.querySelector("main");
const bullets = document.querySelectorAll(".bullets span");
const images = document.querySelectorAll(".image");

inputs.forEach((inp) => {
  inp.addEventListener("focus", () => {
    inp.classList.add("active");
  });
  inp.addEventListener("blur", () => {
    if (inp.value != "") return;
    inp.classList.remove("active");
  });
});

toggle_btn.forEach((btn) => {
  btn.addEventListener("click", () => {
    main.classList.toggle("sign-up-mode");
  });
});

function moveSlider() {
  let index = this.dataset.value;

  let currentImage = document.querySelector(`.img-${index}`);
  images.forEach((img) => img.classList.remove("show"));
  currentImage.classList.add("show");

  const textSlider = document.querySelector(".text-group");
  textSlider.style.transform = `translateY(${-(index - 1) * 2.2}rem)`;

  bullets.forEach((bull) => bull.classList.remove("active"));
  this.classList.add("active");
}

bullets.forEach((bullet) => {
  bullet.addEventListener("click", moveSlider);
});

const carouselImages = document.querySelectorAll(".carousel .image");
const textSlider = document.querySelector(".text-slider .text-group");

let currentIndex = 0;
const slideInterval = 3000; 

function showSlide(index) {
  carouselImages.forEach((image, i) => {
    image.classList.remove("show");
    bullets[i].classList.remove("active");
  });
  carouselImages[index].classList.add("show");
  bullets[index].classList.add("active");

  textSlider.style.transform = `translateY(${-(index * 2.2)}rem)`;
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % carouselImages.length;
  showSlide(currentIndex);
}

function startCarousel() {
  setInterval(nextSlide, slideInterval);
}

window.addEventListener("load", startCarousel);
