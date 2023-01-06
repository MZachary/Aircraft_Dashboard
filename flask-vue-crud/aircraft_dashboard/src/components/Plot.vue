<template>
  <div id="chart">
      <apexchart type="line" height="500" width="1000" ref="chart" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>

<script>
import VueApexCharts from 'vue3-apexcharts';
import axios from 'axios';

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
  },
  methods: {
    addDataPoint() {
      // Make a request to the Flask server to retrieve the latest data point
      axios.get('http://localhost:5000/serial_data')
        .then(response => {
          // Add the data point to the chart
          this.series[0].data.push({
            x: response.data.lon,
            y: response.data.lat
          });
          this.series[0].data = this.series[0].data.slice(-100)
          // this.chartOptions.xaxis.categories.push(response.data.time_recorded);
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  mounted() {
    // Add a new data point every second
    setInterval(this.addDataPoint, 150);
  }
};
</script>