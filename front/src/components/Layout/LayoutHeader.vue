<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">
      <img src="../../assets/images/contractt-min.png" height="70">
    </a>

    <div class="collapse navbar-collapse">
      <form class="form-inline ml-auto" @submit.prevent="buscarCandidato()">
        <div class="input-group mb-3">
          <input
            required
            type="text"
            v-model="busca"
            class="form-control"
            placeholder="Buscar candidato"
          >

          <div class="input-group-append">
            <button class="btn btn-outline-secondary">
              <i class="fa fa-search"></i>
            </button>
          </div>
        </div>
      </form>
    </div>
  </nav>
</template>

<script>
export default {
  data: () => ({
    busca: ''
  }),

  methods: {
    buscarCandidato () {
      this.$router.push({
        name: 'BuscarCandidato',
        params: {
          query: this.busca
        }
      })
    }
  }
}
</script>
