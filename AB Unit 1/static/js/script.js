let items = 0;

// Select key elements
const addButtons = document.querySelectorAll('.Product button'); // Add to cart buttons
const cartIcon = document.querySelector('#cart'); // Cart icon
const cartList = document.querySelector('.cartList'); // Cart items list
const counter = document.querySelector('.counter'); // Cart counter
const openCart = document.querySelector('.openCart'); // Button to open the cart modal
const closeCart = document.querySelector('.closeCart'); // Close button for the cart modal
const cartModal = document.querySelector('.cartModal'); // The modal itself
const cartBtn = document.getElementById("cart");


cartBtn.addEventListener(`click`, function(event) {
  if (items === 0) {
    window.location.href = `/EmptyShoppingCart`;
  } 
  else {
    // Open the cart modal on button click
    openCart.addEventListener('click', () => {
    cartModal.showModal(); // Open the modal
});
  }
});

// Array to store cart items
let cart = [];

// Update the cart counter
function updateCounter() {
  counter.textContent = cart.length; // Update counter display
}

// Display the products in the cart modal
function showCart() {
  cartList.innerHTML = ''; // Clear existing items
  cart.forEach((product) => {
    const item = document.createElement('li');
    
    // Create product details (name and price)
    const productText = document.createElement('span');
    productText.textContent = `${product.name} - ${product.price}`;
    
    // Append product text to the item
    item.appendChild(productText);
    cartList.appendChild(item);
  });
}

// Add products to the cart
addButtons.forEach((button) => {
  button.addEventListener('click', (e) => {
    const productElement = e.target.closest('.Product'); // Get the product element
    if (productElement) {
      const name = productElement.querySelector('p').textContent; // Get product name
      const price = productElement.querySelector('.Price').textContent; // Get product price

      // Add product (name and price) to the cart
      cart.push({ name, price });
      items++; // Increment item count
      updateCounter(); // Update the cart counter
      showCart(); // Show updated cart in the modal
      console.log(cart); // Log the cart items
    }
  });
});



// Close the cart modal on button click
closeCart.addEventListener('click', () => {
  cartModal.close(); // Close the modal
});
