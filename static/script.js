let input = document.querySelector('input[name="fake-news-input"]');
let button = document.querySelector('button');


button.addEventListener("click", () => {
    console.log("Button clicked");
    console.log("Input value:", input.value);
});
