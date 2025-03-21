document.addEventListener("DOMContentLoaded", function () {

    // Função para carregar os dados do JSON
    async function fetchData() {
        const response = await fetch("output.json");
        const data = await response.json();
        return data;
    }

    // Função para criar gráficos dinamicamente
    async function generateCharts() {
        const data = await fetchData();

        // 📈 Gráfico de Receita vs Despesas vs Lucro
        if (data.financial_projections_break_even_and_ROI) {
            let years = data.financial_projections_break_even_and_ROI["3_year_financial_projection"].yearly_projections.map(p => p.year);
            let revenue = data.financial_projections_break_even_and_ROI["3_year_financial_projection"].yearly_projections.map(p => p.revenue);
            let expenses = data.financial_projections_break_even_and_ROI["3_year_financial_projection"].yearly_projections.map(p => p.expenses);
            let profit = data.financial_projections_break_even_and_ROI["3_year_financial_projection"].yearly_projections.map(p => p.profit);

            let revenueChart = { x: years, y: revenue, name: "Receita", mode: "lines+markers", line: { color: "green" } };
            let expenseChart = { x: years, y: expenses, name: "Despesas", mode: "lines+markers", line: { color: "red" } };
            let profitChart = { x: years, y: profit, name: "Lucro", mode: "lines+markers", line: { color: "blue" } };

            Plotly.newPlot("revenue_projection_chart", [revenueChart, expenseChart, profitChart], {
                title: "Projeção Financeira",
                xaxis: { title: "Ano" },
                yaxis: { title: "Valor (R$)" }
            });
        }

        // 💰 Gráfico de Investimento por Categoria
        if (data.investment_structure_and_operational_costs) {
            let categories = Object.keys(data.investment_structure_and_operational_costs.initial_investment.breakdown_by_items);
            let values = Object.values(data.investment_structure_and_operational_costs.initial_investment.breakdown_by_items);

            Plotly.newPlot("investment_chart", [{
                x: categories,
                y: values,
                type: "bar"
            }], {
                title: "Distribuição do Investimento Inicial",
                xaxis: { title: "Categoria" },
                yaxis: { title: "Valor (R$)" }
            });
        }

        // 🏪 Gráfico de Tendências de Mercado (Pie Chart)
        if (data.market_and_competitive_analysis) {
            let marketTrends = data.market_and_competitive_analysis.key_market_trends;

            Plotly.newPlot("market_trends_chart", [{
                labels: marketTrends,
                values: marketTrends.map(() => 100 / marketTrends.length),
                type: "pie"
            }], {
                title: "Tendências de Mercado"
            });
        }
    }

    generateCharts();
});
