let items = 0;

// Seleccion de los elementos clave

const addButtons = document.querySelectorAll('.Product button'); 
const cartIcon = document.querySelector('#cart'); 
const cartList = document.querySelector('.cartList'); 
const counter = document.querySelector('.counter'); 
const openCart = document.querySelector('.openCart'); 
const closeCart = document.querySelector('.closeCart'); 
const cartModal = document.querySelector('.cartModal'); 
const cartBtn = document.getElementById("cart");

// Comprobar si hay productos en el carrito

cartBtn.addEventListener(`click`, function (event) {
  if (items === 0) {
    window.location.href = `/EmptyShoppingCart`;
  } else {

    // Abrir el modal al interactuar con el carrito

    openCart.addEventListener('click', () => {
      cartModal.showModal(); // Abrir el modal
    });
  }
});

// Array donde se almacenan los productos seleccionados

let cart = [];

// Funcion para actualizar el contador del carrito

function updateCounter() {
  counter.textContent = cart.length;
}

// Funcion para calcular el precio total de las productos en el carrito

function calculateTotalPrice() {
  return cart.reduce((total, product) => {
    const price = parseFloat(product.price.replace('€', '')); 
    return total + price;
  }, 0);
}

// Mostrar los productos en el carrito

function showCart() {
  cartList.innerHTML = ''; 
  cart.forEach((product) => {
    const item = document.createElement('li');
    

    const productText = document.createElement('span');
    productText.textContent = `${product.name} - ${product.price}`;
    
   
    item.appendChild(productText);
    cartList.appendChild(item);
  });

  // Formatear el precio total a 2 decimales

  const totalPrice = calculateTotalPrice();
  const totalItem = document.createElement('li');
  totalItem.textContent = `Total: €${totalPrice.toFixed(2)}`; 
  cartList.appendChild(totalItem);
}

//Añadir productos al carrito

addButtons.forEach((button) => {
  button.addEventListener('click', (e) => {
    const productElement = e.target.closest('.Product'); 
    if (productElement) {
      const name = productElement.querySelector('p').textContent; 
      const price = productElement.querySelector('.Price').textContent; 

   
      cart.push({ name, price });
      items++; 
      updateCounter(); 
      showCart(); 
      console.log(cart); 
    }
  });
});

// Cerar el carrito al interactuar con el boton de cerrar

closeCart.addEventListener('click', () => {
  cartModal.close(); 
});
