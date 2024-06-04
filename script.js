// Get the hero element
const hero = document.getElementById('hero');

if ({ temp } < 10) {
    hero.style.backgroundImage = 'url("../static/cold.jpeg")';
} else if ({ temp } >= 10 && { temp } < 20) {
    hero.style.backgroundImage = 'url("../static/mild.jpeg")';
} else {
    hero.style.backgroundImage = 'url("../static/hot.jpeg")';
}
