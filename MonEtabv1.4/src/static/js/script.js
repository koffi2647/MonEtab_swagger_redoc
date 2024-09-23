
const ctx = document.getElementById("pieChart").getContext("2d");
const pieChart = new Chart(ctx, {
  type: "pie",
  data: {
    labels: ["Homme", "Femme"],
    datasets: [
      {
        data: [60, 40],
        backgroundColor: ["#3498db", "#e74c3c"],
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: "right",
      },
    },
  },
});

