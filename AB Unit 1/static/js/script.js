let items = 0;

const cartBtn = document.getElementById("cart");

cartBtn.addEventListener(`click`, function(event) {
  if (items === 0) {
    window.location.href = `/EmptyShoppingCart`;
  } 
});

// Select key elements
const addButtons = document.querySelectorAll('.Product button'); // Add to cart buttons
const cartIcon = document.querySelector('#cart'); // Cart icon
const cartModal = document.querySelector('.cartModal'); // Cart modal
const cartList = document.querySelector('.cartList'); // Cart items list
const closeCartButton = document.querySelector('.closeCart'); // Close button for the cart modal
const counter = document.querySelector('.counter'); // Cart counter

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
    const name = productElement.querySelector('p').textContent; // Get product name
    const price = productElement.querySelector('.Price').textContent; // Get product price

    // Add product (name and price) to the cart
    cart.push({ name, price });
    items++; // Increment item count
    updateCounter(); // Update the cart counter
  });
});

// Show or hide the cart modal
cartIcon.addEventListener('click', () => {
  if (cart.length === 0) {
    window.location.href = "/EmptyShoppingCart"; // Redirect if cart is empty
  } else {
    cartModal.classList.toggle('hidden'); // Toggle modal visibility
    showCart(); // Show products in the modal
  }
});

// Close the cart modal
closeCartButton.addEventListener('click', () => {
  cartModal.classList.add('hidden'); // Hide the modal
});
