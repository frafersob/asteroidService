<template>
  <div class="asteroid">
    <h1>{{ msg }}</h1>
    <div class="card-body">
      <form @submit="searchSighting">
        <strong>Rasterized Matrix (ex. 1011):</strong>
        <input type="text" class="form-control" v-model="matrix">
        <strong>Matrix Dimensions (ex. 2x2):</strong>
        <input type="text" class="form-control" v-model="dimensions">
        <button class="btn btn-success">Submit</button>
      </form>
    </div>
    <pre>
      {{errorText}}
    </pre>
    <div
      v-for="sighting in sightings"
      class="sighting"
    >
      Asteroid {{sighting.asteroid_code}}: Avistado el {{sighting.date}} a las {{sighting.time}} por el observatorio {{sighting.observatory_code}}

    </div>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: 'asteroid',
  data () {
    return {
      msg: 'Bienvenido al servicio de consulta de asteroides',
      matrix: '',
      dimensions: '',
      errorText: '',
      sightings: null
    }
  },
  methods: {
    searchSighting(e) {
      e.preventDefault();
      let currentObj = this;
      axios.get("http://127.0.0.1:8000/asteroid/"+this.matrix+"/"+this.dimensions)
      .then(function (response) {
        currentObj.sightings = response.data;
        currentObj.errorText = null;
      })
      .catch(function (error) {
        if(String(error).includes('404'))
          currentObj.errorText = "Error: Asteroid not found"
        else if (String(error).includes('500'))
          currentObj.errorText = "Error: Wrong entry format";
      });
    }
  }
}

var matrix = '10101111';
var dimensions = '2x4';
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #35495E;
}
</style>
