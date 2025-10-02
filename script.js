// Handle form submission
document.getElementById("houseForm").addEventListener("submit", async function(e) {
  e.preventDefault();
  
  const data = {
    area: document.getElementById("area").value,
    bedrooms: document.getElementById("bedrooms").value,
    bathrooms: document.getElementById("bathrooms").value,
    doors: document.getElementById("doors").value,
    age: document.getElementById("age").value,
    location: document.getElementById("location").value
  };

  const response = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  document.getElementById("result").innerText = "💰 Predicted Price: $" + result.price;
});

// ✨ AI Autofill (just random realistic values for demo)
function autoFill() {
  const randomData = {
    area: Math.floor(Math.random() * (4000 - 800) + 800),
    bedrooms: Math.floor(Math.random() * 5) + 1,
    bathrooms: Math.floor(Math.random() * 3) + 1,
    doors: Math.floor(Math.random() * 4) + 1,
    age: Math.floor(Math.random() * 50),
    location: ["newyork", "sanfrancisco", "chicago", "boston"][Math.floor(Math.random() * 4)]
  };

  document.getElementById("area").value = randomData.area;
  document.getElementById("bedrooms").value = randomData.bedrooms;
  document.getElementById("bathrooms").value = randomData.bathrooms;
  document.getElementById("doors").value = randomData.doors;
  document.getElementById("age").value = randomData.age;
  document.getElementById("location").value = randomData.location;
}
