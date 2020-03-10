<template>
  <div class="buscar-candidato py-3">
    <i class="fa fa-spin fa-spinner fa-4x" v-if="loading"/>

    <div style="font-size: 2rem" v-else-if="!listagem.length">
      Ops... Nenhum resultado para sua busca
    </div>

    <div class="resultados-busca" v-else>
      <h2>Resultados da busca para {{ $route.params.query }}</h2>
      <hr>

      <div class="list-group">
        <a href="#" class="list-group-item list-group-item-action" :key="candidato.email" v-for="candidato in listagem">
          {{ candidato.email }}
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    loading: true,
    candidatos: [
      {
        email: 'johndoe@gmail.com'
      },
      {
        email: 'fulanodetal@gmail.com'
      },
      {
        email: 'candidatonovo@gmail.com'
      }
    ]
  }),

  created () {
    setTimeout(() => {
      this.loading = false
    }, 500)
  },

  computed: {
    listagem () {
      return Math.floor(Math.random() * 10, 1) % 2 === 1 ? this.candidatos : []
    }
  }
}
</script>

<style lang="scss">
  .buscar-candidato {
    display: flex;
    align-items: center;
    justify-content: center;
    height: calc(100vh - 200px);

    .resultados-busca {
      width: 100%;
      align-self: start;
    }
  }
</style>
