<template>
  <div>
    <Plot></Plot>
  </div>
</template>

<script>
import Plot from './components/Plot.vue';
import axios from 'axios';

export default {
  components: {
    Plot,
  },
  data() {
    return {
        series: [{
            name: "Data",
            data: []
        }],
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