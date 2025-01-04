let items = 0;

const cartBtn = document.getElementById("cart");

cartBtn.addEventListener(`click`, function(event){
    if (items === 0){
        window.location.href = `/EmptyShoppingCart`;
    }
    else{
        window.location.href = `/ShoppingCart`;

    }
});