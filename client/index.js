const form = document.getElementById("query-form");
const estimatedPrice = document.getElementById("estimated-price");
const queryResults = document.getElementById("query-results");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(event.target);
  let url_local = "http://127.0.0.1:5000/query_results";
  let url_nginx = "/api/query_results";
  fetch(url_nginx, {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      estimatedPrice.innerText = `Estimated Price: $${data.estimated_price}`;
      //   queryResults.innerHTML = "";
      //   for (let result of data.query_results) {
      //     const li = document.createElement("li");
      //     li.innerText = `${result.Neighborhood} - $${result.SalePrice}`;
      //     li.innerText = Object.values(result).join(" - ");
      //     queryResults.appendChild(li);
      //   }
      let placeholder = document.querySelector("#data-output");
      let out = "";
      for (let product of data.query_results) {
        out += `
        <tr>
        <td><img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80" style="width: 100px; height: auto;"></td>
            <td>${product.Neighborhood}</td>
            <td>${product.BldgType}</td>
            <td>${product.LotArea}</td>
            <td>${product.OverallQual}</td>
            <td>${product.BedroomAbvGr}</td>
            <td>${product.Bathrooms}</td>
            <td>${product.GarageCars}</td>
            <td>${product.SalePrice}</td>
        </tr>
        `;
      }
      placeholder.innerHTML = out;
    })
    .catch((error) => console.log(error));
});
