<template>

  <div>
    <label for="serial-port-select">Select Serial Port:</label>
    <select id="serial-port-select" v-model="selectedPort">
      <option v-for="port in serialPorts" :key="port">{{ port }}</option>
    </select>
    <div>
      <button @click="sendSelectedPort">Save Port</button>
    </div>
  </div>

  <div>
    <button @click="startAddingData">Start</button>
    <button @click="stopAddingData">Stop</button>
    <button @click="sendToCSV">CSV</button>
  </div>

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
        selectedPort: '',
        serialPorts: [],

        soundMap: {
          1 : '@/assets/sounds/beginning_preflight_check.mp3'
        },
    }
  },
  methods: {
    // these 2 functions arent working
    startAddingData() {
      if (!this.intervalId) {
        this.intervalId = setInterval(this.addDataPoint, 150);
      }
  },

    stopAddingData() {
      if (this.intervalId) {
        clearInterval(this.intervalId);
        this.intervalId = null;
      }
    },

    addDataPoint() {
      // Make a request to the Flask server to retrieve the latest data point
      axios.get('http://localhost:5000/serial_data')
        .then(response => {
          // Add the data point to the chart
          this.series[0].data.push({
            x: response.data.lon,
            y: response.data.lat,
            sound_bit: response.data.sound_bit
          });
          this.series[0].data = this.series[0].data.slice(-100)
          // this.chartOptions.xaxis.categories.push(response.data.time_recorded);

          if (response.data.sound_bit === 1) {
            const audio = new Audio(this.soundMap[response.data.sound_bit]);
            audio.play();
          }
        })
        .catch(error => {
          console.error(error);
        });
    },

    get_serial_ports(){
      axios.get('http://localhost:5000/serial_ports')
        .then(response => {
          this.serialPorts = response.data;
          // Set 'none' as default port to not break anything
          this.selectedPort = 'none';
        })
        .catch(error => {
          console.log(error);
        })
    },

    sendSelectedPort(){
      axios.post('http://localhost:5000/selected_port', {
        port: this.selectedPort
      })
        .then(response => {
          console.log(response.data);
      })
        .catch(error => {
          console.error(error);
      });

    },
  },
  mounted() {
    // Add a new data point every second
    // no longer needed b/c ive added turn on and off buttons
    setInterval(this.addDataPoint, 150);
    this.get_serial_ports();
  }
};
</script>