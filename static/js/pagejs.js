// Sections sliding in from left to right
const observer = new IntersectionObserver((entries)=> {
    entries.forEach((entry) => {
        console.log(entry)
        if(entry.isIntersecting){
            entry.target.classList.add('show');
        } /*else{
            entry.target.classList.remove('show');
        } If the text should go back to hidden when not in the page
        and the transition hapens again */
    });
});
// text transition. Sliding in
const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el)=> observer.observe(el));

// Hiding sections and displaying them when the button is clicked
function hideorshow(data) {
    var x = document.getElementById(data);
    if (x.style.display == "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
}