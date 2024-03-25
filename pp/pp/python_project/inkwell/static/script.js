const slides = document.querySelector('.slides');

const slideWidth = 1500;
let counter = 0;



function nextSlide() {
  if (counter < 4) {
    counter++;
  } else {
    counter = 0;
  }
  slides.style.transform = `translateX(-${slideWidth * counter}px)`;
  
}

function prevSlide() {
  if (counter > 0) {
    counter--;
  } else {
    counter = 4;
  }
  slides.style.transform = `translateX(-${slideWidth * counter}px)`;
 
}

function goToSlide(index) {
  counter = index;
  slides.style.transform = `translateX(-${slideWidth * counter}px)`;
 
}


setInterval(nextSlide, 3000); // Change slide every 3 seconds
