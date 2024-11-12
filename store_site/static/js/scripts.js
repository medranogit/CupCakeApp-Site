// document.addEventListener("DOMContentLoaded", function () {
//     const buttons = document.querySelectorAll(".adicionar-carrinho");

//     buttons.forEach(button => {
//         button.addEventListener("click", function (event) {
//             event.preventDefault();

//             const produtoId = this.dataset.produtoId;
//             const url = this.dataset.url;

//             fetch(url, { method: "POST", headers: { "X-CSRFToken": getCSRFToken() } })
//                 .then(response => {
//                     if (response.ok) {
//                         return response.json();
//                     }
//                     throw new Error("Erro ao adicionar ao carrinho.");
//                 })
//                 .then(data => {
//                     alert(data.message || "Produto adicionado ao carrinho!");
//                     atualizarContadorCarrinho(data.total_itens);
//                 })
//                 .catch(error => console.error(error));
//         });
//     });

//     function atualizarContadorCarrinho(total) {
//         const contador = document.querySelector("#contador-carrinho");
//         if (contador) {
//             contador.textContent = total;
//         }
//     }

//     function getCSRFToken() {
//         return document.querySelector('[name=csrfmiddlewaretoken]').value;
//     }
// });
