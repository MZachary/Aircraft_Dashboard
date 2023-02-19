<template>
  <div id="chart">
      <apexchart type="line" height="500" width="1000" ref="chart" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>

<script>
import VueApexCharts from 'vue3-apexcharts';

export default {
  components: {
    apexchart: VueApexCharts,
  },
  // props: ['xvalue', 'yvalue'],
  data() {
    return {
      series: [{
        name: "Data",
        data: []
      }],
          chartOptions: {
            chart: {
              id: 'realtime',
              type: 'line',
              animations: {
                enabled: true,
                easing: 'linear',
                dynamicAnimation: {
                  speed: 1000000
                }
              },
              toolbar: {
                show: false
              },
              zoom: {
                enabled: false
              }
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              curve: 'smooth'
            },
            title: {
              text: 'Dynamic Updating Chart',
              align: 'left'
            },
            markers: {
              size: 0
            },
            xaxis: {
              type: 'numeric',
              // range: XAXISRANGE,
            },
            yaxis: {
              // min: -2,
              // max: 2
            },
            legend: {
              show: false
            },
          },
    }
  }
};
</script>