document.addEventListener("DOMContentLoaded", function () {

    // Exemplo: Receita vs Despesas vs Lucro
    var revenueChart = {
        x: [1, 2, 3],
        y: [850000000, 1100000000, 1400000000],
        name: "Receita",
        mode: "lines+markers",
        line: { color: "green" }
    };

    var expenseChart = {
        x: [1, 2, 3],
        y: [720000000, 800000000, 850000000],
        name: "Despesas",
        mode: "lines+markers",
        line: { color: "red" }
    };

    var profitChart = {
        x: [1, 2, 3],
        y: [130000000, 300000000, 550000000],
        name: "Lucro",
        mode: "lines+markers",
        line: { color: "blue" }
    };

    Plotly.newPlot("revenue_projection_chart", [revenueChart, expenseChart, profitChart], {
        title: "Projeção Financeira",
        xaxis: { title: "Ano" },
        yaxis: { title: "Valor (R$)" }
    });

    // Exemplo: Investimentos por Categoria
    var investmentData = [{
        x: ["Infraestrutura", "Equipamentos", "Inventário", "Marketing", "Legal", "Outros"],
        y: [500000000, 300000000, 100000000, 150000000, 50000000, 100000000],
        type: "bar"
    }];

    Plotly.newPlot("investment_chart", investmentData, {
        title: "Distribuição do Investimento Inicial",
        xaxis: { title: "Categoria" },
        yaxis: { title: "Valor (R$)" }
    });

    // Exemplo: Tendências de Mercado (Pie Chart)
    var marketTrendsData = [{
        labels: ["Snacks Saudáveis", "E-commerce", "Ingredientes Naturais"],
        values: [40, 35, 25],
        type: "pie"
    }];

    Plotly.newPlot("market_trends_chart", marketTrendsData, {
        title: "Tendências de Mercado"
    });

});
