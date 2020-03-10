<template>
  <div class="buscar-candidato">
    <i class="fa fa-spin fa-spinner fa-4x" v-if="loading"/>

    <div style="font-size: 2rem" v-else>
      Ops... Nenhum resultado para sua busca
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    loading: true
  }),

  created () {
    setTimeout(() => {
      this.loading = false
    }, 3000)
  }
}
</script>

<style lang="scss">
  .buscar-candidato {
    display: flex;
    align-items: center;
    justify-content: center;
    height: calc(100vh - 200px);
  }
</style>
